# Set up a CI-CD pipeline in Jenkins

## Objectives

Learn:
- To design a CI-CD pipeline
- To build a CI-CD pipeline using Jenkins
- To interact with AWS using the command line
- How to connect different developer tools to each other in order to automate
  the software development lifecycle
- To debug connectivity issues between tools running in the Cloud

## Task: Create a diagram of your desired pipeline

Previously we mentioned how a CI-CD pipeline involves running tests and checks
on our codebase, and then if those tests pass deploying the code to a production
cloud environment.

You previously learned how Docker works and how to containerise an application. Now we're going to wire that into a CI-CD pipeline — so that every time you push code to GitHub, Jenkins will automatically build your Docker image, push it to a container registry, and deploy it to Fargate, a fully managed container platform on AWS.

The application you'll be deploying is a Python Flask app with a built-in AI assistant, powered by a small language model running inside your container — no external API keys required.

<!-- These sorts of checks are a powerful way to improve quality in the systems in
our care, as they will run automatically and help our teams to catch issues
before they get to production. The app not deploying is a pretty strong
incentive to fix the problem! -->

Before we get started, take a moment to diagram out in more detail what this
pipeline is going to have to do, and in what order.

Here's a starting point:

![Insert new diagarams](assets/deployment_process_diagram.png?raw=true
"Deployment process diagram")

Copy out this diagram and add some detail to what Jenkins will need to do.

> :information_source: The resources shared with you during the [CI-CD change
> workshop](https://github.com/makersacademy/devops-course/blob/main/workshops/week-2/ci_cd_overview.md)
> might help with this.

## Task: Set up the pipeline

Your task is to set up a CI-CD pipeline in Jenkins according to your design.

You should expect this task to be challenging, and to require significant
research and exploration. You may find out part way through that you need to
change your approach. This is all OK and expected.

Nevertheless, I've broken down the key steps below along with some resources
for you to use. You can try to follow the below closely, or discard it and find
your own way.

## Key steps

1. **Set up a new local git repository for your Flask application.**
   Copy the files from `app/` to a new directory outside of this one and
   set it up as a local git repository.

2. **Push your local repository to a new, private Github repository.**  
   Why private? Public will make it easier, but you will be missing some key
   learning for this module, as most repositories in your jobs will be private.

3. **Set up Amazon ECR (Elastic Container Registry)**
ECR is AWS's Docker image registry — it's where Jenkins will push your built images, and where Fargate will pull them from.  

4. **Set up Amazon ECS + Fargate**
In last week's task you had a look at ECS and Fargate, refer back to last week's notes as a reminder. 

5. **Create a new pipeline in Jenkins.**

6. **Add a pipeline script.**
      This script should:
   
   1. Clone your repository using the right credentials (more below)
   2. Build a Docker image from your Dockerfile
   3. Push the image to ECR
   4. Deploy the new image to your Fargate service

   You are welcome to attempt this work yourself, _however you will encounter
   significant challenges._ These are thrilling challenges representative of
   what your work will be like as a cloud engineer, so if you feel ready I
   absolutely recommend you go for it.

   However, if you are feeling pretty stretched already, I recommend you instead
   use the sample script in the [Resources Section](#resources), which should
   work without too much trouble.

7. **Add your Github credentials.**
      Jenkins won't magically know your details to access your private repository,
   so you need to provide it with some. You can add these in Manage Jenkins ->
   Credentials -> Global -> Add Credentials.

   Select "Username with password" as the kind.  Put your Github username in the
   'Username' field. Don't put in your Github password to the password field —
   it won't work.
   
   You'll then need to go to Github, finding Settings -> Developer Settings ->
   Personal Access Tokens -> Fine Grained Tokens -> Generate new token.

   The token you're generating will give Jenkins access to perform certain
   actions on your behalf. According to the principle of least privilege (agents
   in a system should have the least permissions necessary to perform their
   work) you should endeavour to give the token permissions _only_ to your
   repository, and _only_ those permissions necessary. These are: 

   * Repository Permissions -> Commit statuses: Read and Write
   * Repository Permissions -> Contents: Read-only
   * Repository Permissions -> Metadata: Read-only

   Generate the token, and then put it in the Password field of your Jenkins
   credentials form. Then hit Create.

   Once you've done this, you'll see that your credential gets an ID. Copy this
   ID and enter it into your pipeline script (if you're using the sample, this
   is called `your-git-credentials-id`)


8. **Try running your pipeline.**
      Go to your pipeline and click 'Build Now'. If everything's working right,
   this should run 'Clone Repo' and 'Install Dependencies' successfully, and
   then fail at 'Run HTML Check' with some errors about invalid HTML. 
   
   This is good — your check is properly failing and your pipeline is now
   failing.


9. **Run your build.**
      After this, your build should pass. Go to ECS → Clusters → your cluster →
   Tasks to find the public IP of your running container. Open
   `http://<public-ip>:5000` in your browser — you should see your Flask app
   running live.

   > Note: the first time the container starts it needs to pull the AI model,
   > which can take a few minutes. If the app isn't responding immediately,
   > wait a moment and try again.

10. **Set up a Github webhook.**
     Right now you need to run the CI-CD pipeline manually. Typically these
    pipelines run automatically on a change to the main branch. To achieve this
    you will need to tell Github to inform Jenkins when you push new code.

    You'll need to integrate Github with Jenkins using a feature called
    Webhooks.


## Check your work

To check you've got everything working correctly:

1. Make a change to your Flask app. Perhaps update the heading in `templates/index.html`.
2. Push it to Github.
3. Don't manually run your build on Jenkins, wait for it to kick in automatically.
4. Watch the build go green.
5. Load up your app and verify that it has changed.

## Resources

A sample Jenkins pipeline script:

```
pipeline {
    agent any
 environment {
        GIT_CREDENTIALS  = 'your-git-credentials-id'
        AWS_REGION       = 'eu-west-2'
        ECR_REPO         = 'YOUR_ACCOUNT_ID.dkr.ecr.eu-west-2.amazonaws.com/my-ai-app'
        ECS_CLUSTER      = 'name'
        ECS_SERVICE      = 'my-ai-service'
        IMAGE_TAG        = "${BUILD_NUMBER}"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', credentialsId: env.GIT_CREDENTIALS, url: 'https://github.com/YOUR_REPOSITORY_URL'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $ECR_REPO:$IMAGE_TAG .'
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region $AWS_REGION | \
                    docker login --username AWS --password-stdin $ECR_REPO
                    docker push $ECR_REPO:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy to Fargate') {
            steps {
                sh '''
                    aws ecs update-service \
                        --cluster $ECS_CLUSTER \
                        --service $ECS_SERVICE \
                        --force-new-deployment \
                        --region $AWS_REGION
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Your app is deploying to Fargate.'
        }
        failure {
            echo 'Pipeline failed. Check the console output above for errors.'
        }
    }
}
```

A sample policy for your User Group:

```json
{
    "Version": "2012-10-17",
    "Statement": [
         {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:PutImage",
        "ecr:InitiateLayerUpload",
        "ecr:UploadLayerPart",
        "ecr:CompleteLayerUpload",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecs
:UpdateService",
        "ecs:DescribeServices",
        "ecs:RegisterTaskDefinition",
        "iam:PassRole"
      ],
      "Resource": "*"
    }           
    ]
}
```



[Next Challenge](04_set_up_serverless.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->

# Serverless CI-CD


Forking the Repository
You will have to push changes to Github in order to trigger the CI/CD pipeline. Therefore, before going any further in this tutorial, fork this repository and work on your own fork from now on. If you have never forked a repository, this might help.

Preparing the Deployment Environment
The simplest way to get a container running on AWS is to use Fargate, so we will use a sample Fargate deployment which takes care of everything for us: VPC, SGs, IAM and the cluster itself.

NOTE: Fargate is only available on the us-east-1 region at the time of writing, so we will use this region.

Perform the following steps to prepare the Fargate environment for our deployment:

Log in to the ECS console under the us-east-1 region (or simply click here).
Click Get Started.
Under Container definition, leave the sample-app option selected and click Next.
Under Load balancer type choose Application Load Balancer and click Next.
If you want, change the name of the cluster under Cluster name. Click Next.
Click Create.
The cluster should now be created along with all required resources. A sample app will be automatically deployed on the cluster once created (this could take a few minutes).

Verify that the sample app works by browsing the DNS name of the load balancer. To find the DNS name you can click the link near Load balancer in the cluster creation status page, or find the load balancer in the Load Balancers view.

Prepare a Docker Repository on ECR
The pipeline you are about to create will generate Docker images, which need to be pushed to some Docker registry. Since we are on AWS we can easily use ECR for this purpose, however you may use other Docker registries as well.

To create a repository on ECR, follow these steps:

On the Repositories section on the ECS console, click Get started or Create repository.
Under Repository name type "sample-app" and click Next step then Done.
Make note of the Repository URI - you will need it later.

This repository provides a skeleton with some files in order for you to get
started creating:

- your own CI-CD solution using [Jenkins](https://www.jenkins.io/) 
- a Serverless backend for the site you will be deploying using [AWS
  Lambda](https://aws.amazon.com/lambda/) and [Amazon API
  Gateway](https://aws.amazon.com/api-gateway/), following a common industry
  pattern.

On this page you will find:

- [Diagrams](#desired-application-and-deployment-process) that serve as the main
  description of what you should be building.
- A series of high-level [tasks](#getting-started) to guide you through the
  project.
- Some [documentation](#project-files) to help you understand the files in this
  repo 

## Desired application and deployment process

Below, you fill find some diagrams that describe the system you have been asked to build in a bit more detail. 

Even so, you'll find that they leave some questions unanswered: some arrows have been left unlabelled and the inner workings of some of the tools involved are not explained. The missing bits are for you to research and discover!

### Application diagram

The following diagram shows how the application should work once deployed. 

![Application diagram](assets/application_diagram.jpg?raw=true "Application
diagram")

The diagram shows that the app is composed of:
- a static site hosted on S3 and accessible through the browser,
- and a backend which the site sends requests to.

It also shows that the backend should be powered by AWS Lambda and that the
frontend should access AWS Lambda through a service called Amazon API Gateway.

### Deployment process diagram

The next diagram illustrates how the application should be deployed:

- The code for the app should be hosted on GitHub
- Jenkins should be used to automatically deploy the application code to AWS S3.
  
![Deployment process diagram](assets/deployment_process_diagram.jpg?raw=true
"Deployment process diagram")

## Getting Started

As a team, using the diagrams and high-level tasks shared below as a starting
point, map out what you understand so far and what open questions you will need
to research.

**Keep modifying and expanding the diagrams you've been given with what you
find.** At the end of the week, you can submit them to your coach for feedback.
Your coach may also ask you to discuss your diagrams during group check-ins.

### Tasks

1. [Set up Deployment Environment](01_set_up_ecs_and_fargate.md)
2. [Set up Jenkins](02_set_up_jenkins.md)
3. [Set up a CI-CD pipeline in Jenkins](03_set_up_pipeline.md)
4. [Set up the Serverless backend](04_set_up_serverless.md)
5. [Bonus tasks: Deepen your understanding, consolidate and
   explore](05_bonus.md)

## Project files

- In the `app` folder you will find the files for a the application. These are the app files will be  containerised and deploy to fargate.
- `resources/deploy_ec2_network_v2.json` is the
  [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
  template to automate the process of creating an EC2 instance on AWS, assign
  the necessary roles and policies and add some security settings that are
  needed for Jenkins to be able to run on the EC2 instance. Note that you do not
  need to know what the whole template does line by line. We will, in fact,
  spend some more time next week working with these concepts on AWS.
- `resources/your-first-lambda.py` is the Lambda function that you will deploy
  in AWS and eventually invoke once you deploy your static website on AWS.
  Modify it to include the names of your group members.
- `assets` folder: files in this folder doesn't need to be deployed. It contains
  support assets for this README (e.g. images).


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->

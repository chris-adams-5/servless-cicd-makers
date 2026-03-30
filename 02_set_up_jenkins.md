# Set up Jenkins

## Objectives

Learn to:
- Use a fundamental AWS service: EC2
- Use SSH to connect to a virtual machine in the Cloud
- Install software on a virtual machine in the Cloud
- Understand the benefits of hosting developer tools in the Cloud

## Task: Set up the Jenkins Server

EC2 stands for Elastic Compute Cloud. It is a service that provides virtual
machines in the Cloud. You can think of it as a service that provides virtual
computers that you can use for whatever you want.

CloudFormation is a service that allows you to describe the cloud infrastructure
you want using a configuration file which you then upload to AWS. AWS will then
manage the lifecycle of the infrastructure you've created.

Jenkins is a piece of software called an automation server. One of the big
things it automates is Continuous Integration (running tests in the cloud) and
Continuous Deployment (deploying software to the cloud).

Your task is to use the [CloudFormation
template](resources/deploy_ec2_network_v2.json) provided in this repository to
set up some infrastructure on EC2, and then deploy Jenkins onto it.

You will need to add your bucket name to the template before uploading it.

## Key steps

1. Create a new key pair in EC2. You will need this for the next step.
2. Go to CloudFormation and create a new stack, uploading the configuration file.  
   Select the instance type 't2.micro' and the key pair you created in step one.
4. In the outputs, find the name of your ecr-repo you created in the first step  to the `ecr repo name` input
5. SSH into your server using the `.pem` key you downloaded in step one. The
   username will be `ec2-user`.
6. The EC2 provided has Jenkins running.
- SSH into your server (you've already done this in week 1)
- You can check Jenkins is installed and running with this command `sudo systemctl status jenkins`


## Check your work

1. Go to CloudFormation.
2. Click on the stack you created.
3. Click on the 'Outputs' tab.
4. Copy the `InstanceDns` value.
5. The server is running port 8080 using HTTP, so visit something like:  
   `http://YOUR_INSTANCE_DNS_VALUE:8080/`
6. You should see something like this:  

   ![A screenshot showing the Jenkins welcome screen](assets/jenkins_installed.png)

7. Log in using your username and password.
8. You should see something like this:  

   ![A screenshot showing the Jenkins dashboard](assets/jenkins_dashboard.png)


[Next Challenge](03_set_up_pipeline.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=02_set_up_jenkins.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=02_set_up_jenkins.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=02_set_up_jenkins.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=02_set_up_jenkins.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=02_set_up_jenkins.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->

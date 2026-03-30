# Set up ECS and Fargate

## Objectives

Learn to:
- Use two fundamental AWS services: ECR and ECS
- Understand how containers are stored and run in the cloud
- Set up a serverless container hosting environment using Fargate

## Background

Last week you learnt how to build Docker containers and run them on EC2 and Fargate. This week we will continue with that with a focus on building jenkins pipelines to automate the deployment of the containers

You will have to push changes to Github in order to trigger the CI/CD pipeline. Therefore, before going any further in this tutorial, copy the app directory and create this as a seperate private repository.


## Preparing the Deployment Environment 

The simplest way to get a container running on AWS is to use Fargate, so we will use a sample Fargate deployment which takes care of everything for us.

To do that you need three AWS services working together:
- ECR (Elastic Container Registry) is a private registry for your Docker
images — think of it like a private Docker Hub, but inside your AWS account.
When Jenkins builds your image it will push it here.

- ECS (Elastic Container Service) is the service that actually runs your
containers. You tell it which image to run, how much CPU and memory to give it, and which port to expose.

- Fargate is the compute engine underneath ECS. It is serverless, meaning you do not need to manage any servers — AWS handles that for you. You just describe the container you want to run and Fargate runs it.


The relationship looks like this:


[ECR → ECS → Fargate architectural relationship](assets/fargate_container_archi.png)

## Task: Set up a container hosting environment on ECS

You will need to do five key things:

* Create an ECR repository to store your Docker images.
* Create an ECS cluster.
* Create a Task Definition describing your container.
* Create an ECS Service to keep your container running.

This will involve some research, feel free to consult your fargate resources from last week.

Cloud documentation takes some careful reading, but if you want to be a professional cloud engineer there is no way around reading documentation — so while we will steer you, you'll need to do the
research yourself too.

## Check your work

You'll know you've done this right when:

1. Is your ECR repository visible in the ECR console?
2. Is your cluster visible in the ECS console?
3. Does your service show a desired task count of 1?


The last point you won't be able to check until after the pipeline exercise — your ECR repository is currently empty, so ECS has no image to run yet. Come back to it once Jenkins has pushed an image.






[Next Challenge](02_set_up_jenkins.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=01_set_up_s3.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=01_set_up_s3.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=01_set_up_s3.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=01_set_up_s3.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=01_set_up_s3.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
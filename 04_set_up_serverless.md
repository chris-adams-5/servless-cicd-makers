# Set up the Serverless backend

## Objectives

Learn to:
- Use AWS Lambda and API Gateway to build a Serverless API backend.

## Background

 You were introduced to serverless containers last week with Fargate but this session will focus on another serverless AWS service - Lambda. 

With serverless, instead of running a whole container or virtual machine, you
just tell AWS to run one specific function when it is called. AWS handles
everything else — no servers to manage, no containers to configure.

We'll use two AWS services together:

**AWS Lambda** — runs your function in response to a trigger. You only pay for
the time your function is actually running.

**AWS API Gateway** — creates an HTTP endpoint URL that triggers your Lambda
function when called. This is how the outside world can invoke your function
over the internet.

## Task: Diagram the architecture

Before diving in, draw a diagram of how you think these two services connect.
Consider:

- What triggers the Lambda function?
- What does the Lambda function return?
- How does API Gateway sit between the caller and the function?

Keep updating this diagram as you learn more.

## Task: Set up the Serverless backend

Your task is to deploy a Lambda function and expose it via API Gateway so it
can be called over the internet.

## Key Steps

1. **Create an AWS Lambda function.**  
   Find AWS Lambda in the AWS Console. Click **Create function**, select
   **Author from scratch**, give it a name, and set the runtime to **Python 3.x**.

2. **Copy in the code from `lambdas/your-first-lambda.py`.**  
   You can find it in this repository. Copy it directly into the AWS Lambda
   code editor. You may need to scroll down to find it after creating the function.

3. **Deploy the Lambda function.**  
   Click the **Deploy** button. You will need to do this every time you make
   a change to the code.

4. **Test the Lambda function.**  
   Click the **Test** button. It will prompt you to create a test event — just
   give it a name and create it without changing anything else, since this
   function doesn't need any input parameters.

   Click **Test** again and you should see the function's output in the
   results panel below.

5. **Create an API Gateway endpoint.**  
   Go to API Gateway in the AWS Console. Select **HTTP API**, then **Lambda**
   as the integration. Select your Lambda function, set the method to **GET**
   and give it a path of your choice. Click through to create it.

6. **Try it out manually.**  
   Find the **Invoke URL** on the API Gateway screen. Open your terminal and
   call your endpoint:

   ```shell
   curl https://YOUR_API_ID.execute-api.eu-west-2.amazonaws.com/YOUR_ROUTE
   ```

   You can find the full route under **Develop → Routes** if you need a reminder.

   You should see the response message from your Lambda function.

7. **Set up CORS.**  
   Browsers block requests from one origin to another by default. CORS (Cross
   Origin Resource Sharing) is the mechanism that selectively allows this.

   Go to **Develop → CORS → Configure** and set the following:

   - **Access-Control-Allow-Origin**: `*`
   - **Access-Control-Allow-Methods**: `GET`
   - **Access-Control-Allow-Headers**: `content-type`

   Click **Save**.

## Check your work

You have done this correctly when:

- Your Lambda function runs successfully when you click **Test** and you can
  see the response in the results panel
- When you call your API Gateway endpoint with `curl` you get the response
  message back
- You can paste the full endpoint URL into your browser and see the response

Well done — you have now deployed both a containerised application with
Fargate and a serverless function with Lambda. These are two of the most
common ways to run code in the cloud, and you have used both in the same week.

[Next Challenge](05_bonus.md)

<!-- END GENERATED SECTION DO NOT EDIT -->

[Next Challenge](05_bonus.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->

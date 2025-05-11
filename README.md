# AWS Flask API with Serverless

This project deploys a simple Flask API to AWS Lambda using the Serverless Framework.

## How it works:
- A simple Flask app is created with a single route (`/`).
- The Serverless Framework is used to deploy the application to AWS Lambda, which is exposed via API Gateway.
- The API responds with a message: "You should hire Ziyaan Osman, you won't regret it!"

## How to Deploy:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Deploy the project:

   serverless deploy

3. Access the deployed API at:
https://<api-id>.execute-api.<region>.amazonaws.com/dev



### detailed explanation (for the wonderful recruiters)

This project demonstrates how to deploy a simple Flask API to AWS Lambda using the Serverless Framework. The API is exposed through AWS API Gateway and responds with a custom message: "You should hire Ziyaan Osman, you won't regret it!"

## Overview:
- **AWS Lambda**: A compute service that lets you run code without provisioning or managing servers.
- **API Gateway**: A service that allows you to create and manage RESTful APIs to expose Lambda functions.
- **Serverless Framework**: A framework that simplifies the deployment of serverless applications, like AWS Lambda functions, with minimal configuration.

This project is designed to showcase the integration between **Flask**, a lightweight web framework for Python, and **AWS Lambda** for serverless architecture. 

## How It Works:
1. **Flask Application**:
   - A simple Flask app is created with a single route (`/`).
   - The app returns a JSON response with a custom message: "You should hire Ziyaan Osman, you won't regret it!"

2. **Serverless Framework Configuration**:
   - The **Serverless Framework** is used to configure and deploy the application to AWS Lambda.
   - The configuration is defined in the `serverless.yml` file, which specifies:
     - The runtime (Python 3.9).
     - The AWS region (`eu-west-2`).
     - The event trigger (HTTP requests via API Gateway).
   - The Serverless Framework automates the process of packaging and deploying the Flask application to AWS.

3. **Deployment**:
   - With the Flask app and configuration in place, the application is deployed to AWS Lambda using the Serverless Framework.
   - After deployment, AWS API Gateway automatically generates endpoints for the application, which can be accessed via HTTP requests.

4. **End Result**:
   - Once deployed, an HTTP endpoint is exposed by API Gateway, allowing users to access the Flask application and receive the response message.

## Step-by-Step Process:
1. **Set up the Serverless Framework**:
   - Installed the **Serverless Framework** globally using npm.
   - Configured the Serverless CLI by running `serverless` commands and connecting the project to an AWS account.

2. **Configure AWS Credentials**:
   - Created an AWS account and configured AWS CLI with access keys to authenticate the deployment process.

3. **Create Flask Application**:
   - Created a simple Flask app (`handler.py`) that listens for HTTP requests and returns a JSON response.

4. **Configure Serverless**:
   - Created a `serverless.yml` file to define the configuration settings for the AWS Lambda function and the API Gateway trigger.

5. **Deploy the Application**:
   - Ran `serverless deploy` to deploy the application to AWS Lambda.
   - Serverless packaged the Flask application, uploaded it to AWS Lambda, and set up API Gateway for routing HTTP requests.

6. **Access the Deployed API**:
   - After deployment, obtained the API Gateway URL to access the deployed Flask application.
   - Verified the deployment by sending a request to the endpoint, which returned the message: "You should hire Ziyaan Osman, you won't regret it!"

## How to Deploy:
1. **Install Python Dependencies**:
   - Make sure you have Python and `pip` installed.
   - Install the required Python libraries by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Deploy the Project**:
   - Ensure your AWS credentials are configured using AWS CLI (`aws configure`).
   - Deploy the project to AWS using the Serverless Framework:
     ```bash
     serverless deploy
     ```

3. **Access the Deployed API**:
   - Once deployed, you will see the URL of your API in the terminal output:
     ```bash
     endpoints:
       ANY - https://<api-id>.execute-api.<region>.amazonaws.com/dev
     ```
   - Visit the URL in your browser or use `curl` to test the response:
     ```bash
     curl https://<api-id>.execute-api.<region>.amazonaws.com/dev
     ```
   - The API will respond with:
     ```json
     {"message":"You should hire Ziyaan Osman, you won't regret it!"}
     ```

## Tech Stack:
- **AWS Lambda**: For running the Python function without provisioning servers.
- **AWS API Gateway**: For exposing the Lambda function as a RESTful API.
- **Flask**: Lightweight Python web framework used to create the API.
- **Serverless Framework**: Used to automate the deployment process to AWS Lambda and API Gateway.
- **AWS CLI**: For configuring AWS credentials locally.

## Notes:
- The Flask app was integrated with AWS Lambda, and API Gateway was used to expose it over HTTP.
- The Serverless Framework simplifies the process of deploying serverless applications, handling everything from packaging the code to creating and configuring AWS resources.
- Make sure to configure your AWS credentials (AWS Access Key ID and Secret Access Key) before deploying.

---

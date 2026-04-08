# AWS Sentiment Analyzer

[![AWS](https://img.shields.io/badge/AWS-Cloud%20Project-232F3E?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Serverless](https://img.shields.io/badge/Serverless-Architecture-FD5750)](https://aws.amazon.com/serverless/)

AWS Sentiment Analyzer is a serverless web application that performs real-time sentiment classification through an AWS Lambda-powered REST API. The project combines a clean HTML/CSS/JavaScript frontend with a Python backend deployed behind API Gateway.

## Overview

This project demonstrates an end-to-end cloud architecture for text analysis. Users enter text in the browser, the request is sent to API Gateway, Lambda processes it with custom keyword-based NLP logic, and the result is returned as `POSITIVE`, `NEGATIVE`, or `NEUTRAL`.

## Architecture

```text
User
	|
	v
HTML Frontend
	|
	v
API Gateway
	|
	v
Lambda Function (Python)
	|
	v
Sentiment Response
```

## Tech Stack

- AWS Lambda
- AWS API Gateway
- Python
- HTML
- CSS
- JavaScript

## Features

- Serverless REST API on AWS Cloud
- Real-time sentiment analysis with `POSITIVE`, `NEGATIVE`, and `NEUTRAL` results
- Custom keyword-based NLP logic in Python
- CORS-enabled public API for browser access
- Clean, responsive web UI

## API Endpoint

`POST https://pi7aowsm33.execute-api.us-east-1.amazonaws.com/Production/analyze`

Request body:

```json
{
	"text": "I really like this project"
}
```

Example response:

```json
{
	"sentiment": "POSITIVE"
}
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/MAhsaanUllah/aws-sentiment-analyzer.git
cd aws-sentiment-analyzer
```

### 2. Open the frontend

Open `index.html` in a browser, or serve it with any static file server.

### 3. Verify the Lambda API

Make sure the API Gateway endpoint is deployed and accessible at:

```text
https://pi7aowsm33.execute-api.us-east-1.amazonaws.com/Production/analyze
```

### 4. Test the application

Enter sample text in the UI and click **Analyze Sentiment**. The app will call the AWS API and display the sentiment result on the page.

## What I Learned

- AWS Lambda function creation and deployment
- API Gateway configuration and routing
- CORS setup for web APIs
- Serverless architecture concepts
- CloudShell for API testing

## Built By

Built by a cloud-focused developer as a hands-on AWS serverless project.

## GitHub Topic Suggestions

Use these topics/tags for the repository:

- aws
- aws-lambda
- api-gateway
- serverless
- python
- javascript
- html
- css
- sentiment-analysis
- cloud-computing
- nlp
- cors

## Project Structure

```text
.
├── index.html
├── lambda_function.py
└── README.md
```

## Recruiter-Friendly Highlights

- Built a serverless AWS application using Lambda and API Gateway
- Designed a browser-based client that communicates with a public cloud API
- Implemented CORS to support cross-origin web requests
- Developed and deployed a simple NLP workflow in Python
- Practiced cloud testing and validation with AWS CloudShell

## GitHub Repository Details

- Description: Serverless AWS sentiment analyzer built with Lambda, API Gateway, Python, and a responsive web UI
- Website: https://pi7aowsm33.execute-api.us-east-1.amazonaws.com/Production/analyze
- Topics: aws aws-lambda api-gateway serverless python javascript html css sentiment-analysis cloud-computing nlp cors
- Home page: Use this README as the repository home page summary
- Releases: Not used yet
- Deployments: Not used yet
- Packages: Not used yet
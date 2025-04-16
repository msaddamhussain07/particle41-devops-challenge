# SimpleTimeService (Flask)

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.0%2B-lightgrey)
![Docker](https://img.shields.io/badge/docker-ready-blueviolet)

A lightweight RESTful microservice that returns current UTC timestamp and client IP in JSON format. Built with Flask for modern DevOps deployments.

## Features

- 🕒 Real-time UTC timestamp (ISO 8601 format)
- 🌐 Client IP detection
- 📦 Container-ready with Docker
- 🔒 Runs as non-root user in production
- 🚀 Minimal dependencies (Flask only)

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation
```
git clone https://github.com/yourusername/simple-time-service.git
cd simple-time-service/app
pip install -r requirements.txt
```
### Running the service
```
flask run --host=0.0.0.0 --port=5000
```
###Test with:
```
curl http://localhost:5000
```
API Documentation
GET /

Returns JSON with current timestamp and client IP.
Response:
{
  "timestamp": "2023-11-20T14:30:00.000Z",
  "ip": "203.0.113.45"
}

Status Codes:

    200: Success

    404: Invalid endpoint

## Docker Deployment

### Build the Image
```
docker build -t simple-time-service .
```
### Run the Container
```
docker run -d \
  -p 5000:5000 \
  -e FLASK_ENV=production \
  --name time-service \
  simple-time-service
```
### Publish to Registry
```
docker tag simple-time-service yourusername/simple-time-service:latest
docker push yourusername/simple-time-service:latest
```
### Configuration

#### Environment Variables:
Variable	Default	Description
FLASK_ENV	production	Runtime environment
PORT	5000	Service port
HOST	0.0.0.0	Binding address
### Health Check

Endpoint: GET /health
Response:
{
  "status": "healthy",
  "timestamp": "2023-11-20T14:30:00.000Z"
}

### Troubleshooting

#### Common Issues:

    1. Port already in use:
        lsof -i :5000
        kill <PID>

    2. Docker permission denied:
        sudo usermod -aG docker $USER

    3. Flask not found:
        pip install -r requirements.txt

## AWS Authentication for Terraform Deployment
### Prerequisites
  1. AWS Account with permissions to:
      create VPC, ECS, ALB, IAM resources
      Access ECR (if using private Docker images)
  2. AWS CLI installed (installation guide)
  3. Terraform installed (installation guide)

### Method 1: AWS CLI Profiles (Recommended)
1. Configure AWS Credentials:
```
aws configure
```
Enter your:
  AWS Access Key ID
  AWS Secret Access Key
  Default region (e.g., us-east-1)
  Default output format (e.g., json)
2. Verify Credentials:
 ```
 aws sts get-caller-identity
 ```
3. Deploy with Terraform:
 ```
 terraform init
 terraform plan
 terraform apply
 ```
### Method 2: Environment Variables
1. Export Credentials (for CI/CD systems):
```
export AWS_ACCESS_KEY_ID="AKIAXXXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
export AWS_REGION="us-east-1"
```
2. Deploy:
```
terraform apply
```

### Method 3: IAM Roles (for EC2/ECS)

If running Terraform from an AWS EC2 instance or ECS task:
1. Attach an IAM Role to the instance/task with permissions for:
  AmazonECS_FullAccess
  AmazonVPC_FullAccess
  (Optional) AdministratorAccess for testing
2. No explicit authentication needed—Terraform will auto-detect the role.

## Security Best Practices
### 1. Least Privilege IAM Policy (minimal example):
```
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "ecs:*",
            "ecr:*",
            "vpc:*",
            "iam:*",
            "logs:*"
          ],
          "Resource": "*"
        }
      ]
    }
```
### 2. Rotate Credentials Regularly
Avoid long-lived access keys.
### 3. Never Commit Credentials
Ensure .gitignore includes:
```
    *.tfvars
    *.tfstate*
    .env
```

## Troubleshooting
Error: No valid credential sources
Solution: Verify AWS CLI config or environment variables

Error: Access Denied
Solution: Check IAM permissions for the user/role

Error: UnauthorizedOperation
Solution: Add missing permissions to IAM policy

## Next Steps
After authentication, deploy with:
```
terraform init
terraform plan -out=tfplan
terraform apply tfplan
```
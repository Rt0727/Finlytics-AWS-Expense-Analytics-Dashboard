# Finlytics: AWS Expense Analytics Dashboard

## Overview
This repository provides an automated setup for an AWS-powered expense analytics dashboard. The project uses Terraform for Infrastructure as Code (IaC) to manage AWS resources, RDS PostgreSQL for secure and scalable data storage, and Dockerized tools for visualizing financial metrics. The dashboard enables users to track and analyze expenses in real-time with a user-friendly interface.

## Features
- **AWS Infrastructure**: Automates deployment of EC2 instances, RDS PostgreSQL, and S3 buckets using Terraform.
- **Expense Tracking Dashboard**: A web-based Flask application for real-time financial analytics.
- **Scalable Data Storage**: Secure and reliable PostgreSQL database hosted on AWS RDS.
- **S3 Integration**: Enables efficient storage and retrieval of large financial data files.
- **Monitoring and Performance Optimization**: Implements AWS CloudWatch for system health tracking and optimized SQL queries for faster analytics.
- **Automation**: Python scripts for data import, expense calculations, and dashboard updates.
- **Backup and Import Scripts**: Bash scripts for backups and data imports.

## Technologies Used
- **Cloud Provider**: AWS (EC2, RDS, S3, IAM, CloudWatch)
- **Database**: PostgreSQL
- **Web Framework**: Flask
- **Containerization**: Docker, Docker Compose
- **IaC**: Terraform
- **Automation**: Bash Scripts, Python (for data handling and calculations)

| Technology                                 | Purpose                              |
|--------------------------------------------|--------------------------------------|
| **AWS (EC2, RDS, S3, IAM, CloudWatch)**    | Cloud Provider                       |
| **PostgreSQL**                             | Database for financial data          |
| **Docker**                                 | Containerization                     |
| **Terraform**                              | Infrastructure provisioning          |
| **Bash Scripts**                           | Automation of routine tasks          |
| **Python**                                 | Core application logic for data import, expense calculations, and dashboard management |

## Prerequisites
- Install [Docker](https://www.docker.com/)
- Install [Terraform](https://www.terraform.io/)
- Install [Git](https://git-scm.com/)
- Install Python 3.x and required libraries (`psycopg2`, `boto3`)
- AWS account with necessary permissions for EC2, RDS, and S3
- Basic knowledge of Bash, Python, and SQL

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine and navigate into the directory:
```bash
git clone https://github.com/Rt0727/Finlytics-AWS-Expense-Analytics-Dashboard.git
cd Finlytics-AWS-Expense-Analytics-Dashboard
```

### 2. Configure Terraform Variables
Create a `.tfvars` file in the `terraform/` directory with the following contents:
```hcl
aws_region           = "us-east-1"
ec2_instance_type    = "t3.micro"
rds_instance_class   = "db.t3.micro"
db_name              = "expense_db"
db_username          = "admin"
db_password          = "securepassword"
s3_bucket_name       = "finlytics-expense-data"
```

### 3. Initialize and Deploy Infrastructure
Use Terraform to initialize and deploy the necessary AWS resources:
```bash
cd terraform
terraform init
terraform apply -var-file="variables.tfvars"
```
This will set up:
- EC2 instance for hosting the Flask application.
- RDS PostgreSQL database for storing financial data.
- S3 bucket for uploading and retrieving large datasets.

Terraform outputs will include the EC2 public IP and RDS endpoint.

### 4. Build and Start Docker Containers
Navigate back to the root directory and build the Docker containers:
```bash
docker-compose up --build
```
This will:
- Build the Docker image for the Flask application.
- Start the Flask app and connect it to the RDS PostgreSQL database.

### 5. Access the Expense Dashboard
To interact with the dashboard, open the EC2 public IP in your browser:
```plaintext
http://<EC2_PUBLIC_IP>:5000
```
The dashboard allows users to upload financial data, view expense reports, and track trends.

### 6. Use Python Scripts for Data Handling and Analytics

#### Import Financial Data
To import financial data from S3 into PostgreSQL, run the following Python script:
```bash
python python/data_importer.py
```
This script will fetch financial data from an S3 bucket and import it into the PostgreSQL database for analysis.

#### Calculate Expenses
To calculate and display expenses by type or date, run the following Python script:
```bash
python python/expense_calculator.py
```
This script will aggregate expenses and output them by category or date.

#### Manage Dashboard Data
To update and manage dashboard data, run:
```bash
python python/dashboard_manager.py
```
This script pulls the latest expense data from the PostgreSQL database and prepares it for display in the dashboard.

### 7. Use Backup and Data Import Scripts
Automate backups and data imports with the provided scripts:

#### Run Backup Script
```bash
./scripts/backup.sh
```
This script backs up the RDS PostgreSQL database to an S3 bucket.

#### Import Financial Data
```bash
./scripts/data_import.sh
```
This script imports financial data files into the PostgreSQL database for analysis.

## Project Structure
```plaintext
aws-expense-dashboard-setup/
│
├── terraform/
│   ├── main.tf               # Defines AWS resources (EC2, RDS, S3)
│   ├── variables.tf          # Contains variable definitions
│   └── outputs.tf            # Outputs AWS resource details
│
├── docker/
│   ├── Dockerfile            # Dockerfile for Flask app
│   └── docker-compose.yml    # Docker Compose for local testing
│
├── python/
│   ├── data_importer.py      # Imports financial data from S3 to PostgreSQL
│   ├── expense_calculator.py # Calculates expenses and aggregates data
│   ├── dashboard_manager.py  # Manages dashboard data updates
│   └── tests/                # Unit tests for Python scripts
│       ├── test_data_importer.py  # Tests for data importer
│       ├── test_expense_calculator.py  # Tests for expense calculator
│       └── test_dashboard_manager.py  # Tests for dashboard manager
│
├── scripts/
│   ├── backup.sh             # Backup script for RDS PostgreSQL
│   └── data_import.sh        # Script to import financial data
│
├── README.md                 # Documentation
└── .gitignore                # Git ignore file
```

## Troubleshooting

### Common Issues
1. **Terraform Errors**: Verify Terraform is installed and `variables.tfvars` is correctly configured.
2. **AWS Credential Issues**: Ensure that your AWS credentials are configured correctly and have permissions for EC2, RDS, and S3.
3. **Database Connection Errors**: Check the RDS endpoint and ensure security group rules allow connections from the EC2 instance.
4. **Docker Issues**: Verify Docker is running and containers are built properly.

### Logs
Access logs for debugging:
- Flask App Logs: Run `docker-compose logs app`
- PostgreSQL Logs: Run `docker-compose logs db`
- AWS CloudWatch: Check logs for EC2 instance and RDS database on AWS Console.

## Future Enhancements
- Add advanced analytics features such as expense trend predictions and anomaly detection.
- Implement role-based access control for secure multi-user operations.
- Integrate third-party APIs for automated financial data imports.
- Introduce CI/CD pipelines for continuous delivery and deployment.

```

For any questions or issues, feel free to reach out at `rt07mahifan@gmail.com`.

```
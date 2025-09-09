# aws-ec2-status-checker
This project is a Python script using Boto3 to monitor AWS EC2 instances across multiple regions. It fetches the status of each instance and categorizes them as running, stopped, or terminated. This helps in cloud monitoring and automation, reducing manual checking effort.

# AWS EC2 Instance Status Checker

## Project Overview
This project automates the monitoring of AWS EC2 instances across multiple regions.  
Using **Python** and the **Boto3 SDK**, the script connects to AWS, fetches instance details, and categorizes them as:
- Running
- Stopped
- Terminated

This automation reduces manual effort and improves efficiency in cloud monitoring.

## Skills & Technologies Used
- AWS (EC2)
- Python
- Boto3

## How to Run
1. Install requirements:
   ```bash
   pip install boto3

**Configure AWS CLI with your credentials:**
aws configure

**Run the script:**
python ec2_status_checker.py



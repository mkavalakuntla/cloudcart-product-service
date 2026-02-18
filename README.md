CloudCart – Product Service


########################################################################################

1. Project Overview

CloudCart Product Service is a foundational microservice built as part of an end-to-end DevOps evolution project.

This service will progressively evolve from:

Local Linux application

Dockerized service

CI/CD integrated

Cloud deployed (AWS)

Kubernetes managed

Fully monitored & secured production system

Current Phase: Level 1 – Local Foundation

#######################################################################################

2. Current Scope (Level 1)

At this stage, the project includes:

Structured project directory

Git version control setup

GitHub remote repository integration

Professional naming conventions

.gitignore configuration

######################################################################################

3. Project Structure
cloudcart-product-service/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── logs/
│   └── .gitkeep
│
├── scripts/
│   ├── start.sh
│   ├── stop.sh
│   └── health-check.sh
│
├── .env
├── .gitignore
└── README.md

##########################################################################################

4. Naming Convention

Repository Name:

cloudcart-product-service

#########################################################################################

Why:

Lowercase
Hyphen-separated
Service-specific naming
Scalable for microservices architecture

#########################################################################################

5. Local Setup Process (Step 1)
Create project directory
mkdir -p ~/projects
cd ~/projects
mkdir cloudcart-product-service
cd cloudcart-product-service

########################################################################################

Create base structure
mkdir app logs scripts
touch app/app.py
touch app/requirements.txt
touch logs/.gitkeep
touch scripts/start.sh
touch scripts/stop.sh
touch scripts/health-check.sh
touch README.md
touch .env
touch .gitignore

########################################################################################

Initialize Git
git init

########################################################################################

Add ignore rules

.gitignore includes:

venv/
__pycache__/
*.pyc
.env
logs/app.log

#######################################################################################

First Commit
git add .
git commit -m "Initial project structure setup"

Connect to GitHub
git remote add origin https://github.com/<username>/cloudcart-product-service.git
git branch -M main
git push -u origin main

######################################################################################

6. Why This Structure Matters

Separation of concerns
Log isolation
Script automation readiness
Environment-based configuration
Scalable for containerization & Kubernetes

######################################################################################

7. Next Phase

Level 1 – Stage 2:

Python virtual environment
Flask application skeleton
Environment variable management
Structured logging

🔹 Step 2 – Python Virtual Environment & Dependency Management
Objective

Establish an isolated Python runtime environment to ensure dependency consistency and reproducibility.

Actions Performed

Created virtual environment using:

python3 -m venv venv


Activated environment:

source venv/bin/activate


Installed dependencies:

Flask

python-dotenv

Generated dependency lock file:

pip freeze > app/requirements.txt

Outcome

Dependencies isolated from system Python

Reproducible environment across systems

Clean dependency tracking using requirements.txt

venv/ excluded via .gitignore

🔹 Step 3 – Application Skeleton with Configuration & Logging
Objective

Build a production-structured minimal Flask service.

Components Implemented
Configuration Layer (config.py)

Loads environment variables from .env

Centralizes runtime configuration

Avoids hardcoded values

Logging Layer (logger.py)

Structured logging format

Logs written to:

logs/app.log


Console + file handlers enabled

Application Layer (app.py)

Root endpoint (/)

Health endpoint (/health)

Service start logging

Binds to 0.0.0.0

Uses configurable port

Validation Performed

Application runs successfully

Health endpoint returns valid JSON

Logs generated for service start and endpoint access

Configuration loaded from .env

Commit this update:

git add README.md
git commit -m "Append documentation for Step 2 and Step 3 completion"
git push


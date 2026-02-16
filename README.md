CloudCart – Product Service


#####################################################################################################################################

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

#####################################################################################################################################

2. Current Scope (Level 1)

At this stage, the project includes:

Structured project directory

Git version control setup

GitHub remote repository integration

Professional naming conventions

.gitignore configuration

#####################################################################################################################################

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

#####################################################################################################################################

4. Naming Convention

Repository Name:

cloudcart-product-service

#####################################################################################################################################

Why:

Lowercase
Hyphen-separated
Service-specific naming
Scalable for microservices architecture

#####################################################################################################################################

5. Local Setup Process (Step 1)
Create project directory
mkdir -p ~/projects
cd ~/projects
mkdir cloudcart-product-service
cd cloudcart-product-service

#####################################################################################################################################

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

#####################################################################################################################################

Initialize Git
git init

#####################################################################################################################################

Add ignore rules

.gitignore includes:

venv/
__pycache__/
*.pyc
.env
logs/app.log

#####################################################################################################################################

First Commit
git add .
git commit -m "Initial project structure setup"

Connect to GitHub
git remote add origin https://github.com/<username>/cloudcart-product-service.git
git branch -M main
git push -u origin main

#####################################################################################################################################

6. Why This Structure Matters

Separation of concerns
Log isolation
Script automation readiness
Environment-based configuration
Scalable for containerization & Kubernetes

#####################################################################################################################################

7. Next Phase

Level 1 – Stage 2:

Python virtual environment
Flask application skeleton
Environment variable management
Structured logging

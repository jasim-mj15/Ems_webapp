# Employee Management System (Ems_webapp)

A complete **Employee Management System** built with Flask, Docker, MySQL, and Kubernetes—designed to demonstrate full-stack DevOps workflows including containerization, orchestration, CI/CD, and infrastructure automation.

---

##  Project Overview

This project serves as a real-world simulation of deploying a typical web application in a DevOps environment. It includes:

- A Flask-based web application for managing employees (CRUD operations).
- MySQL backend database with initial seeding via SQL.
- Docker for containerization.
- Docker Compose for multi-container orchestration.
- Kubernetes deployment manifests for production-ready orchestration.
- Jenkins pipeline for automating builds and deployments (CI).
- Basic unit tests for validating imports and dependencies.

---

##  Stack & Tools

| Layer     | Technologies Used                    |
|-----------|--------------------------------------|
| Backend   | Python, Flask                        |
| Database  | MySQL                                |
| Container | Docker, Docker Compose               |
| Orchestration | Kubernetes                     |
| CI/CD     | Jenkins (via Jenkinsfile)            |
| Testing   | pytest (basic import tests)          |

---

##  Repository Contents
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── init.sql # SQL script to initialize MySQL DB
├── docker-compose.yml # For local multi-container setup
├── Dockerfile # Defines the web app container image
├── jenkinsfile # Pipeline script for CI/CD
├── test_imports.py # Simple test to confirm imports work
├── mysql-deployment.yaml # Kubernetes YAML for MySQL deployment
├── k8s/ # (Optional) Additional Kubernetes manifests
└── templates/ # Flask HTML templates

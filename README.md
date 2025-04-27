# Humanchain-AI-Safety-incident
# 🛡️ AI Safety Incident Log API

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Flask-2.0.1+-green.svg" alt="Flask 2.0.1+">
  <img src="https://img.shields.io/badge/SQLAlchemy-1.4+-orange.svg" alt="SQLAlchemy 1.4+">
  <img src="https://img.shields.io/badge/REST-API-red.svg" alt="REST API">
</div>

<p align="center">
  <i>A robust and elegant solution for logging and managing AI safety incidents</i>
</p>

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [API Documentation](#-api-documentation)
- [Installation & Setup](#-installation--setup)
- [Database Configuration](#-database-configuration)
- [Running Tests](#-running-tests)
- [Design Decisions & Challenges](#-design-decisions--challenges)
- [Future Enhancements](#-future-enhancements)

## 🔍 Overview

This project implements a RESTful API service for logging and managing AI safety incidents. Built for HumanChain's mission to create a safer AI ecosystem, this service provides a reliable system to document, track, and analyze potential AI safety concerns.

The implementation prioritizes clean code architecture, RESTful design principles, and efficient data persistence while maintaining excellent error handling and input validation.

## ✨ Features

- **Complete CRUD Operations** for AI safety incidents
- **Automatic Timestamps** for accurate incident reporting
- **Input Validation** to ensure data integrity
- **Comprehensive Error Handling** with appropriate HTTP status codes
- **JSON Response Formatting** for seamless frontend integration
- **Database Persistence** with proper schema design
- **Scalable Architecture** that can evolve with future requirements

## 🔧 Tech Stack

- **Language**: Python 3.8+
- **Framework**: Flask - chosen for its lightweight nature and flexibility
- **ORM**: SQLAlchemy - provides a powerful abstraction layer for database operations
- **Database**: SQLite (development) / PostgreSQL (production-ready)
- **Testing**: Pytest with coverage reporting
- **Documentation**: OpenAPI/Swagger specification


📋 API Endpoints
1. Get All Incidents

Method: GET
Path: /incidents
Response: 200 OK with JSON array of all incidents

json[
  { "id": 1, "title": "Model Hallucination", "description": "AI generated factually incorrect information", "severity": "Medium", "reported_at": "2025-04-25T14:30:00Z" },
  { "id": 2, "title": "Data Breach", "description": "Unauthorized access to training data", "severity": "High", "reported_at": "2025-04-26T09:15:00Z" }
]
2. Create New Incident

Method: POST
Path: /incidents
Request Body:

json{
  "title": "New Incident Title",
  "description": "Detailed description here.",
  "severity": "Medium"
}

Response: 201 Created with the newly created incident

json{
  "id": 3, 
  "title": "New Incident Title", 
  "description": "Detailed description here.", 
  "severity": "Medium", 
  "reported_at": "2025-04-27T10:15:30Z"
}
3. Get Specific Incident

Method: GET
Path: /incidents/{id}
Path Parameter: id - The unique identifier of the incident
Response: 200 OK with requested incident details or 404 Not Found

json{
  "id": 1, 
  "title": "Model Hallucination", 
  "description": "AI generated factually incorrect information", 
  "severity": "Medium", 
  "reported_at": "2025-04-25T14:30:00Z"
}
4. Delete Incident

Method: DELETE
Path: /incidents/{id}
Path Parameter: id - The unique identifier of the incident
Response: 204 No Content on success or 404 Not Found

🔌 Installation & Setup
Prerequisites

Python 3.8 or higher
pip (Python package manager)

Step 1: Clone the repository
bashgit clone <repository-url>
cd ai-safety-incident-log
Step 2: Create and activate a virtual environment (recommended)
bashpython -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Step 3: Install dependencies
bashpip install -r requirements.txt
This will install all required packages:

Flask
Flask-SQLAlchemy
SQLite3 (built into Python)
Other dependencies as needed

Step 4: Database Configuration
The application uses SQLite by default, which doesn't require separate installation. The database configuration is set in app.py:
python# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
If you prefer to use environment variables for configuration (recommended for production), you can modify app.py to use:
pythonapp.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///incidents.db')
Step 5: Set up the database schema and initial data
bashpython setup_db.py
This script will:

Create the SQLite database file (incidents.db)
Create the necessary tables using SQLAlchemy models
Populate the database with 2-3 sample incidents as required

The database schema includes:

id: Integer, Primary Key, Auto-increment
title: String (100), Not Null
description: Text, Not Null
severity: String (10), Not Null, Constraint to ["Low", "Medium", "High"]
reported_at: DateTime, Not Null, Default: current timestamp

Step 6: Run the application
bashpython app.py
The API server will start running at http://localhost:5000
🧪 Testing the API with curl
Get all incidents
bashcurl -X GET http://localhost:5000/incidents
Get a specific incident
bashcurl -X GET http://localhost:5000/incidents/1
Create a new incident
bashcurl -X POST http://localhost:5000/incidents \
  -H "Content-Type: application/json" \
  -d '{"title":"API Error","description":"Unexpected response from model API","severity":"High"}'
Delete an incident
bashcurl -X DELETE http://localhost:5000/incidents/1
📂 Project Structure
ai-safety-incident-log/
├── app.py                 # Main application file with Flask configuration
├── models.py              # Database models using SQLAlchemy
├── routes.py              # API routes and endpoint handlers
├── setup_db.py            # Database setup script for schema and sample data
├── templates/             # HTML templates
│   └── index.html         # Simple web interface
├── static/                # Static files (CSS, JS)
├── requirements.txt       # Project dependencies
└── README.md              # This file
🔍 Design Decisions and Challenges
Design Decisions

Flask + SQLAlchemy: Chosen for rapid development and simplicity while maintaining good structure through ORM.
SQLite Database: Selected for ease of setup and portability. No additional configuration required for testing.
Separation of Concerns: Split code into multiple files (models, routes, app configuration) for better organization.
Auto-timestamps: Implemented automatic timestamp generation on new incidents to ensure data consistency.
Input Validation: Added validation for required fields and severity values to maintain data integrity.
HTML Interface: Created a simple web interface in addition to API endpoints for easier demonstration.

Challenges and Solutions

Validation Handling: Implemented custom validation to ensure severity is one of the allowed values while keeping the code clean.
DateTime Formatting: Ensured consistent ISO format for datetime fields in JSON responses.
Error Handling: Implemented comprehensive error handling for various error scenarios (404, 400, 500) to provide clear feedback.
Database Integration: Ensured proper integration between Flask and SQLAlchemy for efficient database operations.

🔄 Potential Improvements

Add authentication and authorization
Implement more sophisticated filtering and pagination for the GET endpoints
Add unit and integration tests
Implement logging for application events
Add update functionality (PUT/PATCH endpoints)

---

<div align="center">
  <p>Developed with ❤️ for HumanChain AI Safety</p>
  <p>© 2025 • <a href="https://github.com/yourusername">Your Name</a></p>
</div>

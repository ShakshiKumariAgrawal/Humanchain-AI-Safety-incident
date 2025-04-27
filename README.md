# 🛡️ AI Safety Incident Log API

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Flask-2.0.1+-green.svg" alt="Flask 2.0.1+">
  <img src="https://img.shields.io/badge/SQLAlchemy-1.4+-orange.svg" alt="SQLAlchemy 1.4+">
  <img src="https://img.shields.io/badge/REST-API-red.svg" alt="REST API">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
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

🌟 Live Demo
Demo Link: https://humanchain-ai-safety-incident.vercel.app/

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


📂 Project Structure

```
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
```

## 📚 API Documentation

### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/incidents` | Retrieve all incidents |
| POST | `/incidents` | Create a new incident |
| GET | `/incidents/{id}` | Retrieve a specific incident |
| DELETE | `/incidents/{id}` | Delete a specific incident |

### Detailed API Specifications

#### 1. Get All Incidents

**Request:**
```
GET /incidents
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Prompt Injection Vulnerability",
    "description": "Model exposed to potential prompt injection through unfiltered user input",
    "severity": "High",
    "reported_at": "2025-04-25T14:32:26Z"
  },
  {
    "id": 2,
    "title": "Data Hallucination",
    "description": "Model generated factually incorrect information about medical procedures",
    "severity": "Medium",
    "reported_at": "2025-04-26T09:18:43Z"
  }
]
```

**Status Codes:**
- `200 OK`: Successfully retrieved incidents

#### 2. Create New Incident

**Request:**
```
POST /incidents
Content-Type: application/json

{
  "title": "Authentication Bypass",
  "description": "AI system incorrectly authenticated user with similar voice pattern",
  "severity": "High"
}
```

**Response:**
```json
{
  "id": 3,
  "title": "Authentication Bypass",
  "description": "AI system incorrectly authenticated user with similar voice pattern",
  "severity": "High",
  "reported_at": "2025-04-27T11:42:17Z"
}
```

**Status Codes:**
- `201 Created`: Successfully created the incident
- `400 Bad Request`: Invalid input (missing fields or invalid severity)

#### 3. Get Specific Incident

**Request:**
```
GET /incidents/1
```

**Response:**
```json
{
  "id": 1,
  "title": "Prompt Injection Vulnerability",
  "description": "Model exposed to potential prompt injection through unfiltered user input",
  "severity": "High",
  "reported_at": "2025-04-25T14:32:26Z"
}
```

**Status Codes:**
- `200 OK`: Successfully retrieved the incident
- `404 Not Found`: Incident with specified ID not found

#### 4. Delete Incident

**Request:**
```
DELETE /incidents/2
```

**Response:**
```
204 No Content
```

**Status Codes:**
- `204 No Content`: Successfully deleted the incident
- `404 Not Found`: Incident with specified ID not found

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

### Step 1: Clone or download the repository
```bash
git clone https://github.com/yourusername/ai-safety-incident-log.git
cd ai-safety-incident-log
```

### Step 2: Create and activate a virtual environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set up the database
```bash
python setup_db.py
```

This script will:
1. Create the necessary database tables
2. Pre-populate the database with sample incidents
3. Display a confirmation message when complete

### Step 5: Run the application
```bash
python run.py
```

The API server will start on http://localhost:5000

## 💾 Database Configuration

The application uses SQLAlchemy to interact with the database, making it compatible with various database engines.

### Default Configuration (SQLite)

For development and testing, the application uses SQLite by default:

```python
# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///incidents.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### Using Environment Variables (Recommended for Production)

For production deployments, configure the database using environment variables:

```bash
# Set the DATABASE_URL environment variable
export DATABASE_URL="postgresql://username:password@localhost/incidents_db"
```

```python
# In config.py
import os

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
```

### Database Schema

The incident data model includes:

```
Table: incidents
--------------------------
id          | INTEGER     | PRIMARY KEY, AUTOINCREMENT
title       | VARCHAR(100)| NOT NULL
description | TEXT        | NOT NULL
severity    | VARCHAR(10) | NOT NULL, CHECK IN ('Low', 'Medium', 'High')
reported_at | TIMESTAMP   | NOT NULL, DEFAULT CURRENT_TIMESTAMP
```

## 🧪 Running Tests

The project includes a comprehensive test suite to ensure all endpoints work correctly:

```bash
pytest
```

For test coverage information:

```bash
pytest --cov=app tests/
```

## 🔍 Design Decisions & Challenges

### Architectural Decisions

1. **Flask Framework**: Selected for its lightweight nature and flexibility, allowing for rapid development without sacrificing control over the application structure.

2. **SQLAlchemy ORM**: Chosen to abstract database operations and provide a clean, Pythonic interface for data manipulation while maintaining compatibility with multiple database engines.

3. **Repository Pattern**: Implemented to separate business logic from data access, making the codebase more maintainable and testable.

4. **Input Validation**: Built robust validation to ensure data integrity, particularly for the severity field which must be one of the allowed values.

5. **ISO 8601 DateTime Format**: Standardized timestamp format to ensure consistency across all API responses.

### Challenges & Solutions

1. **Error Handling Consistency**

   *Challenge*: Implementing consistent error responses across all endpoints while keeping code DRY.
   
   *Solution*: Created custom error handler functions and utilized Flask's error handling decorators to maintain consistency.

2. **Request Validation**

   *Challenge*: Balancing thorough input validation with clean code.
   
   *Solution*: Implemented validator functions that return clear error messages for invalid inputs, making debugging easier for API consumers.

3. **Timestamp Handling**

   *Challenge*: Ensuring consistent timestamp formatting between database storage and API responses.
   
   *Solution*: Configured SQLAlchemy to handle UTC timestamps and implemented custom serialization for JSON responses.

## 🔮 Future Enhancements

With additional time, the following features could be implemented to enhance the system:

1. **Authentication & Authorization**: Implement JWT-based authentication to secure the API.

2. **Pagination**: Add support for paginated results to handle large datasets efficiently.

3. **Advanced Filtering**: Allow filtering incidents by various parameters (date range, severity, etc.).

4. **API Versioning**: Implement versioning to ensure backward compatibility as the API evolves.

5. **Audit Logging**: Track changes to incidents with a detailed audit trail.

6. **Webhooks**: Implement webhook notifications for incident creation and updates.

---

<div align="center">
  <p>Developed with ❤️ for HumanChain AI Safety</p>
  <p>© 2025 • <a href="https://github.com/yourusername">Your Name</a></p>
</div>

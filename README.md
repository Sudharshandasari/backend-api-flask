# Backend Engineering Practice Repository

## 📌 Overview

This repository contains backend engineering projects and practice systems built using Python, Flask, SQLite, JWT Authentication, and REST APIs.

The primary goal of this repository is to strengthen:

* Backend Development
* REST API Design
* Authentication & Authorization
* Database Integration
* Software Architecture
* Problem Solving
* Debugging & Testing
* Git & GitHub Workflow

---

## ⚙️ Tech Stack

* Python
* Flask
* SQLite
* JWT Authentication
* bcrypt
* Git & GitHub
* Postman
* Linux / WSL

---

## 🏗️ Repository Structure

```text
backend_app/

├── app.py
├── db/
├── middleware/
├── routes/
├── services/
├── validations/
├── utils/
├── tests/
├── README.md
└── backend_notes.md
```

---

# 🚀 Backend Systems Built

## 1. DSA Backend API

A structured backend system that exposes Data Structures & Algorithms problems as REST APIs.

### Implemented Patterns

### HashMap

* Contains Duplicate → O(n)
* Majority Element (Boyer-Moore) → O(n), O(1)

### Two Pointers

* Valid Palindrome → O(n)
* Two Sum (Sorted Array) → O(n)

### Sliding Window

* Max Sum Subarray → O(n)
* Longest Unique Substring → O(n)
* Minimum Window Substring → O(n)
* Sliding Window Maximum → O(n)

### Prefix Sum

* Prefix Sum API

### Features

* REST APIs for DSA problems
* Input Validation
* Error Handling
* Consistent JSON Responses
* Modular Architecture

---

## 2. Expense Tracker API

CRUD-based backend application built using Flask and SQLite.

### Features

* Create Expense
* Get All Expenses
* Get Expense By ID
* Update Expense
* Delete Expense

### Database

Table: expenses

Fields:

* id
* title
* amount
* category

### API Endpoints

```text
POST   /expenses
GET    /expenses
GET    /expenses/<id>
PUT    /expenses/<id>
DELETE /expenses/<id>
```

### Concepts Practiced

* SQLite Integration
* CRUD Operations
* Service Layer Architecture
* Route Layer Design
* Validation Layer
* Database Debugging

---

## 3. Task Manager API

### Features

* Create Task
* Get All Tasks
* Get Task By ID
* Update Task
* Delete Task

### Database

Table: tasks

Fields:

* id
* title
* status
* priority
* created_at

### API Endpoints

```text
POST   /tasks
GET    /tasks
GET    /tasks/<id>
PUT    /tasks/<id>
DELETE /tasks/<id>
```

### Architecture

```text
Client
↓
Route
↓
Validation
↓
Service
↓
Database
↓
Response
```

---

## 4. Authentication API

Authentication system built using Flask, JWT, bcrypt, and SQLite.

### Features

* User Registration
* User Login
* Password Hashing with bcrypt
* JWT Token Generation
* JWT Token Verification
* Authentication Middleware
* Protected Routes
* Current User Profile Endpoint

### API Endpoints

```text
POST /users
POST /login_user
GET  /profile
```

### Authentication Flow

```text
User Login
↓
bcrypt Password Verification
↓
JWT Token Generation
↓
Client Stores Token
↓
Authorization Header
↓
JWT Middleware
↓
Protected Route Access
```

### Protected Route Example

```text
GET /profile
Authorization: Bearer <JWT_TOKEN>
```

### Concepts Practiced

* Authentication
* Authorization
* JWT
* Middleware
* Password Hashing
* Protected Routes
* Request Context (g)
* Token Validation

---

# 🧠 Backend Concepts Practiced

* HTTP Fundamentals
* REST API Design
* Routing
* Request Handling
* Serialization
* Validation
* Error Handling
* CRUD Operations
* SQLite
* Authentication
* Authorization
* JWT
* Middleware
* Password Hashing
* Protected Routes
* Request Context
* Debugging
* Testing
* Git Workflow

---

# 🛠️ How To Run

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

local development Server:

```text
http://127.0.0.1:5000
```

---

# 📈 Current Progress

### Completed

✅ DSA API Project

✅ Expense Tracker API

✅ Task Manager API

✅ Authentication API

✅ JWT Authentication

✅ Middleware-Based Protected Routes

---

### Current Focus

* Backend Development with Python
* API Architecture
* Database Design
* Testing & Debugging
* Git & GitHub
* System Thinking

---

### Upcoming Focus

* PostgreSQL
* SQLAlchemy
* Pagination
* Search & Filters
* File Uploads
* Role-Based Access Control
* Docker
* Deployment

---

# 🎯 Goal

Build production-style backend systems while developing strong engineering habits in:

* Design
* Debugging
* Testing
* Documentation
* Problem Solving
* Software Architecture

---

🚀 Actively Learning, Building, Testing, and Improving.

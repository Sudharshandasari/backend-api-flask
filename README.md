# Backend Algorithm API (Flask)

## 📌 Overview

This project is a backend system built with Flask that exposes Data Structures & Algorithms (DSA) problems as APIs.

Focus:

* Strong DSA problem solving
* Clean backend architecture
* Real API development practice

---

## ⚙️ Tech Stack

* Python
* Flask
* Git & GitHub
* Postman

---

## Implemented Patterns

### 🔹 Hashmap

* Contains Duplicate
* Majority Element

### 🔹 Two Pointers

* Valid Palindrome
* Two Sum (Sorted Array)

---

## 🏗️ Project Structure

backend_app/
│
├── app.py
├── routes/
├── services/
│   ├── hashmap/
│   ├── two_pointers/
├── utils/
├── requirements.txt

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints (POST only)

### 🔹 Valid Palindrome

```
POST /twopointers/palindrome
```

Input:

```json
{ "s": "A man, a plan, a canal: Panama" }
```

Output:

```json
{ "is_palindrome": true }
```

---

### 🔹 Two Sum (Sorted)

```
POST /twopointers/twosum-sorted
```

Input:

```json
{ "numbers": [2,7,11,15], "target": 9 }
```

Output:

```json
{ "indices": [1,2] }
```

---

## Design Principles

* No business logic inside routes
* Logic handled in services layer
* Validation handled in utils
* JSON-based responses only
* Status codes:

  * 200 → Success
  * 400 → Invalid input

---

## 🎯 Goal

Build a scalable backend system with:

* 10+ DSA patterns
* Clean API structure
* Interview-ready backend skills

---

## 📌 Status

🚧 In Progress — building APIs pattern by pattern

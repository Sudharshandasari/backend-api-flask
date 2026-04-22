Backend Algorithm API (Flask)
📌 Overview

A structured backend system that exposes Data Structures & Algorithms (DSA) problems as REST APIs.

This project focuses on:

Converting DSA logic into real-world backend APIs
Building clean and scalable backend architecture
Strengthening problem-solving + backend integration skills

⚙️ Tech Stack
Python
Flask
Git & GitHub
Postman

🧠 Implemented Patterns
🔹 Hashmap
Contains Duplicate → O(n)
Majority Element (Boyer-Moore) → O(n), O(1)
🔹 Two Pointers
Valid Palindrome → O(n)
Two Sum (Sorted Array) → O(n)
🔹 Sliding Window
Max Sum Subarray (Fixed Window) → O(n)
Longest Unique Substring (Variable Window) → O(n)
⚡ Key Features
REST APIs for DSA problems
Input validation with proper error handling
Consistent JSON response structure
Clean separation of concerns:
Routes → API layer
Services → Core logic
Utils → Validation
Scalable pattern-based architecture

🏗️ Project Structure
backend_app/
│
├── app.py
├── routes/
│   ├── hashmap_routes.py
│   ├── two_pointers_routes.py
│   ├── sliding_window_routes.py
│
├── services/
│   ├── hashmap/
│   ├── two_pointers/
│   ├── sliding_window/
│
├── utils/
├── requirements.txt
📡 API Endpoints
🔹 Sliding Window
1. Max Sum Subarray

POST /sliding-window/max-sum-subarray

Request

{
  "nums": [2,1,5,1,3,2],
  "k": 3
}

Response

{
  "success": true,
  "data": 9,
  "error": null
}
2. Longest Unique Substring

POST /sliding-window/longest-unique-substring

Request

{
  "s": "abcabcbb"
}

Response

{
  "success": true,
  "data": 3,
  "error": null
}
🔹 Two Pointers
Valid Palindrome

POST /two-pointers/palindrome

Two Sum (Sorted)

POST /two-pointers/two-sum-sorted

🔹 Hashmap
Contains Duplicate

POST /hashmap/contains-duplicate

Majority Element

GET /hashmap/majority-element

🚀 How to Run
pip install -r requirements.txt
python app.py

Server runs at:

http://127.0.0.1:5000

Design Principles:

No business logic inside routes
Logic handled in services layer
Validation handled in utils
Consistent API response format
Proper HTTP status codes:
200 → Success
400 → Invalid input
500 → Server error
📈 Progress
Patterns Covered: 3+
APIs Built: 6+
Status: Actively Building 🚀
# 💰 Bank of Sasha

A simple banking system built with Python, evolving from a CLI application to a web-based API.

---

## 🚀 About the Project

This project started as a **terminal-based banking system** and evolved into a **backend API using Flask**.

It demonstrates:

* Programming fundamentals
* Business logic implementation
* API development
* Project evolution (CLI → Web)

---

## 🧠 Features

* 💵 Check balance
* ➕ Deposit money
* ➖ Withdraw money
* 🌍 Currency conversion (CLI version)
* ⚠️ Input validation and error handling

---

## 🏗️ Project Structure

```
bank-project/
│
├── server.py        # Flask API (current version)
├── legacy/
│   └── bank.py      # CLI version (first version)
├── .gitignore
└── README.md
```

---

## 🔥 Evolution

This project was built step by step:

* **v1:** CLI banking system using Python (`input`, `print`)
* **v2:** Backend API using Flask
* **v3 (coming soon):** Frontend with React

---

## ⚙️ How to Run

### 1. Install dependencies

```bash
pip install flask flask-cors
```

---

### 2. Run the server

```bash
python server.py
```

---

### 3. API will be available at:

```
http://127.0.0.1:5000
```

---

## 📡 API Endpoints

### 🔹 Get Balance

```
GET /balance
```

---

### 🔹 Deposit

```
POST /deposit
```

Body:

```json
{
  "amount": 100
}
```

---

### 🔹 Withdraw

```
POST /withdraw
```

Body:

```json
{
  "amount": 50
}
```

---

## 🧪 Technologies Used

* Python 🐍
* Flask 🌐
* Git & GitHub

---

## 🎯 Future Improvements

* Add transaction history
* Add authentication (login system)
* Connect to a real database
* Build a frontend (React)

---

## 👨‍💻 Author

Developed as a learning project to practice backend development and system design.

---

## ⭐ Final Note

This project represents my journey from **basic programming concepts** to building a **real web application**.

---

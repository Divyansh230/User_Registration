# 🧾 User Registration System (Python + Pytest)

🚀 A **robust and modular User Registration Validation System** built using Python.
This project ensures strict validation of user inputs based on predefined rules and includes **automated testing using Pytest**.

---

## 📌 Features

✅ First Name Validation (Starts with capital, min 3 chars)
✅ Last Name Validation (Same rules as first name)
✅ Email Validation (Strict regex + multiple cases covered)
✅ Phone Number Validation (Country code + 10-digit format)
✅ Password Validation (All rules enforced)
✅ Exception Handling using `ValueError`
✅ Automated Testing using **Pytest**

---

## 🏗️ Project Structure

```bash
User_Registration/
│
├── models/
│   └── user.py
│
├── utils/
│   ├── registration_utils.py
│   
│
├── services/
│   └── user_validator.py
│
├── tests/
│   └── test_user_validation.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Validation Rules

### 👤 Name Rules

* Must start with a capital letter
* Minimum 3 characters

---

### 📧 Email Rules

* Must contain `@` and domain
* No double dots
* Valid TLD (min 2 characters)
* No invalid special characters

---

### 📱 Phone Rules

* Format: `91 9876543210`
* Country code + space + 10 digits

---

### 🔐 Password Rules

* Minimum 8 characters
* At least 1 uppercase letter
* At least 1 numeric digit
* Exactly 1 special character

---

## 🧪 Testing with Pytest

This project uses **Pytest** for unit testing.

### ▶ Run Tests

```bash
pytest
```

### ✔ Example Test Cases

* Valid user
* Invalid email formats
* Invalid passwords
* Edge cases

---

## ⚙️ Installation

```bash
git clone https://github.com/Divyansh230/User_Registration.git
cd User_Registration

pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 🧑‍💻 Tech Stack

* Python 🐍
* Pytest 🧪
* Regex 🔍

---

## 🚀 Future Improvements

* REST API using FastAPI
* Database integration (MongoDB/MySQL)
* Frontend UI for user input
* Docker support

---

## 💡 Learnings

* Modular Python architecture
* Input validation using regex
* Exception handling
* Unit testing using Pytest

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 👨‍💻 Author

**Divyansh Singh**
📧 [divyanshsingh2304@gmail.com](mailto:divyanshsingh2304@gmail.com)
🔗 GitHub: https://github.com/Divyansh230

---

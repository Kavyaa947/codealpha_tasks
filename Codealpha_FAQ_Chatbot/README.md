# FAQ Chatbot Web Application

A Python-based FAQ chatbot project that matches user questions with predefined answers using simple similarity matching in a web interface.

## Project Description

This project keeps the original FAQ chatbot logic intact and wraps it in a Flask web application. Users can ask questions in a browser, and the backend sends the input to the existing FAQ matching system, which returns the most relevant answer.

## Features

- Python-based FAQ chatbot
- Predefined FAQ responses for common questions
- Text similarity matching using the original chatbot logic
- Clean and responsive web chat interface
- REST API endpoint for chatbot responses
- Help and exit command support from the core chatbot logic
- Beginner-friendly project structure

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- re
- difflib.SequenceMatcher
- typing

## Project Structure

```text
FAQ_Chatbot/
├── app.py
├── FAQ_Chatbot.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Installation

1. Open a terminal.
2. Navigate to the project folder.
3. Create and activate a virtual environment.
4. Install dependencies.

## Create and Activate a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## How to Run the Application

From the project folder, run:

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Example Questions

- What is Python?
- How to install Python?
- What is machine learning?
- What is a list in Python?
- How to learn programming?
- help
- exit

## Backend/API Explanation

The Flask backend exposes the following endpoint:

### GET /

Returns the chatbot web page.

### POST /chat

Accepts a JSON request such as:

```json
{
  "question": "What is Python?"
}
```

It sends the question to the existing FAQ chatbot logic and returns a JSON response like:

```json
{
  "answer": "✓ Python is a high-level, interpreted programming language known for its simplicity and readability."
}
```

If the question is empty or invalid, the server returns a 400 error with a descriptive JSON message.

## Future Improvements

- Add more FAQs and categories
- Improve matching with keyword scoring and NLP techniques
- Save chats to a database
- Add user authentication
- Improve UI with animations and richer chat features

## Author

CodeAlpha Internship Project

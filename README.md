```markdown
# TASK 4: Basic Chatbot

## Project Name: SmartDesk - Intelligent Rule-Based Chatbot

## Project Description

SmartDesk is a simple rule-based chatbot developed using Python.

It interacts with users through predefined responses based on
keywords in the user's input.

The chatbot can respond to greetings, basic questions, and
general queries. It also maintains conversation history and
provides basic conversation statistics.

The project demonstrates fundamental Python concepts such as
conditional statements, functions, loops, input/output, and
file handling.

## Main Objectives

- Build a simple rule-based chatbot.
- Accept text input from users.
- Identify keywords in user messages.
- Generate predefined responses.
- Maintain conversation history.
- Provide basic conversation statistics.

## Core Features

1. Greeting Recognition
2. Basic Question and Answer Responses
3. Keyword-Based Response Matching
4. Predefined Chatbot Responses
5. Conversation History Storage
6. Conversation Statistics

## Additional Features

- Streamlit Web Interface
- Previous Conversation History
- Clear Current Chat
- Export Chat History as CSV
- User Profile Display
- Command-Based CLI Interface

## Technologies Used

- Python
- Streamlit
- JSON
- CSV
- Regular Expressions

## Python Concepts Used

- if-elif-else statements
- Functions
- Loops
- User Input and Output
- Lists and Dictionaries
- File Handling
- Keyword Matching

## Project Structure

```text
codealphabasic_chatbot/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── chatbot/
│   ├── __init__.py
│   ├── engine.py
│   ├── history.py
│   └── responses.py
│
└── data/
    └── chat_history.json
```

## Installation

### Step 1: Install Python

Install Python on your system.

### Step 2: Open the Project Folder

Open the project folder in VS Code.

### Step 3: Install Required Package

Open the terminal and execute:

```bash
pip install -r requirements.txt
```

## How to Run the Project

### Method 1: Command-Line Interface

Run the following command:

```bash
python main.py
```

### Method 2: Streamlit Web Interface

Run the following command:

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

## Available Chatbot Commands

| Command | Description |
|---------|-------------|
| help | Display available commands |
| history | View previous conversations |
| stats | View conversation statistics |
| bye | End the conversation |

## Example Interaction

User: hello

SmartDesk: Hello! Welcome to SmartDesk.
How can I help you?

User: how are you

SmartDesk: I am fine and ready to assist you.

User: bye

SmartDesk: Goodbye! Thank you for chatting with SmartDesk.

## Conversation History

The chatbot stores conversation messages in a JSON file.

The saved messages include the sender, message, and timestamp.

## CSV Export

The Streamlit application provides an option to export
available chat history as a CSV file.

## Conclusion

SmartDesk demonstrates the development of a basic
rule-based chatbot using Python.

It uses predefined responses and keyword matching to
interact with users. Additional features such as conversation
history, statistics, and CSV export improve its usability
while maintaining the original objective of the Basic Chatbot task.
```
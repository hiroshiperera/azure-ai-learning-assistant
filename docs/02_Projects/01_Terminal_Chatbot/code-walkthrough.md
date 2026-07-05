# Azure OpenAI Terminal Chatbot - Code Walkthrough

## 📘 About This Document

This document explains the design and implementation of my first Azure OpenAI application. It describes the project architecture, folder structure, key source files, execution flow, and the purpose of each code component. The goal is to understand **how the application works**, rather than simply reading the source code.

---

# Project Overview

This project is a simple terminal-based AI chatbot built using Python and Azure OpenAI.

The application allows a user to type a question in the terminal, sends the question to an Azure OpenAI deployment using the official OpenAI Python SDK, and displays the AI-generated response.

This project was built to understand the complete workflow of connecting a Python application to Azure OpenAI.

---

# Technologies Used

- Microsoft Azure
- Azure OpenAI
- Azure AI Foundry
- GPT-5.4-mini
- Python 3.13
- OpenAI Python SDK
- python-dotenv
- VS Code
- Git
- GitHub

---

# Project Structure

```
azure-ai-learning-assistant/

│
├── .venv/
│
├── src/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── models.py
│   └── prompts.py
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Application Architecture

```
                User
                  │
                  ▼
              app.py
                  │
                  ▼
            ask_chatbot()
                  │
                  ▼
            chatbot.py
                  │
                  ▼
          OpenAI Python SDK
                  │
                  ▼
        Azure OpenAI Endpoint
                  │
                  ▼
         GPT-5.4-mini Deployment
                  │
                  ▼
          AI Generated Response
                  │
                  ▼
              Terminal
```

---

# Application Execution Flow

The application follows the sequence below:

1. User starts the application.
2. User enters a question.
3. `app.py` receives the input.
4. `app.py` calls `ask_chatbot()`.
5. `chatbot.py` creates a request.
6. The request is sent to Azure OpenAI.
7. GPT generates a response.
8. Python receives the response.
9. The answer is printed in the terminal.

---

# Source Code Explanation

## app.py

### Purpose

Acts as the entry point of the application.

### Responsibilities

- Start the program
- Accept user input
- Send the question to the chatbot
- Display the response

Example:

```python
question = input("You: ")
answer = ask_chatbot(question)
print(answer)
```

Why?

The entry point should remain simple and only control the application flow.

---

## chatbot.py

### Purpose

Contains all communication with Azure OpenAI.

### Responsibilities

- Create the Azure OpenAI client
- Send prompts
- Receive responses
- Return the AI answer

This file isolates all Azure-specific logic from the rest of the application.

---

### Creating the Client

```python
client = OpenAI(
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
)
```

Explanation

The client creates the connection between the Python application and Azure OpenAI.

It requires:

- Azure Endpoint
- Azure API Key

---

### Sending the Prompt

```python
response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": user_message
        }
    ]
)
```

Explanation

The application sends two messages.

System Message

Defines the behaviour of the AI.

Example

"You are a helpful AI assistant."

User Message

Contains the actual question typed by the user.

---

### Returning the Response

```python
return response.choices[0].message.content
```

Explanation

The OpenAI SDK returns a structured response.

This line extracts only the generated answer.

---

## config.py

### Purpose

Loads all configuration values.

Values loaded

- Endpoint
- API Key
- Deployment Name

Why?

Separating configuration from application logic makes the project easier to maintain and improves security.

---

## .env

### Purpose

Stores sensitive configuration.

Example

```
AZURE_OPENAI_ENDPOINT=

AZURE_OPENAI_API_KEY=

AZURE_OPENAI_DEPLOYMENT=
```

Why?

Sensitive values should never be hardcoded.

The `.env` file is excluded from Git using `.gitignore`.

---

## requirements.txt

### Purpose

Stores all project dependencies.

Example

```
openai
python-dotenv
```

Why?

Allows another developer to recreate the project by running

```bash
pip install -r requirements.txt
```

---

# Azure OpenAI Communication

The application communicates with Azure OpenAI using the following information.

Endpoint

```
https://<resource-name>.openai.azure.com/openai/v1/
```

Deployment

```
gpt-5.4-mini
```

Authentication

Azure API Key

---

# Error Encountered

## 404 Resource Not Found

Cause

Incorrect Azure endpoint.

The endpoint did not include

```
/openai/v1/
```

Solution

Updated the endpoint to

```
https://<resource>.openai.azure.com/openai/v1/
```

---

# Design Decisions

Several design decisions were made while building this application.

### Configuration Separation

Configuration values are stored separately from the application logic.

Benefits

- Easier maintenance
- Improved security
- Cleaner code

---

### Modular Design

Business logic is placed inside `chatbot.py`.

Benefits

- Easier testing
- Reusable functions
- Better organization

---

### Environment Variables

Secrets are stored inside `.env`.

Benefits

- Prevents accidental exposure
- Easy to change environments
- GitHub safe

---

# Lessons Learned

Today I learned that building a working Azure AI application involves much more than writing Python code.

Understanding Azure resources, deployments, endpoints, API keys, project structure, and secure configuration is equally important.

I also discovered that debugging configuration issues significantly improved my understanding of how Azure OpenAI works.

---

# Future Improvements

The current chatbot is intentionally simple.

Future improvements include:

- Streamlit graphical interface
- Conversation history
- Prompt engineering
- Error handling
- Logging
- Chat memory
- Azure AI Search integration
- Retrieval-Augmented Generation (RAG)

---

# Summary

This project represents my first successful Azure OpenAI application.

By completing this project, I learned:

- Azure OpenAI architecture
- Python project organization
- Azure OpenAI SDK
- Environment variables
- Secure API management
- Chat Completion API
- Azure deployment workflow

This serves as the foundation for all future Azure AI projects in this learning journey.
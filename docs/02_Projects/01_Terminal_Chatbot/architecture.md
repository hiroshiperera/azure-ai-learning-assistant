# Azure OpenAI Terminal Chatbot - Architecture

## 📘 About This Document

This document describes the architecture of my first Azure OpenAI application. It explains how the different components interact with each other, how data flows through the system, and the role of each layer in the application.

The purpose of this document is to provide a high-level understanding of the application before exploring the source code.

---

# Project Overview

The Azure OpenAI Terminal Chatbot is a simple Python application that communicates with Azure OpenAI using the official OpenAI Python SDK.

The user types a question into the terminal. The application sends the question to Azure OpenAI, receives the generated response, and displays it back to the user.

Although this is a simple application, it demonstrates the complete communication flow between a client application and Azure OpenAI.

---

# High-Level Architecture

```
                         +----------------------+
                         |       User           |
                         +----------+-----------+
                                    |
                                    | Types a question
                                    |
                                    v
                         +----------------------+
                         |       app.py         |
                         | Application Entry    |
                         +----------+-----------+
                                    |
                                    | Calls
                                    | ask_chatbot()
                                    |
                                    v
                         +----------------------+
                         |    chatbot.py        |
                         | Business Logic       |
                         +----------+-----------+
                                    |
                                    | Uses
                                    |
                                    v
                         +----------------------+
                         |   OpenAI SDK         |
                         +----------+-----------+
                                    |
                                    | HTTPS Request
                                    |
                                    v
                  +--------------------------------------+
                  | Azure OpenAI Resource                |
                  | Endpoint + API Key Authentication    |
                  +----------------+---------------------+
                                   |
                                   |
                                   v
                      +----------------------------+
                      | GPT-5.4-mini Deployment    |
                      +-------------+--------------+
                                    |
                                    | Generates Response
                                    |
                                    v
                         +----------------------+
                         |    chatbot.py        |
                         +----------+-----------+
                                    |
                                    |
                                    v
                         +----------------------+
                         |       app.py         |
                         +----------+-----------+
                                    |
                                    |
                                    v
                         +----------------------+
                         |      Terminal        |
                         +----------------------+
```

---

# Component Architecture

## User

The user interacts with the application through the command line.

Responsibilities

- Enter questions
- Read AI responses

---

## app.py

### Purpose

Acts as the application's entry point.

Responsibilities

- Starts the application
- Accepts user input
- Calls the chatbot
- Prints the AI response

This file contains very little business logic because its only responsibility is controlling the application flow.

---

## chatbot.py

### Purpose

Handles all communication with Azure OpenAI.

Responsibilities

- Create the Azure OpenAI client
- Send prompts
- Receive AI responses
- Return responses back to app.py

This keeps the Azure communication separate from the user interface.

---

## config.py

### Purpose

Centralizes configuration.

Responsibilities

- Read Endpoint
- Read API Key
- Read Deployment Name
- Load environment variables

Benefits

- Easier maintenance
- Better security
- No duplicated configuration

---

## .env

Stores sensitive information.

Contents

- Azure Endpoint
- Azure API Key
- Deployment Name

This file is ignored by Git to prevent exposing secrets publicly.

---

## Azure OpenAI

Azure OpenAI receives requests from the application.

Responsibilities

- Authenticate requests
- Route requests to the deployment
- Generate AI responses
- Return responses

---

## GPT Deployment

The deployment represents the AI model available inside Azure OpenAI.

Today's deployment

```
gpt-5.4-mini
```

The application communicates with the deployment name rather than the raw model name.

---

# Request Flow

## Step 1

User enters a question.

Example

```
What is the capital city of Sri Lanka?
```

↓

## Step 2

`app.py`

Receives the question.

↓

## Step 3

`chatbot.py`

Creates a Chat Completion request.

↓

## Step 4

OpenAI SDK

Converts the request into an HTTPS request.

↓

## Step 5

Azure OpenAI

Authenticates the request using:

- Endpoint
- API Key

↓

## Step 6

GPT-5.4-mini

Processes the prompt.

↓

## Step 7

Azure OpenAI

Returns the generated response.

↓

## Step 8

Python

Extracts

```python
response.choices[0].message.content
```

↓

## Step 9

The answer is displayed in the terminal.

---

# Folder Structure

```
azure-ai-learning-assistant/

│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── src/
│   ├── chatbot.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── models.py
│   ├── prompts.py
│   └── __init__.py
│
└── docs/
```

---

# Design Principles

## Separation of Concerns

Each file has a single responsibility.

Example

app.py

Handles application flow.

chatbot.py

Handles Azure communication.

config.py

Handles configuration.

---

## Secure Configuration

Sensitive values are stored inside

```
.env
```

instead of the source code.

Benefits

- Improved security
- Easier deployment
- Environment independence

---

## Modularity

The chatbot logic can easily be reused by:

- Streamlit
- FastAPI
- Flask
- REST APIs

without changing the business logic.

---

# Advantages of this Architecture

- Easy to understand
- Modular
- Secure
- Easy to extend
- Suitable for learning
- Ready for future improvements

---

# Current Limitations

The application currently has several limitations.

- No graphical interface
- No conversation history
- No logging
- No exception handling
- No prompt templates
- No chat memory
- No streaming responses

These limitations are intentional because the goal of Day 001 was to understand the Azure OpenAI connection.

---

# Future Architecture

The architecture will gradually evolve.

Current

```
Terminal

↓

Azure OpenAI
```

Future

```
User

↓

Streamlit UI

↓

Chat History

↓

Prompt Engineering

↓

Azure OpenAI

↓

Azure AI Search

↓

Vector Database

↓

RAG

↓

Response
```

Eventually, this project will become a production-ready AI assistant.

---

# Summary

Today's architecture demonstrates the complete lifecycle of a request sent from a Python application to Azure OpenAI.

The project follows a modular design by separating the user interface, business logic, and configuration.

This architecture serves as the foundation for all future Azure AI projects in this learning journey, including Streamlit applications, FastAPI services, Retrieval-Augmented Generation (RAG), Azure AI Search, and AI Agents.
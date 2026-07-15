# OpenAI Python SDK

## 📘 About This Document

This document explains the OpenAI Python SDK and how it is used to communicate with Azure OpenAI.

Although Azure OpenAI hosts the AI models, Python applications cannot communicate with Azure directly without using an API or Software Development Kit (SDK).

The OpenAI Python SDK provides a simple and developer-friendly interface for sending requests to Azure OpenAI and receiving AI-generated responses.

Understanding the SDK is essential because every Azure AI application relies on it to interact with Large Language Models (LLMs).

This document covers the concepts learned during the first phase of the Azure AI Learning Journey.

---

# Learning Objectives

After completing this topic, I should be able to:

- Explain what the OpenAI Python SDK is.
- Understand why an SDK is required.
- Explain what a client object is.
- Understand the purpose of the Azure Endpoint.
- Explain why an API Key is required.
- Create an OpenAI client.
- Send requests to Azure OpenAI.
- Read AI responses.
- Understand the complete communication flow.

---

# What is an SDK?

SDK stands for **Software Development Kit**.

An SDK is a collection of libraries, tools, and documentation that allows developers to interact with a service using a programming language.

Instead of writing low-level networking code, developers can use simple Python functions.

Without an SDK, developers would need to manually create HTTP requests, authenticate every request, and process JSON responses.

The SDK hides this complexity.

---

# What is the OpenAI Python SDK?

The OpenAI Python SDK is the official Python library for communicating with OpenAI models.

When used with Azure OpenAI, the SDK allows Python applications to send prompts and receive AI-generated responses.

Instead of writing REST API calls manually, developers use Python methods provided by the SDK.

Example

```python
from openai import OpenAI
```

---

# Why Do We Need the SDK?

Every interaction with Azure OpenAI is ultimately an HTTPS request.

Without the SDK, developers would need to:

- Build HTTP requests.
- Add authentication headers.
- Format JSON payloads.
- Send requests.
- Receive JSON responses.
- Parse JSON manually.
- Handle networking errors.

The SDK performs these tasks automatically.

---

# Installing the SDK

The SDK is installed using pip.

```bash
pip install openai
```

The project currently uses:

```
openai==2.44.0
```

This version is specified in `requirements.txt`.

---

# Importing the SDK

The SDK is imported using:

```python
from openai import OpenAI
```

This makes the OpenAI client available within the application.

Importing the SDK does not contact Azure OpenAI.

It simply loads the library into the Python application.

---

# What is a Client?

A client is an object that knows how to communicate with an external service.

In this project, the client knows:

- Which Azure resource to contact.
- How to authenticate.
- Where to send requests.
- How to receive responses.
- How to convert Python objects into HTTP requests.
- How to convert JSON responses back into Python objects.

The client acts as the communication bridge between the application and Azure OpenAI.

---

# Creating the Client

The client is created using:

```python
client = OpenAI(
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
)
```

This creates a reusable client object that stores all connection information.

Creating the client does **not** send a request to Azure.

No AI processing occurs.

No tokens are consumed.

No billing takes place.

The client simply prepares the application for future communication.

---

# Understanding the Endpoint

The endpoint identifies the Azure OpenAI Resource that should receive requests.

Example

```
https://aoai-ai102-learning.openai.azure.com/openai/v1/
```

The endpoint includes:

- Resource name
- Azure domain
- REST API path

Every request uses this endpoint.

Without the correct endpoint, Azure cannot identify the destination resource.

---

# Understanding the API Key

Every request must be authenticated.

Authentication is performed using the API Key.

The API Key proves that the application has permission to use the Azure OpenAI Resource.

If the API Key is invalid, Azure returns authentication errors.

API Keys should never be hardcoded into source code.

Instead, they should be stored securely using environment variables.

---

# Environment Variables

Sensitive configuration values are stored inside a `.env` file.

Example

```
AZURE_OPENAI_ENDPOINT

AZURE_OPENAI_API_KEY

AZURE_OPENAI_DEPLOYMENT
```

Advantages include:

- Better security
- Easier deployment
- Cleaner source code
- Prevents accidental exposure through GitHub

---

# Sending a Chat Completion Request

The application sends prompts using the Chat Completions API.

Example

```python
response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=messages
)
```

This method sends the complete conversation to Azure OpenAI.

---

# Understanding the Parameters

## model

```python
model=AZURE_OPENAI_DEPLOYMENT
```

The `model` parameter specifies the deployment name.

Although the parameter is named `model`, Azure expects the deployment name.

---

## messages

```python
messages=messages
```

The `messages` parameter contains the conversation.

Every request sends the complete conversation history.

---

# Messages Structure

Each message is represented as a Python dictionary.

Example

```python
{
    "role": "system",
    "content": "You are a helpful AI assistant."
}
```

Supported roles include:

- system
- user
- assistant

The conversation is simply a list of these dictionaries.

---

# Understanding the Response

The SDK returns a Python object.

Example

```python
response = client.chat.completions.create(...)
```

This object contains:

- AI response
- Metadata
- Token usage
- Finish reason

The generated response is accessed using:

```python
response.choices[0].message.content
```

This extracts the assistant's reply as plain text.

---

# Communication Flow

The communication process follows this architecture.

```
User
  │
  ▼
Python Application
  │
  ▼
OpenAI Python SDK
  │
  ▼
HTTPS Request
  │
  ▼
Azure OpenAI Endpoint
  │
  ▼
Azure OpenAI Resource
  │
  ▼
Deployment
  │
  ▼
GPT-5.4-mini
  │
  ▼
Generated Response
  │
  ▼
OpenAI Python SDK
  │
  ▼
Python Application
  │
  ▼
User
```

The SDK handles all networking and communication.

---

# What Happens Behind the Scenes?

When the application executes:

```python
client.chat.completions.create(...)
```

the SDK performs several steps automatically:

1. Creates an HTTPS request.
2. Adds authentication headers.
3. Converts Python objects into JSON.
4. Sends the request to Azure OpenAI.
5. Waits for the response.
6. Parses the JSON response.
7. Converts the response into Python objects.
8. Returns the response to the application.

The developer does not need to implement any of these steps manually.

---

# Common Errors

## 404 Resource Not Found

Cause:

Incorrect endpoint.

---

## 401 Unauthorized

Cause:

Invalid API Key.

---

## Deployment Not Found

Cause:

Incorrect deployment name.

---

## Network Errors

Cause:

Internet connectivity or service availability issues.

---

# Best Practices

- Create the client once and reuse it.
- Store secrets in environment variables.
- Separate configuration from application logic.
- Handle exceptions gracefully.
- Use reusable functions such as `ask_chatbot()`.
- Keep the SDK code separate from the user interface.

---

# Key Concepts Learned

During this learning journey, I learned that:

- The SDK simplifies communication with Azure OpenAI.
- The client object stores connection information.
- Creating a client does not consume tokens.
- Chat requests are sent using `chat.completions.create()`.
- The SDK automatically handles HTTP communication.
- Responses are returned as Python objects.
- Conversation history is sent through the `messages` list.
- The SDK hides networking complexity from the developer.

---

# Summary

The OpenAI Python SDK provides a simple and efficient way for Python applications to communicate with Azure OpenAI.

Rather than manually creating HTTP requests, the SDK handles authentication, request formatting, network communication, and response parsing.

The client object acts as the bridge between the application and Azure OpenAI, while the Chat Completions API allows developers to send conversations and receive AI-generated responses.

Understanding the OpenAI Python SDK is fundamental for building chatbots, AI assistants, Retrieval-Augmented Generation (RAG) systems, AI agents, and other intelligent applications throughout the Azure AI Learning Journey.
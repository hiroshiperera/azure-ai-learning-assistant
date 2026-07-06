# Understanding the Azure OpenAI Python SDK

## 📘 About This Document

This document explains how a Python application communicates with Azure OpenAI using the official OpenAI Python SDK. Rather than simply learning how to write the code, this guide focuses on understanding what happens behind the scenes when a request is sent from Python to Azure OpenAI.

By the end of this document, I should understand the role of the OpenAI SDK, the purpose of the client object, how authentication works, how Azure identifies the correct resource, and how the application establishes communication before sending prompts.

This knowledge forms the foundation for all future Azure AI applications.

---

# Learning Objectives

After completing this topic, I should be able to:

- Explain the purpose of the OpenAI Python SDK.
- Understand why the SDK is required.
- Explain what a client object is.
- Understand the purpose of the Azure Endpoint.
- Explain why an API Key is required.
- Describe how the Python application communicates with Azure OpenAI.
- Explain why creating the client does not consume AI tokens.

---

# What is the OpenAI Python SDK?

The OpenAI Python SDK is an official Python library that allows developers to communicate with OpenAI models using simple Python code.

Instead of manually creating HTTP requests, handling authentication, formatting JSON payloads, and parsing responses, the SDK provides easy-to-use Python methods that perform these tasks automatically.

Without the SDK, developers would need to write significantly more code to communicate with Azure OpenAI.

The SDK simplifies the development process while hiding the complexity of network communication.

---

# Why Do We Need the SDK?

Every interaction with Azure OpenAI is ultimately an HTTPS request.

Without the SDK, a developer would need to:

- Create HTTP requests manually.
- Add authentication headers.
- Construct JSON request bodies.
- Send requests.
- Receive JSON responses.
- Parse the returned JSON.
- Handle network errors.

The SDK performs all these tasks automatically, allowing developers to focus on building AI applications rather than implementing networking logic.

---

# Communication Overview

The communication process follows the architecture below.

```

User

↓

Python Application

↓

OpenAI Python SDK

↓

HTTPS Request

↓

Azure OpenAI Service

↓

GPT Deployment

↓

Generated Response

↓

Python Application

↓

User

```

The OpenAI SDK acts as the communication layer between the Python application and Azure OpenAI.

---

# Importing the SDK

The SDK is imported using:

```python
from openai import OpenAI
```

This statement makes the OpenAI client available within the application.

The SDK itself does not communicate with Azure.

It only provides the tools required to establish communication.

---

# Creating the Client

The first important step is creating an OpenAI client.

```python
client = OpenAI(
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
)
```

This line creates a client object.

The client is responsible for communicating with Azure OpenAI.

It stores all connection information that will be used later whenever the application sends requests.

Creating the client **does not** contact Azure.

No AI processing occurs at this stage.

No tokens are consumed.

No API request is sent.

The client simply prepares the application for future communication.

---

# What is a Client?

A client is an object that knows how to communicate with an external service.

In this project, the client knows:

- Which Azure resource to contact.
- How to authenticate.
- How to send requests.
- How to receive responses.
- How to convert Python objects into HTTP requests.
- How to convert HTTP responses back into Python objects.

Think of the client as a messenger between the Python application and Azure OpenAI.

---

# Understanding the Endpoint

The endpoint identifies the Azure OpenAI resource that should receive the request.

Example

```
https://aoai-ai102-learning.openai.azure.com/openai/v1/
```

The endpoint contains several important pieces of information.

Resource Name

```
aoai-ai102-learning
```

Azure Domain

```
openai.azure.com
```

REST API Version

```
/openai/v1/
```

Every request sent from the SDK uses this endpoint.

Without a valid endpoint, Azure cannot determine which resource should process the request.

---

# Why is the API Key Required?

Every Azure OpenAI request must be authenticated.

Authentication proves that the caller has permission to use the Azure resource.

The API Key acts like a secure password.

During every request, Azure verifies the key before processing the prompt.

If the API Key is incorrect, Azure rejects the request.

Typical authentication errors include:

- 401 Unauthorized
- 403 Forbidden

For security reasons, API Keys should never be hardcoded into source code.

Instead, they should be stored inside a `.env` file.

---

# Why Doesn't the Client Contain the Model?

Notice that the client only requires:

- Endpoint
- API Key

It does **not** require the model or deployment name.

The reason is simple.

The client's responsibility is only to establish communication.

The model is selected later when a Chat Completion request is created.

This separation makes the client reusable across different deployments.

---

# Responsibilities of the Client

The client performs several important tasks.

It:

- Stores connection details.
- Authenticates requests.
- Creates HTTP requests.
- Sends requests securely.
- Receives responses.
- Converts JSON into Python objects.
- Handles network communication.

The client does **not** generate AI responses.

The AI model performs that task.

---

# What Happens When the Client is Created?

When Python executes:

```python
client = OpenAI(
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
)
```

the following events occur:

1. The OpenAI client object is created.
2. The endpoint is stored.
3. The API Key is stored.
4. The client becomes ready for communication.

Nothing is sent to Azure.

No tokens are consumed.

No billing occurs.

No GPT model is executed.

Actual communication begins only when a request is sent.

---

# What Happens Next?

The client becomes active only when the application executes:

```python
client.chat.completions.create(...)
```

At this point:

- A request is created.
- Authentication is applied.
- The HTTPS request is sent.
- Azure processes the prompt.
- GPT generates a response.
- The response returns to Python.

This is the moment where Azure billing begins because AI processing occurs.

---

# Key Takeaways

- The OpenAI SDK is a communication library.
- The SDK hides networking complexity.
- The client object manages communication with Azure OpenAI.
- Creating a client does not contact Azure.
- No tokens are consumed when creating the client.
- The endpoint identifies the Azure resource.
- The API Key authenticates every request.
- The deployment is selected only when creating a Chat Completion request.

---

# Summary

Understanding the OpenAI Python SDK is essential before building larger AI applications.

The SDK provides a simple interface for communicating with Azure OpenAI while hiding the complexity of HTTP communication.

The client object acts as the bridge between the Python application and Azure OpenAI. It stores connection details, manages authentication, and prepares the application for communication. Actual AI processing only begins when the application sends a Chat Completion request.

This knowledge provides the foundation for understanding prompts, conversation history, streaming responses, Azure AI Search integration, Retrieval-Augmented Generation (RAG), and AI Agents in future lessons.
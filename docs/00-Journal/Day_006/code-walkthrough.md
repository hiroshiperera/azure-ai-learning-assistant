# Code Walkthrough - Day 006
# Introducing Prompt Management

## 📘 About This Document

This document explains the changes made to the Azure AI Learning Assistant during Day 006.

The primary objective was to introduce Prompt Engineering while improving the application's architecture.

Rather than storing the System Prompt directly inside the chatbot or user interface, prompts are now managed in a dedicated module.

---

# Objective

Refactor the application so that:

- Prompt definitions are separated from chatbot logic.
- The chatbot becomes independent of specific prompts.
- Prompt management becomes reusable and maintainable.

---

# Previous Design

Previously the System Prompt was written directly inside the application.

```python
{
    "role": "system",
    "content": "You are a helpful AI assistant."
}
```

Although functional, this approach makes it difficult to reuse prompts across different AI applications.

---

# New Design

A new module was introduced.

```
src/
    prompts.py
```

This module stores reusable prompt templates.

Example:

```python
SYSTEM_PROMPT = """
You are an Azure AI tutor helping students prepare for the Microsoft AI-102 certification.

Explain concepts clearly.
Use simple language.
Provide practical examples.
"""
```

---

# Updating Streamlit

Instead of hardcoding the prompt:

```python
{
    "role":"system",
    "content":"You are a helpful AI assistant."
}
```

the application now imports:

```python
from src.prompts import SYSTEM_PROMPT
```

and uses:

```python
{
    "role":"system",
    "content":SYSTEM_PROMPT
}
```

---

# Why This Change?

Prompt definitions are configuration.

They are not business logic.

Moving prompts into a separate module improves maintainability and encourages reuse.

---

# Benefits

The application can now support multiple AI personalities.

For example:

- AI-102 Tutor
- Travel Assistant
- Math Teacher
- Coding Assistant

Only the prompt changes.

No chatbot code needs to be modified.

---

# Architecture

```
User

↓

Streamlit

↓

SYSTEM_PROMPT

↓

chatbot.py

↓

Azure OpenAI

↓

Response
```

---

# Software Engineering Principles

Today's refactoring applied:

- Separation of Concerns
- Configuration Management
- Reusability
- Maintainability

---

# Lessons Learned

I learned that prompts should be treated as configurable resources rather than hardcoded strings.

Separating prompts from application logic makes the application easier to extend and maintain.

---

# Summary

Today's refactoring introduced dedicated prompt management through `prompts.py`.

The chatbot now focuses only on communicating with Azure OpenAI, while prompt definitions are managed independently.

This architecture prepares the application for Prompt Templates, AI Agents, and Retrieval-Augmented Generation in future lessons.
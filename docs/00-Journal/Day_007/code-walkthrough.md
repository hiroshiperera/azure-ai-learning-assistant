# Code Walkthrough - Day 007
# Configuring Azure OpenAI Model Parameters

## About This Document

This document explains the code changes introduced during Day 007.

The primary objective was to configure Azure OpenAI model parameters and understand how they influence response generation.

---

# Objective

Enhance the chatbot by explicitly configuring model parameters rather than relying on default settings.

---

# Previous Implementation

Previously, the chatbot simply called Azure OpenAI using:

```python
response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=messages,
)
```

The model used its default behaviour.

---

# Updated Implementation

The API call was modified to include model parameters.

```python
response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=messages,
    temperature=0.2,
    max_completion_tokens=300
)
```

---

# Temperature

Temperature was introduced to make responses more deterministic.

A value of:

```python
temperature = 0.2
```

was selected because the chatbot is designed as an AI-102 learning assistant.

---

# Max Completion Tokens

The chatbot now limits responses using:

```python
max_completion_tokens = 300
```

This provides reasonably detailed answers while avoiding unnecessarily long responses.

---

# API Compatibility

While implementing this feature, the application initially used:

```python
max_tokens
```

The Azure OpenAI API returned an error indicating that the deployed GPT-5 model requires:

```python
max_completion_tokens
```

The code was updated accordingly.

---

# Software Engineering Observation

Today's implementation demonstrated the importance of:

- Reading API documentation.
- Understanding model compatibility.
- Responding appropriately to runtime errors.

---

# Architecture

```
User

↓

Streamlit

↓

Session State

↓

chatbot.py

↓

Azure OpenAI

↓

Temperature

↓

Max Completion Tokens

↓

Response
```

---

# Lessons Learned

Today's work showed that model parameters are an important part of application behaviour.

Rather than modifying the AI model itself, developers configure response characteristics using parameter values.

---

# Summary

The chatbot now explicitly configures Azure OpenAI model parameters.

These settings improve response consistency and prepare the application for future enhancements such as configurable AI behaviour and user-adjustable settings.
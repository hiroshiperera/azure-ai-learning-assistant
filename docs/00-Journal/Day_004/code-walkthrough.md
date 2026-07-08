# Code Walkthrough - Day 004
# Building a ChatGPT-style Azure OpenAI Web Application using Streamlit

## 📘 About This Document

This document explains the implementation changes made on Day 004 of the Azure AI Learning Journey.

During previous lessons, the application evolved from a terminal chatbot into a basic Streamlit web application capable of communicating with Azure OpenAI.

However, the application still had several limitations:

- Messages disappeared after every interaction.
- The interface did not resemble a modern chat application.
- The application did not preserve chat history.
- Streamlit's execution model was not fully understood.

The objective of today's implementation was to transform the application into a conversational AI interface while understanding the concepts behind Streamlit state management.

---

# Objectives

Today's implementation focused on:

- Learning Streamlit chat components.
- Understanding Streamlit reruns.
- Introducing Session State.
- Preserving chat history.
- Connecting Streamlit with the existing Azure OpenAI chatbot.
- Improving software architecture.

---

# Previous Application

The previous implementation looked similar to the following.

```python
import streamlit as st
from src.chatbot import ask_chatbot

st.title("🤖 Azure AI Learning Assistant")

user_input = st.text_input("Ask me anything")

if st.button("Send"):

    answer = ask_chatbot(user_input)

    st.write(answer)
```

Although this application worked correctly, it behaved more like a question-and-answer system than a conversational chatbot.

Each new question replaced the previous conversation.

---

# Problem 1

## Traditional Text Input

Originally, the application used

```python
st.text_input()
```

together with

```python
st.button()
```

This required users to:

1. Type a question.
2. Click the Send button.

Although functional, this did not provide a natural conversational experience.

---

# Solution

The application was updated to use Streamlit's dedicated chat component.

```python
user_input = st.chat_input("Ask me anything...")
```

Advantages include:

- Automatically submits when Enter is pressed.
- Modern chat interface.
- Better user experience.
- Specifically designed for AI chat applications.

---

# Problem 2

## Responses Were Displayed as Plain Text

Previously, AI responses were displayed using

```python
st.write(answer)
```

Example

```
Azure OpenAI is...
```

Although correct, the output did not visually distinguish user messages from assistant messages.

---

# Solution

The application now uses

```python
with st.chat_message("assistant"):
    st.write(answer)
```

Likewise, user messages are displayed using

```python
with st.chat_message("user"):
    st.write(user_input)
```

This automatically renders professional chat bubbles similar to ChatGPT.

---

# Problem 3

## Chat History Disappeared

Every time the user submitted a question, Streamlit reran the entire script.

As a result:

- Previous variables were recreated.
- Previous messages disappeared.
- Only the latest interaction remained visible.

Example

```
User:
Hello

Assistant:
Hi!
```

Next question

```
User:
What is Azure?

Assistant:
Azure is...
```

The original conversation was lost.

---

# Understanding the Cause

Unlike traditional desktop applications, Streamlit reruns the Python script after every user interaction.

```
User Interaction

↓

Streamlit

↓

Run Entire Script Again

↓

Update Interface
```

Because normal Python variables exist only during a single execution, they disappear during each rerun.

---

# Solution

## Introducing Session State

To preserve information between reruns, Streamlit Session State was introduced.

The conversation history is created only once.

```python
if "messages" not in st.session_state:

    st.session_state.messages = []
```

This creates a persistent list that survives future reruns.

---

# Storing User Messages

Whenever a user submits a prompt, it is stored.

```python
st.session_state.messages.append(
    {
        "role":"user",
        "content":user_input
    }
)
```

Rather than displaying the message immediately, it becomes part of the application's conversation history.

---

# Connecting Azure OpenAI

The application already contained a working chatbot module.

Instead of creating new Azure code, the existing implementation was reused.

```python
response = ask_chatbot(user_input)
```

This demonstrates the benefit of separating business logic from the user interface.

---

# Storing Assistant Responses

After Azure OpenAI generated a response, it was also stored.

```python
st.session_state.messages.append(
    {
        "role":"assistant",
        "content":response
    }
)
```

The conversation history now contains both participants.

Example

```python
[
    {
        "role":"user",
        "content":"Hello"
    },
    {
        "role":"assistant",
        "content":"Hi!"
    }
]
```

---

# Rebuilding the Conversation

Instead of displaying only the latest message, the application redraws the entire conversation.

```python
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])
```

Every time Streamlit reruns, every stored message is displayed again.

Although the script restarts, the conversation appears continuous.

---

# Chat Flow

The application's execution flow is now:

```
User

↓

st.chat_input()

↓

Store User Message

↓

ask_chatbot()

↓

Azure OpenAI

↓

Assistant Response

↓

Store Assistant Message

↓

Session State

↓

Rerun

↓

Display Entire Conversation
```

---

# Session State Experiment

Before integrating Azure OpenAI, a separate experiment was created.

Instead of calling Azure OpenAI, a simple Echo response was generated.

```python
response = f"Echo: {user_input}"
```

This allowed Session State behaviour to be understood independently of Azure services.

---

# Counter Experiment

A second experiment was created to understand Session State.

The application stored

```python
st.session_state.count
```

instead of

```python
count
```

This demonstrated that Session State survives Streamlit reruns while normal Python variables do not.

This experiment provided the conceptual foundation required for implementing chat history.

---

# Software Architecture

The application architecture now consists of multiple layers.

```
                User
                  │
                  ▼
        Streamlit Interface
                  │
                  ▼
        Streamlit Session State
                  │
                  ▼
           chatbot.py
                  │
                  ▼
        OpenAI Python SDK
                  │
                  ▼
       Azure OpenAI Service
                  │
                  ▼
          GPT-5.4-mini
```

Each layer has a single responsibility.

---

# Design Observation

During implementation, an architectural issue was identified.

Conversation history currently exists in two locations.

```
Streamlit

↓

st.session_state.messages
```

and

```
chatbot.py

↓

messages
```

This duplicates the same information.

A future refactoring will allow Streamlit to own the conversation history while chatbot.py becomes responsible only for communicating with Azure OpenAI.

This will simplify the architecture and better follow the Single Responsibility Principle.

---

# Lessons Learned

Today's implementation introduced several important concepts.

I learned:

- How Streamlit reruns an application.
- Why normal variables disappear.
- Why Session State is required.
- How chat history is preserved.
- How `st.chat_input()` differs from `st.text_input()`.
- How `st.chat_message()` creates professional chat interfaces.
- How business logic can be reused across different user interfaces.
- Why good software architecture separates responsibilities.

---

# Summary

Today's implementation transformed the Azure AI Learning Assistant from a simple question-and-answer application into a conversational AI application.

The most significant improvement was introducing Session State to preserve conversation history across Streamlit reruns.

Additional improvements included replacing traditional input controls with Streamlit chat components, reusing the existing Azure OpenAI chatbot, and recognising future opportunities to improve the software architecture.

This implementation forms the foundation for future enhancements such as streaming responses, persistent chat history, Retrieval-Augmented Generation (RAG), FastAPI integration, and AI Agents.
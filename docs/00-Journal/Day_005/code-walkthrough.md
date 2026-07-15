# Code Walkthrough - Day 005
# Refactoring the Streamlit Chatbot using Session State

## 📘 About This Document

This document explains the architectural refactoring performed on the Azure AI Learning Assistant during Day 005.

In previous lessons, the chatbot maintained its own conversation history inside `chatbot.py`. Although the application worked correctly, the design violated an important software engineering principle because two different components were responsible for managing conversation state.

Today's objective was to redesign the application by making **Streamlit** the single owner of the conversation history while reducing the responsibility of `chatbot.py` to communicating with Azure OpenAI only.

No new functionality was added. Instead, the application was refactored to produce a cleaner, more maintainable architecture.

---

# Objective

Refactor the application to:

- Remove conversation management from `chatbot.py`
- Store conversation history only inside Streamlit Session State
- Make `chatbot.py` responsible only for Azure OpenAI communication
- Improve the application's architecture using the Single Responsibility Principle (SRP)

---

# Previous Architecture

Before refactoring, the application architecture looked like this.

```
                User
                  │
                  ▼
            Streamlit UI
                  │
                  ▼
          ask_chatbot(user_input)
                  │
                  ▼
            chatbot.py
                  │
        Conversation History
          (messages list)
                  │
                  ▼
        Azure OpenAI Service
                  │
                  ▼
            AI Response
                  │
                  ▼
             Streamlit UI
```

The conversation history was maintained inside `chatbot.py`.

---

# Problems with the Previous Design

Although the chatbot worked correctly, the design introduced several problems.

- `chatbot.py` owned the conversation.
- Streamlit displayed the conversation.
- The UI could not directly manage or modify conversation history.
- Future features such as Clear Chat, Multiple Conversations, Chat Export, and Persistent Memory would become difficult to implement.

Most importantly, two different components were responsible for the same data.

This violated the principle of having a **Single Source of Truth**.

---

# Understanding the Single Source of Truth

In software engineering, important data should have only one owner.

Instead of storing conversation history in multiple locations, a single component should be responsible for creating, updating, and managing that data.

For this application, Streamlit Session State is the most appropriate owner because it manages the user interface.

---

# New Architecture

After refactoring, the architecture became:

```
                User
                  │
                  ▼
            Streamlit UI
                  │
                  ▼
        st.session_state.messages
                  │
                  ▼
        ask_chatbot(messages)
                  │
                  ▼
            chatbot.py
                  │
                  ▼
        Azure OpenAI Service
                  │
                  ▼
            AI Response
                  │
                  ▼
        st.session_state.messages
                  │
                  ▼
            Streamlit UI
```

The entire conversation is now managed by Streamlit.

---

# Step 1 – Initialize Session State

Previously, Session State was initialized with an empty list.

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

After refactoring:

```python
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]
```

The system prompt now becomes part of the conversation managed by Streamlit.

---

# Why Move the System Message?

Previously, the system prompt was created inside `chatbot.py`.

Since Streamlit now owns the conversation, it is also responsible for creating the first message.

This ensures the complete conversation exists in one location.

---

# Step 2 – Hide the System Prompt

The system prompt is intended only for the AI model.

It should not be displayed to users.

Instead of displaying every message:

```python
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])
```

The application now ignores the system message.

```python
for message in st.session_state.messages:

    if message["role"] != "system":

        with st.chat_message(message["role"]):
            st.write(message["content"])
```

Only User and Assistant messages appear in the interface.

---

# Step 3 – Save User Messages

When the user enters text, Streamlit stores the message.

```python
st.session_state.messages.append(
    {
        "role": "user",
        "content": user_input
    }
)
```

The conversation history now grows inside Session State.

---

# Step 4 – Send the Entire Conversation

Previously:

```python
response = ask_chatbot(user_input)
```

Only the latest user message was sent.

After refactoring:

```python
response = ask_chatbot(st.session_state.messages)
```

The chatbot now receives the entire conversation.

This allows Azure OpenAI to generate responses using previous context.

---

# Step 5 – Simplify chatbot.py

The responsibility of `chatbot.py` changed significantly.

Previously it:

- Created conversation history
- Added user messages
- Added assistant messages
- Called Azure OpenAI

After refactoring, it performs only one task.

```python
def ask_chatbot(messages: list[dict]) -> str:

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=messages
    )

    return response.choices[0].message.content
```

The chatbot module no longer stores any state.

It simply receives a conversation and returns a response.

---

# Responsibilities After Refactoring

## Streamlit

Responsible for:

- User Interface
- Session State
- Conversation History
- Displaying Messages
- Receiving User Input

---

## chatbot.py

Responsible for:

- Communicating with Azure OpenAI
- Sending requests
- Receiving responses

No conversation management occurs inside this module.

---

# Software Engineering Concepts Learned

## Single Responsibility Principle (SRP)

Every component should have one responsibility.

### Streamlit

Responsible for the application's user interface.

### chatbot.py

Responsible for Azure OpenAI communication.

---

## Separation of Concerns

The UI layer and AI communication layer are now separated.

This makes the application easier to maintain and extend.

---

## Single Source of Truth

Conversation history exists only inside:

```
st.session_state.messages
```

No duplicate copies are maintained elsewhere.

---

## Refactoring

Refactoring means improving the internal structure of software without changing its external behaviour.

Today's work did not add any new features.

Instead, it produced a cleaner architecture that will support future enhancements.

---

# Architecture Comparison

## Before

```
Streamlit

↓

User Input

↓

chatbot.py

↓

Conversation History

↓

Azure OpenAI
```

---

## After

```
Streamlit

↓

Session State

↓

Complete Conversation

↓

chatbot.py

↓

Azure OpenAI
```

The conversation now belongs entirely to Streamlit.

---

# Debugging Experience

During the refactoring process, an Azure OpenAI error appeared.

```
Missing required parameter:
messages[17].content[0].type
```

To identify the problem, several debugging techniques were used.

- Created a minimal standalone Python script.
- Verified Azure OpenAI independently of Streamlit.
- Confirmed the Azure endpoint and SDK were working correctly.
- Isolated the issue to the application rather than the Azure service.
- Restarted the Streamlit application to clear stale session state.

This demonstrated the importance of isolating problems before assuming cloud services are at fault.

---

# Lessons Learned

Today I learned that software development is not only about adding new features.

Professional developers frequently improve existing code through refactoring.

I also learned that:

- Session State is the appropriate place to manage conversation history.
- Azure OpenAI should remain independent from the user interface.
- Clean architecture makes future features much easier to implement.
- Debugging should begin by isolating the smallest possible working example.

---

# Summary

Today's work significantly improved the internal architecture of the Azure AI Learning Assistant.

Key improvements include:

- Refactored the chatbot architecture.
- Introduced a Single Source of Truth.
- Moved conversation history into Streamlit Session State.
- Simplified `chatbot.py`.
- Applied the Single Responsibility Principle.
- Applied Separation of Concerns.
- Learned professional debugging techniques.
- Prepared the application for future features such as chat history persistence, RAG, Azure AI Search, file upload, and AI Agents.

This refactoring forms an important architectural milestone in the Azure AI Learning Journey.
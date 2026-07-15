# Understanding Streamlit State Management and Building an AI Chat Application

## 📘 About This Document

This document explains the concepts learned while transforming a basic Streamlit application into an interactive AI chat application.

Unlike previous lessons that focused on Azure OpenAI and the Python SDK, today's lesson focused on understanding how Streamlit manages application state and how chat applications preserve conversation history.

During this lesson, I learned how Streamlit reruns Python scripts, why normal variables lose their values, and how `st.session_state` allows applications to remember information between user interactions.

These concepts form the foundation for building professional AI chat applications using Streamlit.

---

# Learning Objectives

After completing this lesson, I should be able to:

- Explain why Streamlit reruns an entire script.
- Understand the difference between normal variables and Session State.
- Explain how `st.session_state` works.
- Build a simple Streamlit application using chat components.
- Explain the purpose of `st.chat_input()`.
- Explain the purpose of `st.chat_message()`.
- Understand how conversation history is stored in Streamlit.
- Explain the separation between the UI layer and business logic.

---

# The Problem

The previous Streamlit application could communicate with Azure OpenAI.

However, every new question replaced the previous response.

Example

```
User:
Hello

AI:
Hello!
```

Next question

```
User:
What is Azure OpenAI?

AI:
Azure OpenAI is...
```

The previous conversation disappeared.

The application was unable to remember previous interactions.

---

# Why Does This Happen?

One of the most important characteristics of Streamlit is its execution model.

Whenever a user interacts with the application, Streamlit reruns the entire Python script from beginning to end.

```
User Interaction

↓

Streamlit

↓

Run Entire Script Again

↓

Update User Interface
```

This means that every normal Python variable is recreated during each rerun.

---

# Normal Variables

Consider the following example.

```python
count = 0

if st.button("Increase"):
    count += 1

st.write(count)
```

Although the button increases the value, the script immediately reruns.

The variable `count` is recreated as:

```python
count = 0
```

The application therefore forgets its previous value.

---

# Introducing Session State

Streamlit provides a mechanism called Session State.

Session State allows information to survive script reruns.

Instead of storing data in a normal variable,

```python
count = 0
```

the application stores data inside:

```python
st.session_state
```

Session State belongs to the user's browser session and remains available until the session ends.

---

# Creating Session State

Before storing data, it must be created only once.

```python
if "count" not in st.session_state:
    st.session_state.count = 0
```

This statement checks whether the variable already exists.

If not, it is created.

Otherwise, the existing value is preserved.

---

# Counter Experiment

To understand Session State, a simple counter application was developed.

```python
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increase"):
    st.session_state.count += 1

st.write(st.session_state.count)
```

Unlike normal variables, the counter continued increasing after every button click.

This demonstrated that Session State survives Streamlit reruns.

---

# Session State is Streamlit's Memory

One of the most important lessons learned today is:

> Session State is Streamlit's memory.

It allows applications to remember information while the browser session remains active.

Without Session State:

```
0

↓

0

↓

0
```

With Session State:

```
0

↓

1

↓

2

↓

3
```

---

# Chat Components

Today's lesson introduced two Streamlit components designed specifically for conversational AI applications.

---

## st.chat_input()

```python
user_input = st.chat_input("Ask me anything...")
```

Unlike `st.text_input()`, this component is specifically designed for chat applications.

Features include:

- Automatically submits when Enter is pressed.
- Displays a modern chat input box.
- Provides a better user experience for conversational applications.

---

## st.chat_message()

```python
with st.chat_message("user"):
    st.write(user_input)
```

This component displays chat messages using built-in chat bubbles.

Supported roles include:

- user
- assistant

This makes Streamlit applications visually similar to ChatGPT.

---

# Storing Chat History

Instead of storing a single counter value,

```python
st.session_state.count
```

today's application stored an entire conversation.

```python
st.session_state.messages
```

The messages variable is simply a Python list.

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

Every new message is appended to this list.

---

# Displaying Previous Messages

Whenever the application starts, it loops through every stored message.

```python
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])
```

This redraws the entire conversation after every rerun.

Although Streamlit reruns the script, the conversation appears continuous because the messages are stored in Session State.

---

# Chat History Experiment

Before connecting Azure OpenAI, a simple chat experiment was created.

Instead of calling an AI model, the application generated an Echo response.

Example

```
User:
Hello

Assistant:
Echo: Hello
```

This experiment demonstrated that Session State successfully preserved conversation history.

---

# Integrating Azure OpenAI

After verifying that Session State worked correctly, the fake response was replaced with the existing chatbot.

Instead of

```python
response = f"Echo: {user_input}"
```

the application called

```python
response = ask_chatbot(user_input)
```

This demonstrated how Streamlit can reuse existing business logic without modifying the Azure OpenAI implementation.

---

# Software Architecture

Today's application follows a layered architecture.

```
                User
                  │
                  ▼
          Streamlit Interface
                  │
                  ▼
          Session State
                  │
                  ▼
           chatbot.py
                  │
                  ▼
        Azure OpenAI SDK
                  │
                  ▼
       Azure OpenAI Service
                  │
                  ▼
          GPT-5.4-mini
```

Each layer has a different responsibility.

---

# Separation of Concerns

One important design principle observed today is the separation of concerns.

The Streamlit application is responsible for:

- Displaying the user interface.
- Receiving user input.
- Managing Session State.

The chatbot module is responsible for:

- Communicating with Azure OpenAI.
- Sending prompts.
- Receiving AI responses.

This separation makes the application easier to maintain and extend.

---

# Design Observation

During implementation, an important architectural observation was made.

Currently, conversation history exists in two different places.

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

Both components maintain their own copy of the conversation.

This duplication can be improved in future lessons by allowing Streamlit to manage conversation history while chatbot.py focuses only on communicating with Azure OpenAI.

This refactoring will improve the architecture and better follow the Single Responsibility Principle.

---

# Key Takeaways

Today I learned that:

- Streamlit reruns the entire script after every interaction.
- Normal Python variables do not survive reruns.
- Session State stores information between reruns.
- `st.chat_input()` is designed specifically for chat applications.
- `st.chat_message()` displays professional chat bubbles.
- Chat history can be preserved using Session State.
- UI and business logic should remain separated.
- Good software architecture evolves through continuous refactoring.

---

# Summary

Today's lesson transformed the Azure AI Learning Assistant from a simple web interface into a conversational application capable of maintaining chat history during a browser session.

The most important concept learned today was Session State, which provides memory for Streamlit applications.

By combining Session State, chat components, and the existing Azure OpenAI chatbot, the application took a significant step toward becoming a professional AI assistant.

Future lessons will focus on improving the architecture by eliminating duplicated conversation history and further separating responsibilities between the user interface and the chatbot module.
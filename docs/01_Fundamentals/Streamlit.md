# Streamlit Fundamentals

## 📘 About This Document

This document contains the Streamlit concepts learned throughout my Azure AI Learning Journey.

Rather than documenting projects, this document focuses on understanding the core concepts of Streamlit and how they are used to build AI applications.

This knowledge base will continue to grow as I learn more Streamlit features.

---

# What is Streamlit?

Streamlit is an open-source Python framework that allows developers to build interactive web applications using only Python.

Unlike traditional web development, Streamlit does not require knowledge of HTML, CSS, or JavaScript.

It is widely used for:

- Machine Learning applications
- AI Chatbots
- Data Science dashboards
- Data visualization
- Rapid prototyping
- Internal business tools

For AI engineers, Streamlit provides one of the fastest ways to convert a Python script into a professional web application.

---

# Why Use Streamlit?

Without Streamlit, a developer would need to build:

- HTML pages
- CSS styling
- JavaScript interactions
- Backend APIs

Streamlit automatically handles these tasks, allowing developers to focus on Python code and application logic.

---

# How Streamlit Works

A Streamlit application is simply a Python script.

Example

```python
import streamlit as st

st.title("Hello Streamlit")
```

Run the application using

```bash
streamlit run streamlit_app.py
```

Streamlit starts a local web server and opens the application in a web browser.

---

# Streamlit Execution Model

One of the most important concepts in Streamlit is its execution model.

Whenever the user interacts with the application, Streamlit reruns the entire Python script.

```
User Interaction

↓

Streamlit

↓

Run Entire Script Again

↓

Update Interface
```

Unlike desktop applications, Streamlit does not execute only a small section of code.

Instead, the complete script is executed from top to bottom after every interaction.

Understanding this behaviour is essential for building Streamlit applications.

---

# Streamlit Widgets

Widgets are interactive components that allow users to communicate with the application.

Examples include:

- Text boxes
- Buttons
- Checkboxes
- Sliders
- Dropdowns

Every widget returns a value that can be used inside Python.

---

# st.title()

Displays the main title of the application.

Example

```python
st.title("🤖 Azure AI Learning Assistant")
```

Used for the application's primary heading.

---

# st.header()

Displays a large section heading.

Example

```python
st.header("Welcome")
```

Used to divide major sections of a page.

---

# st.subheader()

Displays a smaller heading.

Example

```python
st.subheader("My AI-102 Learning Journey")
```

Useful for grouping related content.

---

# st.write()

The most commonly used Streamlit function.

It can display:

- Text
- Numbers
- Lists
- Dictionaries
- Tables
- DataFrames

Example

```python
st.write("Hello World")
```

---

# st.markdown()

Displays Markdown content.

Example

```python
st.markdown("---")
```

Useful for:

- Horizontal lines
- Bold text
- Bullet lists
- Links
- Markdown formatting

---

# Status Components

Streamlit provides several built-in components for displaying messages.

## Success

```python
st.success("Operation completed.")
```

Displays a green success message.

---

## Info

```python
st.info("Information message.")
```

Displays an informational message.

---

## Warning

```python
st.warning("Warning message.")
```

Displays a warning.

---

## Error

```python
st.error("Error message.")
```

Displays an error message.

---

# Text Input

The first version of the chatbot used

```python
st.text_input()
```

Example

```python
user_input = st.text_input("Ask me anything")
```

This widget allows the user to type text.

Unlike chat_input(), it usually requires a button to submit the input.

---

# Buttons

Buttons perform actions when clicked.

Example

```python
if st.button("Send"):
    ...
```

Every button click causes Streamlit to rerun the script.

---

# Chat Input

Streamlit provides a dedicated input component for chat applications.

```python
user_input = st.chat_input("Ask me anything...")
```

Advantages:

- Automatically submits when Enter is pressed.
- Modern chat interface.
- Better user experience.
- Designed specifically for conversational AI applications.

---

# Chat Messages

Messages are displayed using

```python
with st.chat_message("user"):
```

or

```python
with st.chat_message("assistant"):
```

Example

```python
with st.chat_message("assistant"):
    st.write(answer)
```

This automatically renders messages using chat bubbles.

Supported roles include:

- user
- assistant

---

# Session State

One of the most important Streamlit concepts.

Session State allows an application to remember information between reruns.

Instead of

```python
count = 0
```

we use

```python
st.session_state.count = 0
```

Session State belongs to the user's browser session.

---

# Creating Session State

Before using Session State, the variable must be created.

Example

```python
if "count" not in st.session_state:
    st.session_state.count = 0
```

This ensures the variable is created only once.

---

# Counter Example

A counter application demonstrated how Session State works.

```python
if st.button("Increase"):
    st.session_state.count += 1
```

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

# Chat History

Instead of storing a single number, Session State can store a conversation.

Example

```python
st.session_state.messages = []
```

Each message is represented as a dictionary.

```python
{
    "role": "user",
    "content": "Hello"
}
```

or

```python
{
    "role": "assistant",
    "content": "Hi!"
}
```

The complete conversation is stored as a list.

---

# Displaying Chat History

The stored conversation is displayed using

```python
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])
```

Although Streamlit reruns the script after every interaction, the conversation appears continuous because the messages are stored in Session State.

---

# Streamlit Rerun

Sometimes the application needs to refresh immediately.

This can be achieved using

```python
st.rerun()
```

Example

```python
st.session_state.count += 1

st.rerun()
```

This forces Streamlit to rerun the application immediately after updating Session State.

---

# Building an AI Chat Application

The chatbot application follows the architecture below.

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
        Azure OpenAI SDK
                  │
                  ▼
       Azure OpenAI Service
                  │
                  ▼
          GPT-5.4-mini
```

The Streamlit application is responsible for:

- Collecting user input.
- Displaying responses.
- Managing Session State.

The chatbot module is responsible for:

- Communicating with Azure OpenAI.
- Sending prompts.
- Receiving responses.

---

# Key Concepts Learned

During the first four days of learning Streamlit, I learned:

- Streamlit applications are written entirely in Python.
- Streamlit reruns the complete script after every interaction.
- Widgets collect user input.
- Buttons trigger actions.
- Chat components simplify AI application development.
- Session State preserves information between reruns.
- Chat history can be stored as a list inside Session State.
- Business logic should be separated from the user interface.

---

# Best Practices Learned

- Keep UI code inside `streamlit_app.py`.
- Keep AI logic inside `chatbot.py`.
- Use `st.chat_input()` for conversational applications.
- Use `st.chat_message()` for displaying conversations.
- Store UI state inside `st.session_state`.
- Separate experiments from production code.
- Build small experiments before integrating features into the main project.
- Use Git to track code history instead of keeping old code commented out.

---

# Summary

Streamlit provides a simple yet powerful framework for building AI applications using only Python.

Its widget system allows developers to create interactive user interfaces, while Session State enables applications to preserve information across reruns.

By combining Streamlit with Azure OpenAI, it is possible to build conversational AI applications with minimal code while following good software engineering practices such as separation of concerns and reusable business logic.

This document will continue to evolve as more Streamlit concepts are learned throughout the Azure AI Learning Journey.
# Code Walkthrough - Day 003
# Building the First Streamlit Web Application

## 📘 About This Document

This document explains the implementation completed on Day 003 of the Azure AI Learning Journey.

On Day 002, the Azure OpenAI chatbot was improved by adding conversation history, allowing the application to maintain context during a terminal session.

The objective of Day 003 was to introduce **Streamlit**, understand how Streamlit applications work, and build the first web interface that will eventually replace the terminal interface.

No Azure OpenAI integration was performed today. The focus was entirely on understanding Streamlit fundamentals.

---

# Objective

Learn the fundamentals of Streamlit by creating the first web application and understanding how Python applications can be transformed into interactive web interfaces.

---

# Why Streamlit?

Until now, the chatbot was only accessible through the terminal.

```
==================================================

Azure AI Learning Assistant

==================================================

You:
```

Although this was sufficient for learning Azure OpenAI, real users expect graphical interfaces instead of command-line applications.

Streamlit allows developers to build modern web applications using only Python, without requiring HTML, CSS, or JavaScript.

---

# What is Streamlit?

Streamlit is an open-source Python framework designed for building data science and AI web applications.

Unlike traditional web frameworks, Streamlit automatically converts Python code into a web application.

This makes it an excellent choice for rapidly building AI prototypes, dashboards, and chat applications.

---

# Installing Streamlit

Streamlit was installed into the project's virtual environment.

```
pip install streamlit
```

After installation, the project dependencies were updated using:

```
pip freeze > requirements.txt
```

This ensures that anyone cloning the repository can recreate the same Python environment.

---

# Creating the First Streamlit Application

A new file was created.

```
streamlit_app.py
```

This file serves as the entry point for the web application.

The first version of the application contained:

```python
import streamlit as st

st.title("🤖 Azure AI Learning Assistant")

st.write("Welcome to my first Streamlit application!")

st.write("This application will eventually become my AI-102 Learning Assistant.")
```

This demonstrated how Python code can generate a webpage without writing HTML.

---

# Running the Application

Unlike a standard Python program, a Streamlit application is started using:

```
streamlit run streamlit_app.py
```

Once executed, Streamlit starts a local web server and opens the application in the browser.

Default URL:

```
http://localhost:8501
```

---

# Understanding the Architecture

Unlike the terminal chatbot, Streamlit introduces a browser between the user and the Python application.

```
                User
                  │
                  ▼
             Web Browser
                  │
                  ▼
         Streamlit Server
                  │
                  ▼
        streamlit_app.py
                  │
                  ▼
         Streamlit Components
                  │
                  ▼
            Rendered Web Page
```

The browser communicates with the Streamlit server, which executes the Python script and generates the user interface.

---

# Streamlit Components Learned

Several fundamental Streamlit components were explored.

## Page Title

```python
st.title("🤖 Azure AI Learning Assistant")
```

Displays the main title of the application.

---

## Header

```python
st.header("Welcome")
```

Creates a large section heading.

---

## Subheader

```python
st.subheader("My AI-102 Learning Journey")
```

Creates a smaller section heading.

---

## Write

```python
st.write("Hello World")
```

The most flexible output function.

It can display:

- Text
- Numbers
- Lists
- Dictionaries
- DataFrames
- Variables

---

## Markdown

```python
st.markdown("---")
```

Supports Markdown formatting.

Useful for:

- Horizontal lines
- Lists
- Tables
- Rich text

---

## Status Messages

Several built-in message components were explored.

```python
st.success()
```

Displays a green success message.

```python
st.info()
```

Displays an informational message.

```python
st.warning()
```

Displays a warning message.

```python
st.error()
```

Displays an error message.

These components help provide clear feedback to users.

---

# Understanding Streamlit's Execution Model

One of the most important concepts learned today is that Streamlit does **not** behave like a normal Python script.

A traditional Python application executes once.

```
Run Program

↓

Execute Code

↓

Exit
```

A Streamlit application behaves differently.

Whenever the user interacts with the interface, Streamlit reruns the entire script from top to bottom.

```
User Action

↓

Streamlit

↓

Run Entire Script Again

↓

Update Interface
```

Understanding this execution model is essential before learning Session State and building interactive applications.

---

# Comparing Terminal and Streamlit Applications

Terminal Application

```
User

↓

Terminal

↓

Python

↓

Azure OpenAI

↓

Terminal Output
```

Streamlit Application

```
User

↓

Browser

↓

Streamlit

↓

Python

↓

Azure OpenAI
```

The backend logic remains the same.

Only the user interface changes.

This separation of concerns is an important software engineering principle.

---

# Lessons Learned

Today I learned that Streamlit is a Python framework for rapidly building web applications.

Unlike traditional web development, Streamlit allows developers to create interactive interfaces without HTML, CSS, or JavaScript.

I also learned that Streamlit reruns the entire Python script whenever a user interacts with the application.

This behaviour is different from standard Python programs and explains why Session State will become important in future lessons.

---

# What's Next?

The current Streamlit application only displays static content.

In the next lesson, the following features will be implemented:

- User input
- Chat interface
- Session State
- Chat messages
- Integration with the existing Azure OpenAI chatbot
- Conversation history inside the web application

---

# Summary

Day 003 introduced Streamlit as the frontend technology for the Azure AI Learning Assistant.

Key accomplishments include:

- Installed Streamlit.
- Created the first Streamlit application.
- Learned how to run Streamlit applications.
- Explored the core Streamlit components.
- Understood Streamlit's execution model.
- Compared terminal and web application architectures.

This lesson establishes the foundation for building a professional web-based Azure AI chatbot in the upcoming lessons.
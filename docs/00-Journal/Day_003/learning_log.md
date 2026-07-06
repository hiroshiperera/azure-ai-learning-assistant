# Understanding Streamlit

## 📘 About This Document

This document introduces Streamlit, a Python framework for building interactive web applications.

Unlike traditional web development frameworks, Streamlit allows developers to create modern user interfaces using only Python. It is widely used for data science, machine learning, dashboards, and AI applications because it enables rapid development without requiring HTML, CSS, or JavaScript.

In this learning session, I explored the fundamentals of Streamlit and built my first web application. This knowledge will serve as the frontend foundation for my Azure AI Learning Assistant.

---

# Learning Objectives

After completing this topic, I should be able to:

- Explain what Streamlit is.
- Understand why Streamlit was created.
- Explain how Streamlit works.
- Create a basic Streamlit application.
- Run a Streamlit application.
- Understand Streamlit's execution model.
- Use the most common Streamlit components.
- Explain the difference between a terminal application and a Streamlit web application.

---

# What is Streamlit?

Streamlit is an open-source Python framework for building interactive web applications.

It enables developers to transform Python scripts into web applications without writing HTML, CSS, or JavaScript.

Originally designed for data scientists and machine learning engineers, Streamlit has become one of the most popular frameworks for creating AI demonstrations, dashboards, prototypes, and chat applications.

---

# Why Was Streamlit Created?

Traditional web development requires multiple technologies.

For example:

- HTML
- CSS
- JavaScript
- Backend Framework
- API

For many AI engineers, learning all these technologies before demonstrating an AI model can be time-consuming.

Streamlit solves this problem by allowing developers to build web applications entirely in Python.

This enables rapid prototyping while focusing on AI rather than frontend development.

---

# Why Use Streamlit for AI Applications?

Streamlit is especially useful for AI projects because it:

- Requires only Python.
- Is simple to learn.
- Provides built-in UI components.
- Supports data visualization.
- Supports chat interfaces.
- Integrates easily with AI models.
- Enables rapid application development.

Many AI demonstrations and proof-of-concept applications are built using Streamlit.

---

# Streamlit Architecture

A Streamlit application consists of several components working together.

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
          Python Script
                  │
                  ▼
       Streamlit Components
                  │
                  ▼
           Rendered Web Page
```

Unlike a terminal application, Streamlit introduces a browser-based interface between the user and the Python application.

---

# Creating the First Streamlit Application

A Streamlit application begins by importing the framework.

```python
import streamlit as st
```

This provides access to all Streamlit components.

The first application created was:

```python
import streamlit as st

st.title("🤖 Azure AI Learning Assistant")

st.write("Welcome to my first Streamlit application!")

st.write("This application will eventually become my AI-102 Learning Assistant.")
```

Even though only a few lines of code were written, Streamlit automatically generated a web page.

---

# Running a Streamlit Application

Unlike normal Python applications, Streamlit applications are executed using:

```bash
streamlit run streamlit_app.py
```

This command starts a local Streamlit server and opens the application in the default web browser.

By default, Streamlit runs on:

```
http://localhost:8501
```

---

# Streamlit Components Learned

Several core Streamlit components were explored.

## Title

```python
st.title()
```

Displays the main title of the page.

---

## Header

```python
st.header()
```

Displays a section heading.

---

## Subheader

```python
st.subheader()
```

Displays a smaller heading.

---

## Write

```python
st.write()
```

The most flexible Streamlit function.

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
st.markdown()
```

Supports Markdown formatting.

Useful for creating:

- Lists
- Tables
- Hyperlinks
- Horizontal lines
- Rich formatted text

---

## Status Components

Streamlit includes several built-in components for displaying status messages.

```python
st.success()
```

Displays a success message.

```python
st.info()
```

Displays informational content.

```python
st.warning()
```

Displays warnings.

```python
st.error()
```

Displays error messages.

These components improve the user experience by visually distinguishing different types of information.

---

# Understanding Streamlit's Execution Model

One of the most important concepts learned is how Streamlit executes Python code.

Unlike a traditional Python program that executes once and exits, a Streamlit application reruns the entire script whenever the user interacts with the interface.

Traditional Python Program

```
Run Program

↓

Execute Once

↓

Exit
```

Streamlit Application

```
User Interaction

↓

Run Entire Script Again

↓

Update User Interface
```

Understanding this behavior is essential before learning Session State and building interactive applications.

---

# Terminal Application vs Streamlit Application

Terminal Application

```
User

↓

Terminal

↓

Python

↓

Output
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

Rendered Web Page
```

The application logic remains the same.

Only the presentation layer changes.

---

# Advantages of Streamlit

- Simple to learn.
- Fast development.
- Pure Python.
- Excellent for AI applications.
- Interactive user interfaces.
- Rapid prototyping.
- Built-in visualization support.
- Modern chat components.

---

# Limitations of Streamlit

Although Streamlit is excellent for prototypes and AI demonstrations, it is not designed to replace full-featured web frameworks.

Large enterprise applications often use frameworks such as:

- FastAPI
- Django
- Flask

Streamlit is best suited for rapid development and AI interfaces.

---

# Key Takeaways

- Streamlit is a Python framework for building web applications.
- No HTML, CSS, or JavaScript is required.
- Streamlit automatically creates a web interface from Python code.
- Applications run inside a web browser.
- Every user interaction reruns the Python script.
- Streamlit provides built-in UI components.
- Streamlit is widely used for AI and machine learning applications.

---

# Summary

Streamlit provides one of the simplest ways to transform Python applications into interactive web applications.

It enables AI engineers to build professional-looking interfaces without requiring frontend development skills.

Understanding Streamlit fundamentals provides the foundation for building the web interface of the Azure AI Learning Assistant. In future lessons, Streamlit will be integrated with Azure OpenAI to create a complete conversational AI application capable of maintaining conversation history and interacting with Azure AI services.
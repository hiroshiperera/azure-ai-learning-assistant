# Code Walkthrough - Day 002
# Adding Conversation History to the Azure OpenAI Chatbot

## 📘 About This Document

This document explains the changes made to the Azure OpenAI Terminal Chatbot on Day 002.

On Day 001, the chatbot was able to send user prompts to Azure OpenAI and display responses. However, every request was treated as a completely new conversation because previous messages were not preserved.

The objective of Day 002 was to introduce **conversation history**, allowing the chatbot to remember previous interactions within the same session.

---

# Objective

Convert the chatbot from a **stateless** application into a **stateful** conversational chatbot.

---

# What Was Wrong With the Previous Implementation?

In the original implementation, the `messages` list was created inside the `ask_chatbot()` function.

```python
messages=[
    {
        "role":"system",
        "content":"You are a helpful AI assistant."
    },
    {
        "role":"user",
        "content":user_message
    }
]
```

Every time the function was called:

1. A new `messages` list was created.
2. Previous conversations were discarded.
3. Azure OpenAI only received the current question.

As a result, the chatbot had no memory of earlier interactions.

Example:

```
User:
My name is Hiroshi.

AI:
Nice to meet you.

User:
What is my name?

AI:
I don't know.
```

Although this behavior seems like the model forgot the conversation, the real reason is that the application never sent the previous messages back to Azure OpenAI.

---

# Understanding Conversation History

Large Language Models do not automatically remember previous conversations.

Instead, the application is responsible for maintaining the conversation history and sending it with every request.

The conversation history is represented as a Python list.

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]
```

Each item in the list represents one message exchanged during the conversation.

---

# New Architecture

```
                User
                  │
                  ▼
            app.py
                  │
                  ▼
          ask_chatbot()
                  │
                  ▼
        Conversation History
          (messages list)
                  │
                  ▼
      OpenAI Python SDK
                  │
                  ▼
       Azure OpenAI Service
                  │
                  ▼
      GPT-5.4-mini Deployment
                  │
                  ▼
         AI Generated Response
                  │
                  ▼
        Conversation History
        (Assistant Response)
                  │
                  ▼
               Terminal
```

The application now maintains the conversation history before and after every request.

---

# Step 1 - Create the Conversation History

Instead of creating the messages list inside the function, it is created once when the application starts.

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]
```

Why?

Creating the list once allows the application to preserve previous messages throughout the lifetime of the program.

---

# Step 2 - Store the User Message

Before sending a request to Azure OpenAI, the user's message is added to the conversation history.

```python
messages.append(
    {
        "role": "user",
        "content": user_message
    }
)
```

This ensures that Azure receives the latest user input together with the previous conversation.

---

# Step 3 - Send the Complete Conversation

Previously, only the latest message was sent.

Now the entire conversation is sent.

```python
response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=messages
)
```

The `messages` variable now contains every message exchanged since the application started.

---

# Step 4 - Save the Assistant's Response

After Azure OpenAI generates a response, the assistant's reply is also stored.

```python
answer = response.choices[0].message.content

messages.append(
    {
        "role": "assistant",
        "content": answer
    }
)
```

Saving the assistant's reply allows future requests to include both sides of the conversation.

---

# How the Conversation Grows

When the application starts:

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]
```

After the user says:

```
Hello
```

```
System

↓

User
```

After Azure replies:

```
System

↓

User

↓

Assistant
```

After another user question:

```
System

↓

User

↓

Assistant

↓

User
```

The list continues to grow as long as the application is running.

---

# Understanding the Message Roles

Every message contains two properties.

## System

Defines the behaviour of the AI.

Example

```
You are a helpful AI assistant.
```

---

## User

Represents input from the user.

Example

```
What is Azure OpenAI?
```

---

## Assistant

Represents the AI-generated response.

Example

```
Azure OpenAI is Microsoft's managed service...
```

The conversation is simply an ordered list of these three message types.

---

# Why This Works

Azure OpenAI does not store conversation history.

Instead, the application sends the complete conversation every time a request is made.

The model reads the conversation history and generates a response based on all previous messages.

This is why the chatbot can answer questions such as:

```
User:
My name is Hiroshi.

AI:
Nice to meet you.

User:
What is my name?

AI:
Your name is Hiroshi.
```

---

# Limitations

The current implementation stores conversation history only while the application is running.

When the application closes, the conversation is lost.

In future lessons, conversation history can be stored using:

- Files
- Databases
- Redis
- Azure Cosmos DB
- Azure AI Memory solutions

---

# Lessons Learned

Today I learned that Large Language Models do not automatically remember previous conversations.

Conversation memory is created by the application, not by the model.

By maintaining a list of messages and sending the complete conversation with every request, a chatbot can support multi-turn conversations and maintain context throughout the session.

---

# Summary

Today's enhancement transformed the chatbot from a stateless application into a stateful conversational assistant.

Key improvements include:

- Introduced conversation history.
- Stored user messages.
- Stored assistant responses.
- Sent the complete conversation to Azure OpenAI.
- Enabled multi-turn conversations.
- Improved understanding of how chat-based AI applications work.

This implementation forms the foundation for future enhancements such as Streamlit interfaces, persistent chat history, Retrieval-Augmented Generation (RAG), and AI Agents.
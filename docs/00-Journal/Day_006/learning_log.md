# Day 006 - Prompt Engineering Fundamentals

**Date:** 17 July 2026

---

# 📘 About Today

Today's lesson introduced one of the most important concepts in Generative AI and the AI-102 certification: **Prompt Engineering**.

Until now, I had been sending prompts to Azure OpenAI without thinking deeply about how the instructions influenced the model's behavior.

Today I learned that the prompt is not just user input—it is one of the most important parts of an AI application. By carefully designing prompts, developers can guide the model to produce responses that match a specific role, style, audience, or objective.

I also improved the architecture of my application by separating prompts from the application logic.

---

# Learning Objectives

Today's goals were to:

- Understand Prompt Engineering.
- Learn the purpose of the System Prompt.
- Understand the different message roles.
- Observe how changing the System Prompt changes the AI's behaviour.
- Separate prompt configuration from application logic.

---

# What I Learned

## Prompt Engineering

Prompt Engineering is the process of designing effective instructions for a Large Language Model.

Rather than changing the AI model itself, developers improve the quality of the instructions they send to the model.

Well-designed prompts produce more useful, accurate, and consistent responses.

---

## The Three Message Roles

Azure OpenAI conversations consist of three message roles.

### System

Defines the behaviour and personality of the AI.

Example:

```
You are an Azure AI tutor helping students prepare for AI-102.
```

---

### User

Represents the user's question or request.

Example:

```
What is Azure OpenAI?
```

---

### Assistant

Represents previous AI responses and enables multi-turn conversations.

---

# Experiment

Today I experimented with different System Prompts.

For each experiment, I asked exactly the same question:

```
What is Azure OpenAI?
```

Only the System Prompt changed.

Examples included:

- Pirate
- AI-102 Instructor
- Senior Software Engineer

Although the model remained the same, the responses changed significantly depending on the System Prompt.

This demonstrated that the System Prompt controls the overall behaviour of the AI.

---

# Software Engineering Improvement

Previously, the System Prompt was hardcoded inside the application.

Today I introduced a dedicated file:

```
src/
    prompts.py
```

The System Prompt is now stored separately from the chatbot logic.

This makes the application easier to maintain and allows prompts to be reused across different AI applications.

---

# Why This Matters

Separating prompts from the application logic follows good software engineering practices.

Future AI applications can simply replace the prompt without changing the chatbot implementation.

Examples include:

- AI Tutor
- Travel Assistant
- Math Teacher
- Customer Support Bot
- AI Agent

Only the prompt changes.

---

# Lessons Learned

Today I learned that:

- Prompt Engineering is a core skill in Generative AI.
- The System Prompt controls the behaviour of the AI.
- User messages ask questions.
- Assistant messages preserve conversation history.
- Prompts should be managed separately from application logic.
- Good software architecture supports better AI development.

---

# AI-102 Connection

Today's lesson directly relates to:

**Implement Generative AI Solutions using Azure OpenAI**

Understanding prompt design is essential for building effective AI applications and is a key practical skill for AI Engineers.

---

# Summary

Today's lesson introduced Prompt Engineering and demonstrated how carefully designed prompts influence the behaviour of Large Language Models.

I also improved my application architecture by introducing a dedicated `prompts.py` file, separating prompt configuration from business logic.

This forms the foundation for future topics such as Prompt Templates, Retrieval-Augmented Generation (RAG), AI Agents, and Structured Outputs.


# AI-102 Progress

## Skill Area

Implement Generative AI Solutions

## Concepts Covered

- Prompt Engineering
- System Prompt
- User Messages
- Assistant Messages
- Prompt Management

## Exam Readiness

⭐⭐⭐⭐⭐ (5/5)
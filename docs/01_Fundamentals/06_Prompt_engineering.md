# Prompt Engineering

## 📘 About This Document

Prompt Engineering is the process of designing effective instructions that guide a Large Language Model (LLM) to produce accurate, useful, and consistent responses.

Rather than changing the AI model itself, developers improve the quality of the instructions they send to the model.

Prompt Engineering is one of the most important skills for building Generative AI applications and is widely used with Azure OpenAI.

---

# Learning Objectives

After completing this topic, I should be able to:

- Explain Prompt Engineering.
- Understand the three message roles.
- Design effective System Prompts.
- Explain how prompts influence model behaviour.
- Apply Prompt Engineering when building Azure AI applications.

---

# What is Prompt Engineering?

Prompt Engineering is the practice of writing clear, structured, and purposeful instructions for an AI model.

The quality of the output often depends on the quality of the prompt.

Good prompts lead to better AI responses.

---

# Why is Prompt Engineering Important?

Prompt Engineering helps developers:

- Control AI behaviour.
- Improve response quality.
- Reduce ambiguity.
- Produce consistent outputs.
- Build specialised AI assistants.

---

# Message Roles

Azure OpenAI conversations consist of three message types.

## System

Defines the AI's behaviour.

Example:

```
You are an Azure AI tutor.
```

---

## User

Represents the user's request.

Example:

```
Explain Azure AI Search.
```

---

## Assistant

Represents previous AI responses.

Assistant messages allow the AI to maintain conversation context.

---

# System Prompt

The System Prompt is one of the most important parts of a Generative AI application.

It tells the model:

- Who it is.
- How it should respond.
- What style to use.
- What rules to follow.

Example:

```
You are an Azure AI instructor.

Explain concepts using simple English.

Provide practical examples.

Relate explanations to AI-102 where appropriate.
```

---

# Prompt Engineering Examples

Poor Prompt

```
Explain Azure.
```

Better Prompt

```
You are an Azure AI instructor.

Explain Azure OpenAI to a beginner preparing for AI-102.

Use simple English.

Provide one practical example.

Limit your response to 150 words.
```

The second prompt provides clearer guidance and produces a more focused response.

---

# Best Practices

Good prompts should:

- Be clear.
- Be specific.
- Define the AI's role.
- Specify the audience.
- Include constraints when necessary.
- Request examples if helpful.

---

# Prompt Engineering in This Project

The Azure AI Learning Assistant stores prompts inside:

```
src/
    prompts.py
```

Separating prompts from application logic makes the application easier to maintain and reuse.

---

# AI-102 Connection

Prompt Engineering is an essential skill when implementing Generative AI solutions with Azure OpenAI.

Understanding how prompts influence model behaviour helps developers create more effective AI applications.

---

# Key Takeaways

- Prompt Engineering guides AI behaviour.
- The System Prompt defines the AI's role.
- User messages contain requests.
- Assistant messages maintain context.
- Well-designed prompts improve response quality.
- Prompt management should be separated from application logic.

---

# Summary

Prompt Engineering is the process of designing effective instructions for Large Language Models.

By carefully defining the System Prompt and structuring user interactions, developers can create AI applications that produce accurate, consistent, and user-focused responses.

This knowledge provides the foundation for future topics including Prompt Templates, Structured Outputs, Retrieval-Augmented Generation (RAG), and AI Agents.
# Azure AI Learning Journey

> My personal Azure AI Engineering journey towards AI-102 certification.
>
> Goal: Pass AI-102 in November 2026 by understanding the theory, building real-world projects, documenting everything, and creating a professional GitHub portfolio.

---

# Lesson 01 - Azure Foundations & First Azure OpenAI Chatbot

**Date:** 05 July 2026

## Objective

Set up the Azure environment from scratch and build my first Azure OpenAI application using Python.

---

## What I Learned

### Azure Fundamentals

- Difference between Azure Subscription and Resource Group.
- Why Resource Groups are used.
- Pay-As-You-Go pricing model.
- Importance of creating Budgets before creating resources.
- Azure pricing awareness.
- Azure regions and why East US was selected.

---

### Azure OpenAI

- Created my first Azure OpenAI Resource.
- Understood the difference between:
  - Azure OpenAI Resource
  - Model
  - Deployment
- Learned how Azure AI Foundry works.
- Deployed GPT-5.4-mini.
- Learned that some older model versions are deprecated and cannot be used for new deployments.

---

### Python SDK

- Created a Python virtual environment using:

```bash
python -m venv .venv
```

- Activated the environment.

```bash
.venv\Scripts\activate
```

- Installed the required packages.

- Used the official OpenAI Python SDK (v2.x).

- Configured environment variables using `.env`.

---

### Project Built

✅ Terminal-based Azure AI Chatbot

Features

- User enters a prompt.
- Prompt is sent to Azure OpenAI.
- GPT-5.4-mini generates a response.
- Response is displayed in the terminal.

---

## Problems I Solved

### 1. Azure Subscription

Initially couldn't create a subscription.

Eventually upgraded to Pay-As-You-Go and successfully created the subscription.

---

### 2. Budget

Created a monthly budget.

- Budget: USD 10
- Alert at 50%
- Alert at 80%
- Alert at 100%

---

### 3. GPT Deployment

Initially attempted to deploy older GPT models.

Deployment failed because the selected model version was deprecated.

Solution:

Created a deployment using GPT-5.4-mini.

---

### 4. Python Configuration

Created:

- src/config.py
- .env

to securely store configuration values.

---

### 5. Azure Endpoint

Received:

404 Resource Not Found

Reason:

Incorrect Azure endpoint.

Solution:

Correct Azure endpoint:

https://aoai-ai102-learning.openai.azure.com/openai/v1/

---

## Azure Resources Created

- Azure Subscription
- Monthly Budget
- Resource Group
- Azure OpenAI Resource
- GPT-5.4-mini Deployment

---

## Folder Structure Created

```
azure-ai-learning-assistant/

src/
tests/
docs/

app.py
requirements.txt
.env
README.md
```

---

## Documentation Created

- Azure Foundation
- Azure OpenAI
- Python SDK
- Terminal Chatbot
- Cheat Sheet

---

## GitHub Status

Repository initialized.

Project structure prepared for future commits.

---

## Key Takeaways

Today I realized that building a real project teaches much more than simply watching videos.

I successfully created my first Azure OpenAI application from scratch, solved real deployment and configuration issues, and connected Azure OpenAI to Python.

This project gave me confidence that I can build AI applications rather than only study theory.

---

## Next Lesson

Lesson 02

Production-Ready Chatbot

Topics

- Streamlit
- Prompt Engineering
- Better project structure
- Chat history
- AI-102 concepts related to chat applications

---

# Progress

- [x] Azure Subscription
- [x] Budget
- [x] Resource Group
- [x] Azure OpenAI
- [x] GPT Deployment
- [x] Python SDK
- [x] First Chatbot

Current Progress: 1 / 40 Lessons
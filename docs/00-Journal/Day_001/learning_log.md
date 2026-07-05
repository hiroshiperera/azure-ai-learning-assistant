# Day 001 - My First Azure OpenAI Application

**Date:** 05 July 2026

---

# 🎯 Goal

Build my first Azure OpenAI application from scratch and understand the complete process of connecting a Python application to Azure OpenAI.

---

# 📖 What I Learned

Today I began my Azure AI engineering journey.

Instead of only studying theory, I built my first working Azure OpenAI application.

During this process, I learned how Azure resources are organized and how a Python application communicates with Azure OpenAI.

## Azure Fundamentals

I learned the purpose of:

- Azure Subscription
- Pay-As-You-Go pricing
- Azure Budget
- Resource Groups

I also learned that Resource Groups are free and are used to logically organize Azure resources.

---

## Azure OpenAI

I created my first Azure OpenAI Resource.

I learned the difference between:

- Azure OpenAI Resource
- Model
- Deployment

I deployed the **GPT-5.4-mini** model using Azure AI Foundry.

I also learned that applications communicate with the **deployment name**, not directly with the model name.

---

## Python Development

I created my first Azure AI Python project.

Project structure included:

- Virtual Environment
- requirements.txt
- .env
- src folder
- Configuration file

I learned how to securely store Azure credentials using environment variables.

---

## Azure OpenAI SDK

I connected my Python application to Azure OpenAI using the official OpenAI Python SDK.

I learned how to:

- Create the Azure OpenAI client
- Send prompts
- Receive responses
- Display the AI response in the terminal

---

# 🛠️ What I Built

Successfully built:

✅ Azure OpenAI Terminal Chatbot

Features:

- Accepts user questions
- Sends requests to Azure OpenAI
- Generates AI responses
- Displays responses in the terminal

Example:

User:

> What is the capital city of Sri Lanka?

AI:

> Sri Jayawardenepura Kotte

---

# 🐞 Problems I Solved

## Problem 1

Initially I was unable to create a new Azure subscription because of Microsoft account restrictions.

Solution:

Used my existing Pay-As-You-Go subscription.

---

## Problem 2

GPT deployment failed because the selected model version had been deprecated.

Solution:

Deployed **GPT-5.4-mini** instead.

---

## Problem 3

Received:

404 Resource Not Found

Cause:

The Azure OpenAI endpoint was incorrect.

Solution:

Updated the endpoint to include:

```
/openai/v1/
```

The chatbot successfully connected afterwards.

---

## Problem 4

Learned how to configure:

- Endpoint
- API Key
- Deployment Name

using a `.env` file instead of hardcoding values.

---

# 💡 Key Takeaways

Today I realized that building a project teaches me much more than simply watching videos.

Although I have completed several AI courses before, this hands-on approach helped me understand how Azure OpenAI actually works.

I also discovered that debugging real problems significantly improves my understanding of the platform.

---

# 🚀 Progress

Completed:

- ✅ Azure Subscription
- ✅ Azure Budget
- ✅ Resource Group
- ✅ Azure OpenAI Resource
- ✅ GPT-5.4-mini Deployment
- ✅ Python Project Setup
- ✅ Virtual Environment
- ✅ Environment Variables
- ✅ Azure OpenAI SDK
- ✅ First Azure OpenAI Chatbot

---

# 🤔 Reflection

## What went well

- Successfully deployed my first Azure OpenAI model.
- Connected Python to Azure OpenAI.
- Built a fully working chatbot.
- Solved a real Azure endpoint issue.

## What challenged me

- Understanding the difference between a Resource, Deployment, and Model.
- Configuring the correct Azure endpoint.
- Learning Azure AI Foundry for the first time.

## Lessons for my future self

- Always configure a budget before creating Azure resources.
- Keep secrets in a `.env` file.
- Deployment Name is not the same as the Model Name.
- Read Azure error messages carefully—they usually point to the root cause.

---

# 📅 Next Goal

Build a production-ready chatbot by adding:

- Better project structure
- Streamlit user interface
- Prompt Engineering
- Conversation history

Continue documenting everything as part of my Azure AI Learning Journey.
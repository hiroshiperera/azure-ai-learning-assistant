# Azure Foundations - Implementation Guide

## 📘 About This Document

This document records the practical implementation steps I performed while setting up my Azure environment for AI development. It serves as a reproducible guide for creating the Azure resources required before building Azure AI applications.

The objective of this implementation was to prepare a secure and cost-controlled Azure environment for developing Azure OpenAI applications.

---

# Implementation Objectives

By completing this implementation, I achieved the following:

- Created an Azure Pay-As-You-Go subscription.
- Configured cost monitoring using Azure Budgets.
- Created a Resource Group.
- Created an Azure OpenAI Resource.
- Deployed my first GPT model.
- Retrieved the Endpoint and API Key.
- Verified the Azure OpenAI service was ready for Python development.

---

# Prerequisites

Before beginning, ensure you have:

- Microsoft Account
- Azure Subscription
- Internet Connection
- Web Browser
- Access to Azure Portal

Azure Portal

https://portal.azure.com

---

# Step 1 - Sign in to Azure Portal

Navigate to

https://portal.azure.com

Sign in using your Microsoft account.

Result

✅ Successfully signed in to Azure Portal.

---

# Step 2 - Verify Azure Subscription

Navigate to

Home

↓

Subscriptions

Verified that my existing Pay-As-You-Go subscription was available.

Subscription Name

AI-102-Learning

Result

✅ Azure subscription ready.

---

# Step 3 - Create a Budget

Purpose

Prevent unexpected Azure charges while learning.

Navigation

Cost Management

↓

Budgets

↓

Create

Configuration

Budget Name

AI-102-Budget

Budget Amount

USD 10

Alerts

- 50%
- 80%
- 100%

Result

✅ Budget successfully created.

---

# Step 4 - Create Resource Group

Purpose

Organize Azure resources for this project.

Navigation

Resource Groups

↓

Create

Configuration

Resource Group

rg-ai102-learning

Region

East US

Result

✅ Resource Group successfully created.

---

# Step 5 - Create Azure OpenAI Resource

Purpose

Create an Azure resource capable of hosting OpenAI models.

Navigation

Marketplace

↓

Azure OpenAI

↓

Create

Configuration

Subscription

AI-102-Learning

Resource Group

rg-ai102-learning

Region

East US

Resource Name

aoai-ai102-learning

Pricing Tier

Standard S0

Networking

All Networks

Tags

None

Result

✅ Azure OpenAI Resource successfully created.

---

# Step 6 - Open Azure AI Foundry

Purpose

Manage Azure OpenAI deployments.

Navigation

Azure OpenAI Resource

↓

Go to Foundry Portal

Result

✅ Azure AI Foundry opened successfully.

---

# Step 7 - Deploy GPT Model

Purpose

Deploy a model that applications can access.

Navigation

Chat Playground

↓

Create Deployment

Model

GPT-5.4-mini

Deployment Type

Global Standard

Deployment Name

gpt-5.4-mini

Result

✅ Deployment completed successfully.

---

# Step 8 - Retrieve Endpoint

Purpose

Allow Python applications to communicate with Azure OpenAI.

Navigation

Azure OpenAI Resource

↓

Overview

↓

Endpoints

Copied

Azure OpenAI Endpoint

Example

```
https://aoai-ai102-learning.openai.azure.com/openai/v1/
```

Result

✅ Endpoint copied successfully.

---

# Step 9 - Retrieve API Key

Purpose

Authenticate requests to Azure OpenAI.

Navigation

Azure OpenAI Resource

↓

Keys and Endpoint

Copied

- Key 1
- Endpoint

Result

✅ API Key copied successfully.

---

# Step 10 - Verify Deployment

Opened Azure AI Foundry.

Opened Chat Playground.

Selected

```
gpt-5.4-mini
```

Verified the deployment was available.

Result

✅ Deployment verified.

---

# Azure Resources Created

| Resource | Name |
|----------|------|
| Subscription | AI-102-Learning |
| Budget | AI-102-Budget |
| Resource Group | rg-ai102-learning |
| Azure OpenAI Resource | aoai-ai102-learning |
| Model Deployment | gpt-5.4-mini |

---

# Azure Regions Used

| Resource | Region |
|----------|--------|
| Resource Group | East US |
| Azure OpenAI | East US |
| GPT Deployment | Global Standard |

---

# Security Configuration

Implemented the following security practices:

- API Keys stored in `.env`
- `.env` excluded from Git using `.gitignore`
- No secrets hardcoded into source code

Result

✅ Secure configuration completed.

---

# Validation

Verified the following:

- Azure Portal accessible
- Subscription active
- Budget active
- Resource Group created
- Azure OpenAI Resource created
- GPT Deployment available
- Endpoint accessible
- API Key retrieved

Result

✅ Azure environment successfully configured.

---

# Lessons Learned

During this implementation, I learned:

- Azure resources are organized using Resource Groups.
- Budgets help monitor cloud spending.
- Azure OpenAI requires a deployed model before it can process requests.
- Applications connect using the Deployment Name rather than the model name.
- API Keys should never be hardcoded.
- Proper resource naming improves project organization.

---

# Next Implementation

The Azure environment is now ready.

The next implementation will focus on:

- Creating the Python project
- Configuring the virtual environment
- Installing the OpenAI SDK
- Connecting Python to Azure OpenAI
- Building the first Azure AI chatbot
# Azure Fundamentals

## 📘 About This Document

This document explains the fundamental Azure concepts required before building any Azure AI solution. Understanding these concepts is essential because every Azure AI service, including Azure OpenAI, Azure AI Search, Document Intelligence, and Azure AI Foundry, is deployed and managed within the Azure cloud platform.

These concepts form the foundation for the AI-102 certification and are used throughout almost every Azure AI project.

---

# Why Learn Azure Fundamentals?

Before creating AI applications, it is important to understand how Azure organizes cloud resources, manages billing, secures services, and deploys applications.

Without understanding Azure Fundamentals, it becomes difficult to troubleshoot issues, manage cloud costs, or design scalable AI solutions.

This module introduces the core building blocks that every Azure AI Engineer should understand.

---

# Microsoft Azure

Microsoft Azure is Microsoft's cloud computing platform that provides more than 200 cloud services for building, deploying, and managing applications.

Azure allows organizations and developers to rent computing resources instead of purchasing physical servers.

Azure provides services such as:

- Virtual Machines
- Storage
- Databases
- Networking
- Artificial Intelligence
- Machine Learning
- Security
- Analytics
- DevOps

Azure OpenAI is one of these cloud services.

---

# Azure Account

An Azure Account represents your identity within Microsoft Azure.

Your Azure Account allows you to:

- Sign in to Azure Portal
- Create Azure resources
- Manage subscriptions
- Access Azure services
- View billing information

A single Azure account can own multiple Azure subscriptions.

---

# Azure Subscription

A Subscription is a billing and management boundary inside Azure.

Every Azure resource belongs to a subscription.

The subscription determines:

- Billing
- Spending
- Access permissions
- Resource quotas
- Service availability

Think of a subscription as your Azure workspace.

Example

Azure Account

↓

Azure Subscription

↓

Resources

---

# Pay-As-You-Go Subscription

Pay-As-You-Go is one of Azure's pricing models.

Instead of paying a monthly fixed fee, you only pay for the services you actually use.

Advantages

- No long-term commitment
- Ideal for learning
- Suitable for development
- Easy to scale

Disadvantages

- Unexpected costs if resources are left running

This is why budgeting is important.

---

# Azure Budget

An Azure Budget allows you to monitor your cloud spending.

A budget helps you:

- Track costs
- Receive notifications
- Prevent unexpected bills

Important

Budgets DO NOT stop Azure resources.

They only send alerts.

For learning projects, it is recommended to create a small monthly budget before creating resources.

Example

Monthly Budget

USD 10

Alerts

- 50%
- 80%
- 100%

---

# Resource Group

A Resource Group is a logical container that organizes Azure resources.

Every Azure resource must belong to one Resource Group.

A Resource Group makes it easier to:

- Organize projects
- Delete multiple resources together
- Apply security
- Track costs

Example

Resource Group

↓

Azure OpenAI

↓

Storage

↓

Azure AI Search

↓

Key Vault

Important

Resource Groups are completely FREE.

Only the resources inside them generate costs.

---

# Azure Region

Azure operates data centers around the world.

These geographical locations are called Regions.

Examples

- East US
- West Europe
- Southeast Asia
- Australia East

Choosing the correct region is important because it affects:

- Latency
- Available services
- Pricing
- Compliance

For this project we selected:

East US

---

# Azure Portal

The Azure Portal is Microsoft's web interface for managing Azure resources.

Through the Azure Portal you can:

- Create resources
- Monitor usage
- Configure networking
- Manage subscriptions
- View costs
- Deploy AI services

Portal

https://portal.azure.com

---

# Azure AI Foundry

Azure AI Foundry is Microsoft's platform for building Generative AI applications.

It allows developers to:

- Deploy GPT models
- Test prompts
- Build AI applications
- Manage model deployments
- Create AI agents
- Connect AI with enterprise data

Azure AI Foundry is where Azure OpenAI models are deployed and managed.

---

# Azure OpenAI Resource

An Azure OpenAI Resource provides secure access to OpenAI models through Microsoft Azure.

It manages:

- API Keys
- Endpoints
- Billing
- Security
- Deployments

Without creating this resource, applications cannot communicate with GPT models.

---

# Relationship Between Azure Components

Microsoft Account

↓

Azure Subscription

↓

Resource Group

↓

Azure OpenAI Resource

↓

Model Deployment

↓

Python Application

Every AI application follows this structure.

---

# Best Practices

Always:

- Create a budget before creating resources.
- Use meaningful names for Resource Groups.
- Store API Keys securely.
- Delete unused Azure resources.
- Keep resources in the same region whenever possible.
- Never expose secrets in GitHub.

---

# Summary

After completing Azure Fundamentals, I should understand:

✅ What Microsoft Azure is

✅ What an Azure Account is

✅ What a Subscription is

✅ Pay-As-You-Go pricing

✅ Azure Budgets

✅ Resource Groups

✅ Azure Regions

✅ Azure Portal

✅ Azure AI Foundry

✅ Azure OpenAI Resources

These concepts form the foundation for every Azure AI project and will be used repeatedly throughout the AI-102 learning journey.
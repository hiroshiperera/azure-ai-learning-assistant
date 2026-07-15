# Day 007 - Understanding Model Parameters

**Date:** 18 July 2026

---

# About Today

Today's lesson focused on understanding how Azure OpenAI model parameters influence the behaviour of Large Language Models.

Until today, my chatbot used the default model settings. I learned that developers can configure model behaviour without changing the model itself.

---

# Learning Objectives

Today's goals were to:

- Understand Temperature.
- Understand Max Completion Tokens.
- Learn about Top P.
- Observe how different parameter values change model responses.
- Learn about model compatibility across Azure OpenAI models.

---

# What I Learned

## Temperature

Temperature controls creativity.

Low values produce predictable and factual responses.

Higher values encourage more creative responses.

---

## Max Completion Tokens

This parameter limits the maximum length of the generated response.

Smaller values generate concise answers.

Larger values allow detailed explanations.

---

## Top P

Top P is another sampling parameter used to control randomness.

For most beginner applications, adjusting Temperature alone is sufficient.

---

# Practical Experiment

I experimented with different values for:

- Temperature
- Max Completion Tokens

I observed that changing these settings significantly changed the model's behaviour even though the model itself remained the same.

---

# Important Discovery

While implementing today's lesson, I encountered the following Azure OpenAI error:

```
Unsupported parameter:
'max_tokens'

Use 'max_completion_tokens' instead.
```

I learned that newer GPT-5 models use `max_completion_tokens` rather than `max_tokens`.

This reinforced the importance of reading API error messages carefully and understanding model compatibility.

---

# AI-102 Connection

Today's lesson directly supports:

**Implement Generative AI Solutions using Azure OpenAI**

Understanding model parameters is essential when building reliable and effective AI applications.

---

# Lessons Learned

Today I learned:

- Temperature influences creativity.
- Max Completion Tokens controls response length.
- Azure OpenAI models may support different parameters.
- API error messages often provide the exact solution.

---

# AI-102 Progress

## Skill Area

Implement Generative AI Solutions

## Concepts Covered

- Temperature
- Max Completion Tokens
- Top P
- Model Compatibility

## Exam Readiness

⭐⭐⭐⭐⭐
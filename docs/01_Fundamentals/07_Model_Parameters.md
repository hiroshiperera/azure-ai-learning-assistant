# Model Parameters

## 📘 About This Document

Large Language Models (LLMs) provide several parameters that control how responses are generated.

These parameters do not change the AI model itself. Instead, they influence how the model selects words, determines response length, and balances creativity with consistency.

Understanding these parameters is an essential skill for building Generative AI applications using Azure OpenAI and is an important topic for the AI-102 certification.

---

# Learning Objectives

After completing this topic, I should be able to:

- Explain the purpose of model parameters.
- Understand Temperature.
- Understand Max Completion Tokens.
- Understand Top P.
- Select appropriate parameter values for different applications.
- Apply model parameters when building Azure OpenAI applications.

---

# What Are Model Parameters?

Model parameters are settings supplied when making an API request.

They influence how the AI generates responses without changing the underlying model.

Example:

```python
response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=messages,
    temperature=0.2,
    max_completion_tokens=300
)
```

---

# Temperature

Temperature controls the randomness and creativity of the model.

Lower values produce more predictable and consistent responses.

Higher values produce more creative and varied responses.

---

## Low Temperature

```python
temperature = 0
```

Characteristics:

- Deterministic
- Factual
- Consistent
- Less creative

Best suited for:

- Technical documentation
- Programming
- AI-102 preparation
- Mathematics
- Enterprise applications

---

## High Temperature

```python
temperature = 1.2
```

Characteristics:

- Creative
- Varied
- Less predictable

Best suited for:

- Story writing
- Brainstorming
- Marketing
- Creative content

---

# Max Completion Tokens

Max Completion Tokens limits how many tokens the model is allowed to generate in its response.

Smaller values produce shorter responses.

Larger values allow longer and more detailed explanations.

Example:

```python
max_completion_tokens = 50
```

Produces concise answers.

Example:

```python
max_completion_tokens = 500
```

Allows detailed responses.

---

# Top P

Top P is another parameter that controls randomness by limiting the pool of candidate words.

In most applications, developers adjust either Temperature or Top P, but not both simultaneously.

For beginners, Temperature is generally sufficient.

---

# Parameter Comparison

| Parameter | Purpose | Typical Values |
|-----------|---------|---------------|
| Temperature | Controls creativity | 0.0 – 1.2 |
| Max Completion Tokens | Limits response length | 50 – 1000+ |
| Top P | Controls randomness | 0.1 – 1.0 |

---

# Choosing the Right Settings

## Technical Assistant

```python
temperature = 0.2
max_completion_tokens = 300
```

---

## AI-102 Tutor

```python
temperature = 0.2
max_completion_tokens = 500
```

---

## Creative Writer

```python
temperature = 1.0
max_completion_tokens = 800
```

---

# Model Compatibility

Different Azure OpenAI models may support different parameters.

Older models commonly used:

```python
max_tokens
```

Newer GPT-5 models use:

```python
max_completion_tokens
```

Always check the official Azure OpenAI documentation or API error messages when working with new model versions.

---

# Best Practices

- Use low Temperature for technical applications.
- Increase Max Completion Tokens only when longer responses are required.
- Avoid changing both Temperature and Top P unless necessary.
- Test different parameter values before deploying an application.

---

# Common Mistakes

- Using a high Temperature when factual accuracy is important.
- Setting Max Completion Tokens too low, causing incomplete answers.
- Assuming all Azure OpenAI models support identical parameters.
- Ignoring API compatibility messages.

---

# AI-102 Exam Notes

Remember:

- Temperature controls creativity.
- Max Completion Tokens controls response length.
- Prompt Engineering and Model Parameters work together to influence model behaviour.

---

# Key Takeaways

- Model parameters influence AI behaviour.
- Temperature controls creativity.
- Max Completion Tokens limits response length.
- Top P is another sampling parameter.
- Parameter support depends on the model version.
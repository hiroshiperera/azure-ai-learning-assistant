# 🐞 Mistakes & Problems Encountered - Day 001

## 1. Azure Subscription Issue

### Problem

Could not create a new Azure Free account.

### Cause

Microsoft did not allow creating another free Azure account because an account already existed.

### Solution

Upgraded the existing subscription to **Pay-As-You-Go**.

### Lesson Learned

Always check existing subscriptions before trying to create a new Azure account.

---

## 2. Concern About Azure Costs

### Problem

Uncertainty about unexpected Azure charges.

### Solution

Created a **USD 10 monthly budget** with alerts at:

- 50%
- 80%
- 100%

### Lesson Learned

Budgets do **not** stop resources; they only notify you when spending reaches the defined thresholds.

---

## 3. Misunderstanding Resource Groups

### Problem

Thought Resource Groups themselves would incur charges.

### Solution

Learned that:

- Resource Groups are **free**.
- Only the resources inside them (such as Azure OpenAI) may generate charges.

### Lesson Learned

Always delete unused resources to avoid unnecessary costs.

---

## 4. GPT Deployment Failed

### Problem

Initial model deployment failed.

### Cause

The selected GPT model version had been deprecated.

### Solution

Deployed **GPT-5.4-mini** instead.

### Lesson Learned

Always check which Azure OpenAI models are currently supported.

---

## 5. Python Virtual Environment

### Problem

Unsure whether to use:

- Conda
- python -m venv

### Solution

Selected:

```bash
python -m venv .venv
```

### Lesson Learned

For this project, `venv` is lightweight, simple, and suitable.

---

## 6. Virtual Environment Activation

### Problem

The virtual environment was not activated initially.

### Solution

Activated using:

```bash
.venv\Scripts\activate
```

### Lesson Learned

Always activate the virtual environment before installing packages or running the application.

---

## 7. Azure OpenAI Endpoint

### Problem

Received:

```
404 Resource Not Found
```

### Cause

Incorrect Azure endpoint configuration.

The endpoint did not include:

```
/openai/v1/
```

### Solution

Updated the endpoint to:

```
https://YOUR_RESOURCE.openai.azure.com/openai/v1/
```

### Lesson Learned

Azure OpenAI requires the `/openai/v1/` endpoint when using the current OpenAI SDK.

---

## 8. Deployment Name Confusion

### Problem

Confused the **model name** with the **deployment name**.

### Solution

Learned that the SDK uses:

```python
model=AZURE_OPENAI_DEPLOYMENT
```

where the value is the **deployment name**, not necessarily the model name.

### Lesson Learned

Resource → Deployment → Model are different concepts.

---

## 9. API Version Confusion

### Problem

Unsure where to find the Azure OpenAI API version.

### Solution

Learned that with the current OpenAI Python SDK and the `/openai/v1/` endpoint, you no longer needed to specify an API version in your code.

### Lesson Learned

Always check which SDK version you're using before following older tutorials.

---

## 10. Git First Commit

### Problem

Attempted to commit before staging files.

Git displayed:

```
nothing added to commit but untracked files present
```

### Solution

Executed:

```bash
git add .
```

before running:

```bash
git commit
```

### Lesson Learned

Git requires files to be staged before they can be committed.

---

## 11. GitHub Authentication

### Problem

Received:

```
Invalid username or token.
Password authentication is not supported.
```

### Cause

GitHub no longer supports password authentication for Git operations over HTTPS.

### Status

To be resolved by configuring GitHub authentication (browser sign-in, Git Credential Manager, or a Personal Access Token).

### Lesson Learned

Modern GitHub authentication uses secure tokens or browser-based authentication rather than account passwords.

---

## 12. Documentation Structure

### Problem

Initially designed several documentation structures and found them confusing.

### Solution

Decided to redesign the documentation around the learning journey and long-term maintainability.

### Lesson Learned

A documentation system should support learning, not create additional complexity.
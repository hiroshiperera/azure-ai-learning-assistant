# Python SDK

## Virtual Environment

A virtual environment isolates project dependencies.

Command

python -m venv .venv

---

## Why .env?

The .env file stores secrets separately from source code.

This prevents API keys from being committed to Git repositories.

---

## Why config.py?

config.py centralizes application configuration.

Other modules simply import configuration values.

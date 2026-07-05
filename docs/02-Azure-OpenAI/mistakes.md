# Troubleshooting

## Problem

GPT-4o-mini deployment failed.

Reason

Azure attempted to deploy a deprecated model version.

Solution

Deploy GPT-5.4-mini instead.

---

## Problem

404 Resource Not Found

Reason

Incorrect endpoint.

Incorrect

https://resource.openai.azure.com/

Correct

https://resource.openai.azure.com/openai/v1/

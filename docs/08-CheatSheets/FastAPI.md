# FastAPI Cheat Sheet

## Install

pip install fastapi uvicorn

---

## Run Server

uvicorn app:app --reload

---

## Swagger UI

http://127.0.0.1:8000/docs

---

## Import

from fastapi import FastAPI

---

## Create App

app = FastAPI()

---

## GET

@app.get("/")

---

## POST

@app.post("/")
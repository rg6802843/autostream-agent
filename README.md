# 🚀 AutoStream AI Agent

## 📌 Overview

This project is a conversational AI agent that converts user conversations into qualified leads for a fictional SaaS product **AutoStream**.

The agent can:

* Understand user intent
* Answer product-related queries using a knowledge base
* Identify high-intent users
* Capture leads through a structured conversational flow

---

## 🧠 Features

### ✅ Intent Detection

Classifies user input into:

* Greeting
* Inquiry
* High Intent

---

### ✅ RAG (Knowledge Retrieval)

Uses a local JSON knowledge base to answer:

* Pricing
* Features
* Policies

---

### ✅ Conversational Lead Capture

* Detects high-intent users
* Collects:

  * Name
  * Email
  * Platform
* Validates input
* Calls lead capture function

---

### ✅ Stateful Memory

Maintains conversation context using a state dictionary:

* Tracks conversation stage
* Enables multi-step interaction

---

## ⚙️ Tech Stack

* Python 3.9+
* LangChain (installed)
* JSON (knowledge base)
* FAISS (for future use)

---

## ▶️ How to Run

```bash
git clone https://github.com/rg6802843/autostream-agent.git
cd autostream-agent

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

---

## 🏗️ Architecture

User Input → Intent Detection → Router
→ Greeting / RAG / Lead Flow
→ Tool Execution (Lead Capture)

State management ensures context is preserved across multiple turns.

---

## 📱 WhatsApp Integration (Concept)

* Use WhatsApp Business API
* Connect via webhook
* Send user messages to agent
* Return responses back to WhatsApp

Flow:
WhatsApp → Webhook → Agent → Response → WhatsApp

---

## 🎥 Demo

The agent demonstrates:

* Answering pricing queries
* Detecting high-intent users
* Collecting user details
* Capturing leads successfully

---

## 🚀 Future Improvements

* Use LLM-based intent detection
* Add vector search for RAG
* Deploy as API or chatbot UI

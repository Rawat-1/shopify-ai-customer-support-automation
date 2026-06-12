# Shopify AI Customer Support Automation

## Overview

Shopify AI Customer Support Automation is an AI-powered workflow designed to automate customer support operations for eCommerce businesses. The system classifies customer support tickets, analyzes sentiment, determines escalation requirements, retrieves relevant company policies, and generates context-aware customer responses.

The solution was developed as a Proof of Concept (POC) to demonstrate how Generative AI can be integrated into customer support workflows while maintaining reliability through business rules, Retrieval-Augmented Generation (RAG), and human escalation mechanisms.

---

## Problem Statement

Customer support teams spend significant time handling repetitive requests such as:

* Refund inquiries
* Shipping status requests
* Damaged product complaints
* Replacement requests
* General policy questions

Manual processing increases operational costs and response times.

This project automates the initial analysis and response generation process while ensuring high-risk cases are escalated for human review.

---

## Features

### AI Ticket Classification

Automatically classifies customer tickets based on:

* Priority (High, Medium, Low)
* Intent Detection
* Sentiment Analysis
* Escalation Requirement

### Business Rules Engine

Applies predefined business logic such as:

* Refund requests above $500 require human review
* Damaged product complaints require escalation
* High-risk tickets are routed to human agents

### Retrieval-Augmented Generation (RAG)

Retrieves company policies from a knowledge source before generating responses.

Current knowledge source:

```text
store_policies.txt
```

This reduces hallucinations and ensures responses remain aligned with company policies.

### AI Response Generation

Generates professional customer support responses using Gemini.

### REST API

Exposes functionality through a FastAPI endpoint:

```http
POST /ticket
```

### Error Handling

Handles:

* API quota exhaustion
* Service unavailability
* Invalid model outputs
* Missing policy files

When AI services are unavailable, requests are safely routed for human review.

---

## Architecture

```text
Customer Support Ticket
          │
          ▼
      FastAPI API
          │
          ▼
  Ticket Classification
     (Gemini API)
          │
          ▼
 Business Rules Engine
(Escalate / Auto Respond)
          │
     ┌────┴────┐
     │         │
     ▼         ▼
Human Review  Policy Retrieval
                 (RAG)
                    │
                    ▼
         Store Policies
         (store_policies.txt)
                    │
                    ▼
        Response Generator
           (Gemini API)
                    │
                    ▼
             JSON Response
```

---

## Technology Stack

| Component              | Technology             |
| ---------------------- | ---------------------- |
| Backend API            | FastAPI                |
| AI Model               | Google Gemini          |
| RAG Layer              | Local Policy Retrieval |
| Programming Language   | Python                 |
| Environment Management | python-dotenv          |
| API Documentation      | Swagger UI             |

---

## Project Structure

```text
shopify-ai-support/
│
├── api.py
├── classifier.py
├── response_generator.py
├── rag.py
├── main.py
│
├── data/
│   └── store_policies.txt
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .env.example
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd shopify-ai-support
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Generate an API key from Google AI Studio.

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn api:app --reload
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Example

### Request

```http
POST /ticket
```

```json
{
  "ticket": "I would like a refund. What is your refund policy?"
}
```

### Response

```json
{
  "classification": {
    "priority": "Medium",
    "intent": "Refund Inquiry",
    "sentiment": "Neutral",
    "escalate": false
  },
  "action": "Auto Respond",
  "response": "Customers may request refunds within 17 days of purchase."
}
```

---

## Cost Analysis

| Component             | Estimated Cost          |
| --------------------- | ----------------------- |
| FastAPI               | Free                    |
| Python                | Free                    |
| Local Storage         | Free                    |
| Gemini API            | Free Tier / Usage Based |
| Deployment (Optional) | $5–10/month             |

---

## Risks and Limitations

### API Quotas

Free-tier Gemini APIs may experience rate limits or quota restrictions.

### Service Availability

Cloud AI services may occasionally experience downtime or high-demand periods.

### Hallucinations

Although reduced through RAG, hallucinations remain a potential risk in generative AI systems.

### Static Knowledge Source

The current implementation uses a text-based policy file and does not yet support dynamic policy updates.

---

## Future Improvements

* ChromaDB-based vector search
* Shopify webhook integration
* Multi-agent workflows
* CRM integration
* Human-in-the-loop approval workflows
* Conversation memory
* Multi-language support
* Cloud deployment

---

## Conclusion

This project demonstrates how AI can automate customer support workflows by combining ticket classification, business rules, retrieval-augmented generation, and response generation into a single production-oriented workflow. The architecture provides a scalable foundation for future deployment within Shopify and eCommerce support environments.

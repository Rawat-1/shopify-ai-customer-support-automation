from fastapi import FastAPI
from pydantic import BaseModel

from classifier import classify_ticket
from response_generator import generate_reply

app = FastAPI()


class TicketRequest(BaseModel):
    ticket: str

@app.get("/")
def home():
    return {
        "project": "Shopify AI Customer Support Automation",
        "status": "Running",
        "version": "1.0"
    }

@app.post("/ticket")
def process_ticket(data: TicketRequest):

    ticket = data.ticket

    classification = classify_ticket(ticket)

    if classification.get("error"):
        action = "Human Review Required"
    else:
        action = (
        "Escalate to Human Agent"
        if classification["escalate"]
        else "Auto Respond"
    )

    response = generate_reply(ticket)

    return {
        "classification": classification,
        "action": action,
        "response": response
    }
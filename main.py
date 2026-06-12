from classifier import classify_ticket
from response_generator import generate_reply

ticket = """
I would like a refund.
What is your refund policy?
"""

print("\n==============================")
print("SHOPIFY AI SUPPORT ASSISTANT")
print("==============================")

classification = classify_ticket(ticket)

print("\n=== CLASSIFICATION ===")
print(classification)

if classification.get("error"):

    print("\n=== SYSTEM STATUS ===")
    print("AI Service Unavailable")

    print("\n=== ERROR ===")
    print(classification["error"])

else:

    print("\n=== ACTION ===")

    if classification["escalate"]:
        print("Escalate to Human Agent")
    else:
        print("Auto Respond")

    print("\n=== RESPONSE ===")

    reply = generate_reply(ticket)

    print(reply)
from classifier import classify_ticket
from response_generator import generate_reply

ticket = """
My order hasn't arrived after 12 days.
I would like a refund.
"""

classification = classify_ticket(ticket)

print("\nCLASSIFICATION")
print(classification)

print("\nRESPONSE")
print(generate_reply(ticket))
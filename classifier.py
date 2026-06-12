import os
import json
from google import genai
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def classify_ticket(ticket):

    prompt = f"""
You are a Shopify customer support ticket classifier.

Business Rules:

- Refund requests above $500 must be escalated.
- Damaged products should be escalated.
- Extremely negative customers should be escalated.

Return ONLY valid JSON.

Schema:

{{
  "priority": "High|Medium|Low",
  "intent": "string",
  "sentiment": "Positive|Neutral|Negative",
  "escalate": true/false
}}

Ticket:
{ticket}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "").strip()

        return json.loads(text)

    except json.JSONDecodeError as e:
        print(f"JSON Parsing Error: {e}")

        return {
            "priority": "Unknown",
            "intent": "Unknown",
            "sentiment": "Unknown",
            "escalate": True,
            "error": "Invalid JSON returned by model"
        }

    except Exception as e:
        print(f"Classification Error: {e}")

        return {
            "priority": "Unknown",
            "intent": "Unknown",
            "sentiment": "Unknown",
            "escalate": True,
            "error": str(e)
        }
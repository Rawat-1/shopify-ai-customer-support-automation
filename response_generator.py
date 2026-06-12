import os
from google import genai
from dotenv import load_dotenv
from rag import get_policy_context

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_reply(ticket):

    policies = get_policy_context()

    prompt = f"""
You are a Shopify customer support representative.

Store Policies:

{policies}

Use ONLY the policies above when answering.

Do NOT use placeholders such as:
[Your Name]
[Company Name]
[Store Name]

Sign every response with:

Shopify AI Support Team

Customer Ticket:

{ticket}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return (
        f"AI_SERVICE_UNAVAILABLE: {str(e)}"
    )
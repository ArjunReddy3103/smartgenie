import os
import requests

PERPLEXITY_API_KEY = os.environ.get("PERPLEXITY_API_KEY")
PERPLEXITY_MODEL = "sonar-pro"
PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"

def ask_ai(prompt: str) -> str:
    try:
        if not PERPLEXITY_API_KEY:
            return "[ERROR] API key not provided. Set PERPLEXITY_API_KEY environment variable."

        messages = [
            {
                "role": "system",
                "content": (
                    "You are StartGenieBot, an expert assistant helping startup founders with ideation, "
                    "product planning, marketing, and execution strategy.\n"
                    "Whenever the user's request has several aspects, steps, or options, respond using "
                    "clear bullet points or numbered lists in markdown, so your answers are easy to scan."
                )
            },
            {"role": "user", "content": prompt}
        ]

        payload = {
            "model": PERPLEXITY_MODEL,
            "messages": messages,
            "max_tokens": 500
        }

        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(PERPLEXITY_URL, headers=headers, json=payload)
        response.raise_for_status()
        reply = response.json().get("choices", [{}])[0].get("message", {}).get("content", "").strip()

        return reply

    except Exception as e:
        return f"[ERROR] {str(e)}"

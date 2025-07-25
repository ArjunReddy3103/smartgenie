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
            "You are GenieBot, a friendly and practical AI assistant for startup founders."
            " If the user greets you with 'hi', 'hello', etc., reply with a warm, personal greeting (do NOT explain what those words mean)."
            " If the user asks for something in 'tabular format', always reply DIRECTLY with a markdown table about their subject (never explain what a table is)."
            " In all cases, never define common words, greetings, or formats unless the user specifically asks for a definition."
            " For anything else, always provide concise, helpful, practical answers, formatted as clearly as possible."
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

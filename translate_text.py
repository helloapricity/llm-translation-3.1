"""
translate_text.py
A simple translator script using the OpenAI Chat Completions API.
Designed for Assignment 3.1: input a string + destination language,
return the translated string only.
"""

from openai import OpenAI
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from a .env file (this is where the API key is stored)
load_dotenv()

# Initialize the OpenAI client using the API key from the environment.
# This keeps your API key secure and out of the code itself.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Small mapping of common language codes to their full names.
# This allows the user to pass either a language code ("vi") or the full name ("Vietnamese").
LANG_MAP = {
    "vi": "Vietnamese",
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    # Add more as needed.
}

def _language_name(code_or_name: str) -> str:
    """
    Convert a language code (like 'vi') to its full name ('Vietnamese')
    using the LANG_MAP. If the input is already a full language name,
    return it unchanged.
    """
    code_or_name = code_or_name.strip()
    if len(code_or_name) <= 3 and code_or_name.lower() in LANG_MAP:
        return LANG_MAP[code_or_name.lower()]
    return code_or_name  # assume the full language name is provided already

def translate_text(text: str, dest_language: str, client: Optional[OpenAI]=None) -> str:
    """
    Translate a single text string into the destination language.

    Parameters:
        text (str): The input string to translate.
        dest_language (str): Target language (can be a code 'vi' or full name 'Vietnamese').
        client (Optional[OpenAI]): Optional custom OpenAI client (useful for testing).

    Returns:
        str: The translated text only (no explanations or additional content).
    """
    # If no client is explicitly passed, use the global client defined above.
    if client is None:
        client = globals().get("client")

    # Normalize the destination language to a full name (e.g., 'vi' → 'Vietnamese').
    lang_name = _language_name(dest_language)

    # Build the prompt that instructs the model to translate and return only the translation.
    prompt = (
        f"Translate the following text into {lang_name}.\n\n"
        f"Text: \"{text}\"\n\n"
        "Important: Respond ONLY with the translated text and nothing else "
        "(no explanations, no extra punctuation)."
    )

    try:
        # Send the translation request to the OpenAI Chat Completions API.
        resp = client.chat.completions.create(
            model="gpt-4o-mini",  # Model to use; can be replaced with another.
            messages=[
                {"role": "system", "content": "You are a concise, professional translator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,  # Make output as deterministic as possible.
        )
    except Exception as e:
        # Raise an explicit error if the API call fails (useful for debugging/assignment).
        raise RuntimeError(f"API request failed: {e}")

    # Extract the translated text from the API response and strip extra whitespace.
    translated = resp.choices[0].message.content.strip()
    return translated

if __name__ == "__main__":
    # Quick local demo to show how the function works.
    # (This should NOT include any sensitive information like your API key.)
    import json
    demo = {"text": "Hello", "dest_language": "vi"}
    out = translate_text(demo["text"], demo["dest_language"])
    print(out)  # Prints the translated result (e.g., "Xin chào")
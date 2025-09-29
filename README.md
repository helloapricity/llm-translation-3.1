# LLM Translation – Assignment 3.1

## Overview
This repository contains a simple Python script that uses the OpenAI Chat Completions API 
to translate a single text string into a target language. 
It is designed for Assignment 3.1 for the AI Engineer application. 

The script ensures that only the translated text is returned, without any additional explanations or formatting.

---

## Features
- Translate a single string from any language to the specified target language.
- Accepts both language codes (e.g., "vi") and full language names (e.g., "Vietnamese").
- Supports deterministic output by setting `temperature=0` in API calls.
- Easy to extend for additional languages.

---

## Requirements
- Python 3.10+  
- OpenAI Python SDK (`openai`)  
- `python-dotenv` for loading API keys from a `.env` file (recommended)  

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Setup
1. Create a `.env` file in the project root with your OpenAI API key:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```
2. Ensure `.env` is included in `.gitignore` to keep your API key secure.

---

## Usage
Run the script from the project root:
```bash
python translate_text.py
```
By default, it will translate `"Hello"` to Vietnamese (`"vi"`).
You can modify the `demo` dictionary in the `__main__` block to test other texts or target languages.

---

## Running Tests
Unit tests are included in the `tests/` folder and mock the API for safe testing:
```bash
pytest -q
```
All tests should pass, ensuring that `translate_text()` returns the expected results.

---

## Design Notes
- The script uses `chat.completions.create` with a system prompt to ensure concise translations.
- The language mapping allows short codes or full names to be used interchangeably.
- The `client` parameter in `translate_text()` allows injection of a custom OpenAI client, which is useful for unit testing.
- Errors from the API are explicitly caught and raised to help with debugging.

---

## Future Improvements
- Support batch translation for multiple texts.
- Add automatic language detection for source language.
- Implement caching to reduce API usage costs.
- Extend language mapping to include more languages and variants.
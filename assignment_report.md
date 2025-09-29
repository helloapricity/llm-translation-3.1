Objective:
  Implement a translator for a single text using OpenAI Chat API.

Approach:
  - Use chat completions with a system prompt "You are a concise translator."
  - Force output to be only the translated string for deterministic parsing.
  - Accept both language codes and full language names.

Tests:
  - unit tests mock API and confirm outputs for "Hello" -> "Xin chào".

Limitations:
  - No auto language detection.
  - Costs scale linearly per request (for production, batch multiple texts or use cheaper model if suitable).

Future work:
  - Add batching, rate-limiting, caching, and more complete language mapping.
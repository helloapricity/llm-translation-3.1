# tests/test_translate.py
from translate_text import translate_text

# Create simple fake client that mimics client.chat.completions.create
class DummyCompletions:
    def __init__(self, resp_text):
        self._resp_text = resp_text
    def create(self, **kwargs):
        # mimic response object structure used in translate_text
        return type("Resp", (), {
            "choices": [type("C", (), {"message": type("M", (), {"content": self._resp_text})})]
        })

class DummyChat:
    def __init__(self, resp_text):
        self.completions = DummyCompletions(resp_text)

class DummyClient:
    def __init__(self, resp_text):
        self.chat = DummyChat(resp_text)

def test_translate_text_basic():
    fake = DummyClient("Xin chào")
    out = translate_text("Hello", "Vietnamese", client=fake)
    assert out == "Xin chào"

def test_translate_text_code_input():
    fake = DummyClient("Xin chào")
    # allow 'vi' as input
    out2 = translate_text("Hello", "vi", client=fake)
    assert out2 == "Xin chào"
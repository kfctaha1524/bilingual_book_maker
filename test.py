import pytest


from book_maker.translator.chatgptapi_translator import ChatGPTAPI

def test_translation():
    key = "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"

    # Create an instance of the ChatGPT class
    chatbot = ChatGPTAPI(key)

    # Test the translation function
    result = chatbot.translate("Hello, how are you?")
    assert result == "你好，你好吗？"

if __name__ == "__main__":
    test_translation()

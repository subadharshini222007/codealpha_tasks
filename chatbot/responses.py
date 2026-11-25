"""
SmartDesk - Chatbot Response Database

This file stores predefined keywords and responses.
The chatbot uses these responses to answer user messages.
"""

import random

BOT_NAME = "SmartDesk"

RESPONSES = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "replies": [
            "Hello! Welcome to SmartDesk. How can I help you?",
            "Hi there! What would you like to know?",
            "Hey! I am SmartDesk, your virtual assistant."
        ]
    },

    "how_are_you": {
        "keywords": ["how are you", "how are you doing", "are you fine"],
        "replies": [
            "I am doing great! Thank you for asking.",
            "I am fine and ready to assist you.",
            "All systems are working well!"
        ]
    },

    "name": {
        "keywords": ["your name", "who are you", "what are you"],
        "replies": [
            "I am SmartDesk, a rule-based chatbot developed using Python."
        ]
    },

    "python": {
        "keywords": ["what is python", "python"],
        "replies": [
            "Python is a popular, high-level programming language known for its simple syntax."
        ]
    },

    "capabilities": {
        "keywords": ["what can you do", "your features", "your capabilities"],
        "replies": [
            "I can answer basic questions, respond to greetings, "
            "provide simple information, and maintain conversation history."
        ]
    },

    "thanks": {
        "keywords": ["thank you", "thanks", "thank"],
        "replies": [
            "You're welcome! Happy to help.",
            "Glad I could help!",
            "It's my pleasure!"
        ]
    },

    "help": {
        "keywords": ["help", "commands", "what should i ask"],
        "replies": [
            "You can ask me about Python, my name, my features, "
            "or simply greet me. Type 'bye' to end the conversation."
        ]
    },

    "goodbye": {
        "keywords": ["bye", "goodbye", "exit", "quit"],
        "replies": [
            "Goodbye! Thank you for chatting with SmartDesk.",
            "See you again! Have a wonderful day.",
            "Conversation ended. Take care!"
        ]
    }
}

FALLBACK_RESPONSES = [
    "I am not sure I understood that. Could you rephrase your question?",
    "Sorry, I don't have an answer for that yet. Try asking something else.",
    "I am still learning predefined responses. Please ask me another question."
]


def get_random_response(responses):
    """Return one random response from the given response list."""
    return random.choice(responses)

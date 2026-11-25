
"""
SmartDesk - Rule-Based Chatbot Engine

Uses if-elif conditions, functions and predefined replies.
"""

from chatbot.responses import RESPONSES, FALLBACK_RESPONSES
from chatbot.responses import get_random_response

def normalize_input(user_input):
    """Convert user input into lowercase and remove extra spaces."""
    return " ".join(user_input.lower().strip().split())

def get_response(user_input):
    """Generate a predefined response based on user input."""

    message = normalize_input(user_input)

    if not message:
        return "Please enter a message.", False

    # Greeting
    if message in ["hello", "hi", "hey", "hii", "good morning", "good evening"]:
        response = get_random_response(RESPONSES["greeting"]["replies"])

    # How are you
    elif message in ["how are you", "how are you doing", "are you fine"]:
        response = get_random_response(RESPONSES["how_are_you"]["replies"])

    # Chatbot name
    elif message in ["your name", "what is your name", "who are you"]:
        response = get_random_response(RESPONSES["name"]["replies"])

    # Python information
    elif message in ["python", "what is python", "tell me about python"]:
        response = get_random_response(RESPONSES["python"]["replies"])

    # Chatbot capabilities
    elif message in ["what can you do", "your features", "your capabilities"]:
        response = get_random_response(RESPONSES["capabilities"]["replies"])

    # Thank you
    elif message in ["thank you", "thanks", "thank"]:
        response = get_random_response(RESPONSES["thanks"]["replies"])

    # Help
    elif message in ["help", "commands", "what should i ask"]:
        response = get_random_response(RESPONSES["help"]["replies"])

    # Goodbye
    elif message in ["bye", "goodbye", "exit", "quit"]:
        response = get_random_response(RESPONSES["goodbye"]["replies"])
        return response, True

    # Unknown input
    else:
        response = get_random_response(FALLBACK_RESPONSES)

    return response, False

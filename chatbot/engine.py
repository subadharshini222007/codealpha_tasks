
"""
SmartDesk - Intelligent Rule-Based Chatbot

Handles user input and generates predefined responses
using keyword matching and if-elif conditions.
"""

import re

from chatbot.responses import (
    RESPONSES,
    FALLBACK_RESPONSES,
    get_random_response
)


def normalize_input(user_input):
    """Convert input to lowercase and remove extra spaces."""
    return " ".join(user_input.lower().strip().split())


def matches_keyword(message, keywords):
    """Check whether the message contains any given keyword."""

    for keyword in keywords:
        keyword = keyword.lower().strip()

        pattern = r"\b" + re.escape(keyword) + r"\b"

        if re.search(pattern, message):
            return True

    return False


def get_response(user_input):
    """
    Generate a chatbot response.

    Returns:
        response: Chatbot reply
        should_exit: True when the user wants to end the chat
    """

    message = normalize_input(user_input)

    if not message:
        return "Please enter a message.", False

    # Greeting
    if (
        matches_keyword(message, RESPONSES["greeting"]["keywords"])
        or matches_keyword(message, ["hii"])
    ):
        response = get_random_response(
            RESPONSES["greeting"]["replies"]
        )
        return response, False

    # How are you
    elif matches_keyword(
        message,
        RESPONSES["how_are_you"]["keywords"]
    ):
        response = get_random_response(
            RESPONSES["how_are_you"]["replies"]
        )
        return response, False

    # Chatbot name
    elif matches_keyword(
        message,
        RESPONSES["name"]["keywords"]
    ):
        response = get_random_response(
            RESPONSES["name"]["replies"]
        )
        return response, False

    # Python information
    elif matches_keyword(
        message,
        RESPONSES["python"]["keywords"]
    ):
        response = get_random_response(
            RESPONSES["python"]["replies"]
        )
        return response, False

    # Chatbot capabilities
    elif matches_keyword(
        message,
        RESPONSES["capabilities"]["keywords"]
    ):
        response = get_random_response(
            RESPONSES["capabilities"]["replies"]
        )
        return response, False

    # Thank you
    elif matches_keyword(
        message,
        RESPONSES["thanks"]["keywords"]
    ):
        response = get_random_response(
            RESPONSES["thanks"]["replies"]
        )
        return response, False

    # Help
    elif matches_keyword(
        message,
        RESPONSES["help"]["keywords"]
    ):
        response = get_random_response(
            RESPONSES["help"]["replies"]
        )
        return response, False

    # Goodbye
    elif matches_keyword(
        message,
        RESPONSES["goodbye"]["keywords"]
    ):
        response = get_random_response(
            RESPONSES["goodbye"]["replies"]
        )
        return response, True

    # Unknown input
    else:
        response = get_random_response(FALLBACK_RESPONSES)
        return response, False

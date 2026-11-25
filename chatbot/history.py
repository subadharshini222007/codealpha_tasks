"""
SmartDesk - Conversation History Manager

Stores chatbot conversations in JSON format.
"""

import json
from datetime import datetime
from pathlib import Path


# Project data folder
DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"

# Conversation history file
HISTORY_FILE = DATA_FOLDER / "chat_history.json"


def save_message(sender, message):
    """Save one conversation message with date and time."""

    DATA_FOLDER.mkdir(parents=True, exist_ok=True)

    history = load_history()

    entry = {
        "sender": sender,
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    history.append(entry)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


def load_history():
    """Load previously saved conversation history."""

    if not HISTORY_FILE.exists():
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)

        if isinstance(history, list):
            return history

        return []

    except (json.JSONDecodeError, OSError):
        return []


def clear_history():
    """Clear all saved conversation history."""

    DATA_FOLDER.mkdir(parents=True, exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)

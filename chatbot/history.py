
"""
SmartDesk - Conversation History Manager

Stores conversation history and calculates statistics.
"""

import json
from datetime import datetime
from pathlib import Path


DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"
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


def get_statistics():
    """Calculate conversation statistics."""

    history = load_history()

    total_messages = len(history)
    user_messages = 0
    chatbot_messages = 0

    for entry in history:
        sender = entry.get("sender", "").strip().lower()

        if sender == "smartdesk":
            chatbot_messages += 1
        else:
            user_messages += 1

    return {
        "total_messages": total_messages,
        "user_messages": user_messages,
        "chatbot_messages": chatbot_messages
    }

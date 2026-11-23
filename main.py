
"""
SmartDesk - Intelligent Rule-Based Chatbot

Main application file.
Connects chatbot engine and conversation history.
"""

from chatbot.engine import get_response
from chatbot.history import (
    save_message,
    load_history,
    get_statistics
)


def display_welcome():
    """Display the chatbot welcome screen."""

    print("\n" + "=" * 55)
    print("                 SMARTDESK CHATBOT")
    print("          Your Personal Virtual Assistant")
    print("=" * 55)

    print("\nWelcome! I am SmartDesk.")
    print("I am here to answer your basic questions.")


def display_commands():
    """Display available chatbot commands."""

    print("\n========== AVAILABLE COMMANDS ==========")
    print("help      - Display available commands")
    print("history   - View previous conversations")
    print("stats     - View conversation statistics")
    print("bye       - End the conversation")
    print("========================================")


def display_history():
    """Display saved conversation history."""

    history = load_history()

    print("\n========== CHAT HISTORY ==========")

    if not history:
        print("No conversation history available.")
        return

    for entry in history:
        sender = entry.get("sender", "Unknown")
        message = entry.get("message", "")
        timestamp = entry.get("timestamp", "")

        print(f"\n[{timestamp}] {sender}: {message}")

    print("\n==================================")


def display_statistics():
    """Display conversation statistics."""

    stats = get_statistics()

    print("\n======= CONVERSATION STATISTICS =======")
    print(f"Total Messages   : {stats['total_messages']}")
    print(f"User Messages    : {stats['user_messages']}")
    print(f"Chatbot Messages : {stats['chatbot_messages']}")
    print("=======================================")


def start_chat():
    """Start the chatbot conversation."""

    display_welcome()

    user_name = input("\nEnter your name: ").strip()

    if not user_name:
        user_name = "User"

    print(f"\nHello {user_name}! Let's start chatting.")
    display_commands()

    while True:

        user_input = input(f"\n{user_name}: ").strip()

        if not user_input:
            print("SmartDesk: Please enter a message.")
            continue

        command = user_input.lower().strip()

        # Help command
        if command in ["help", "commands"]:
            display_commands()
            continue

        # History command
        elif command == "history":
            display_history()
            continue

        # Statistics command
        elif command == "stats":
            display_statistics()
            continue

        # Normal chatbot conversation
        save_message(user_name, user_input)

        response, should_exit = get_response(user_input)

        print(f"\nSmartDesk: {response}")

        save_message("SmartDesk", response)

        # Exit conversation
        if should_exit:
            print("\nThank you for using SmartDesk!")
            break


if __name__ == "__main__":
    start_chat()

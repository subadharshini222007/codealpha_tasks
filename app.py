
import streamlit as st
import csv
import io

from chatbot.engine import get_response
from chatbot.history import save_message, load_history, get_statistics


# --------------------------------------------------
# CSV EXPORT FUNCTION
# --------------------------------------------------

def export_chat_history(history):
    output = io.StringIO()

    fieldnames = ["sender", "message", "timestamp"]

    writer = csv.DictWriter(
        output,
        fieldnames=fieldnames,
        extrasaction="ignore"
    )

    writer.writeheader()

    for item in history:
        writer.writerow({
            "sender": item.get("sender", ""),
            "message": item.get("message", ""),
            "timestamp": item.get("timestamp", "")
        })

    return output.getvalue().encode("utf-8-sig")


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="SmartDesk | Virtual Assistant",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #f4f6fb;
}

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #243b67;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #68758b;
    font-size: 16px;
    margin-bottom: 30px;
}

.welcome-card {
    background: linear-gradient(120deg, #243b67, #526fa8);
    padding: 30px;
    border-radius: 18px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.welcome-card h2 {
    color: white;
}

div[class*="st-key-assistant_message_"] {
    background-color: #E8EEF8 !important;
    border: 1px solid #CBD7EE !important;
    border-radius: 14px !important;
    padding: 12px 15px !important;
    margin-bottom: 12px !important;
}

div[class*="st-key-assistant_message_"] p,
div[class*="st-key-assistant_message_"] li {
    color: #243B67 !important;
}

div[class*="st-key-assistant_message_"] [data-testid="stChatMessage"] {
    background-color: transparent !important;
}

div[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) {
    background-color: #ffffff !important;
    border-radius: 14px;
    padding: 12px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! Welcome to SmartDesk. "
                "I am your virtual assistant. "
                "How can I help you today?"
            )
        }
    ]


if "user_name" not in st.session_state:

    st.session_state.user_name = "Guest"


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("💬 SmartDesk")

    st.write("Your Personal Virtual Assistant")

    st.divider()

    st.subheader("👤 User Profile")

    user_name = st.text_input(
        "Enter your name",
        value=st.session_state.user_name
    )

    if user_name.strip():
        st.session_state.user_name = user_name.strip()

    st.divider()

    st.subheader("⚙️ Chat Options")

    if st.button(
        "🗑️ Clear Current Chat",
        use_container_width=True
    ):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello! Welcome back to SmartDesk. "
                    "How can I help you?"
                )
            }
        ]

        st.rerun()

    st.divider()

    # PREVIOUS CONVERSATIONS

    st.subheader("📚 Previous Conversations")

    previous_history = load_history()

    if previous_history:

        for item in previous_history[-8:]:

            st.caption(
                f"{item.get('sender', 'Unknown')}: "
                f"{item.get('message', '')}"
            )

    else:

        st.info("No previous conversations available.")

    st.divider()

    # EXPORT CHAT HISTORY

    st.subheader("📥 Export Chat History")

    if previous_history:

        csv_data = export_chat_history(previous_history)

        st.download_button(
            label="⬇️ Download Chat History",
            data=csv_data,
            file_name="SmartDesk_Chat_History.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.caption(
            f"{len(previous_history)} messages available for export."
        )

    else:

        st.info("No chat history available to export.")

    st.divider()

    st.caption("SmartDesk | Rule-Based Chatbot")


# --------------------------------------------------
# MAIN DASHBOARD
# --------------------------------------------------

st.markdown(
    '<div class="main-title">💬 SmartDesk</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Intelligent Rule-Based Virtual Assistant'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# WELCOME CARD
# --------------------------------------------------

st.markdown(
    f"""
    <div class="welcome-card">
        <h2>Welcome to SmartDesk!</h2>
        <p>Hello {st.session_state.user_name},</p>
        <p>Your personal virtual assistant is ready to help you.</p>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# CHAT INTERFACE
# --------------------------------------------------

st.subheader("💬 Start Conversation")

st.write(
    "Ask a question or select one of the supported topics."
)


# --------------------------------------------------
# DISPLAY CONVERSATION MESSAGES
# --------------------------------------------------

for index, message in enumerate(st.session_state.messages):

    if message["role"] == "assistant":

        with st.container(key=f"assistant_message_{index}"):

            with st.chat_message("assistant"):

                st.markdown(message["content"])

    else:

        with st.chat_message("user"):

            st.markdown(message["content"])


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

user_input = st.chat_input(
    "Type your message here..."
)


# --------------------------------------------------
# PROCESS USER MESSAGE
# --------------------------------------------------

if user_input:

    user_input = user_input.strip()

    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # STATISTICS COMMAND

        if user_input.lower() == "stats":

            statistics = get_statistics()

            response = (
                "### 📊 Conversation Statistics\n\n"
                "---\n\n"
                f"**Total Messages:** "
                f"{statistics['total_messages']}\n\n"
                f"**User Messages:** "
                f"{statistics['user_messages']}\n\n"
                f"**SmartDesk Responses:** "
                f"{statistics['chatbot_messages']}\n\n"
                "---"
            )

        else:

            save_message(
                st.session_state.user_name,
                user_input
            )

            response, should_exit = get_response(user_input)

            if should_exit:

                response += (
                    "\n\nYou can start a new conversation "
                    "whenever you like."
                )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        if user_input.lower() != "stats":

            save_message(
                "SmartDesk",
                response
            )

        st.rerun()


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    "<center>Developed using Python and Streamlit</center>",
    unsafe_allow_html=True
)

"""Chat-list view logic for Streamlit WhatsApp-style chat app."""

import hashlib
import streamlit as st
from conversation_view import switch_to_conversation


def chat_list_view():
    st.title("💬 Chats")
    GROUP_ICON = "👥"
    USER_ICON = "🙂"
    for CHAT_NAME, MSGS in st.session_state.history.items():
        # Choose icon based on chat name
        ICON = GROUP_ICON if CHAT_NAME == "Work Group" else USER_ICON
        # Show last message or placeholder
        PREVIEW = MSGS[-1]["content"] if MSGS else "No messages yet"
        # Markdown label: icon, name, preview
        LABEL = f"{ICON} **{CHAT_NAME}**  \n{PREVIEW}"
        # Safe key for button
        SAFE_KEY = f"btn_{hashlib.md5(CHAT_NAME.encode()).hexdigest()}"
        if st.button(LABEL, use_container_width=True, key=SAFE_KEY):
            switch_to_conversation(CHAT_NAME)

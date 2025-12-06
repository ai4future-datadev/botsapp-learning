"""Streamlit WhatsApp-style chat app."""

import streamlit as st
from login import login
from chat_list_view import chat_list_view
from conversation_view import conversation_view
from css_patch import apply_css_patch

st.set_page_config(page_title="BotsLearn", layout="wide")

# User login
login()


# Session-state initialisation
if "history" not in st.session_state:
    st.session_state.history = {
        "Alice": [{"role": "assistant", "content": "Hello!"}],
        "Work Group": [{"role": "assistant", "content": "Meeting at 2?"}],
        "Project X": [],
    }
if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Alice"
if "view" not in st.session_state:
    st.session_state.view = "chat_list"  # or "conversation"


# Apply CSS patch for left-aligned chat buttons
apply_css_patch()


# Chatlist view
if st.session_state.view == "chat_list":
    chat_list_view()


# Conversation view
else:
    conversation_view()

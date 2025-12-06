"""Conversation view logic for Streamlit WhatsApp-style chat app."""

import streamlit as st


def switch_to_conversation(chat_name: str):
    """Switches the view to the selected conversation and reruns the app."""
    st.session_state.current_chat = chat_name
    st.session_state.view = "conversation"
    st.rerun()


def conversation_view():
    st.header(f"Chat with {st.session_state.current_chat}")
    if st.button("⬅️ Back to chats", use_container_width=True):
        st.session_state.view = "chat_list"
        st.rerun()

    for msg in st.session_state.history[st.session_state.current_chat]:
        with st.chat_message(
            msg["role"],
            avatar=msg.get("avatar", "🙂" if msg["role"] == "user" else "🤖"),
        ):
            st.write(msg["content"])

    def submit_message():
        """Append user and assistant messages to chat history."""
        txt = st.session_state["chat_input"]
        st.session_state.history[st.session_state.current_chat] += [
            {"role": "user", "content": txt, "avatar": "🙂"},
            {"role": "assistant", "content": f"Echo: {txt}", "avatar": "🤖"},
        ]

    st.chat_input(
        "Type a message…",
        key=f"chat_input_{st.session_state.current_chat}",
        on_submit=submit_message,
    )

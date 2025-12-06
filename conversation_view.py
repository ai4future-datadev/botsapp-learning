"""Conversation view logic for Streamlit WhatsApp-style chat app."""

import streamlit as st


def switch_to_conversation(chat_name: str):
    """Switches the view to the selected conversation and reruns the app."""
    st.session_state.current_chat = chat_name
    st.session_state.view = "conversation"
    st.rerun()


def conversation_view():
    """Renders the conversation view."""
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

    # Read the input value returned by st.chat_input (no widget key / no value=)
    # st.chat_input returns the submitted string only when the user submits.
    txt = st.chat_input("Type a message…")
    if txt:
        st.session_state.history[st.session_state.current_chat] += [
            {"role": "user", "content": txt, "avatar": "🙂"},
            {"role": "assistant", "content": f"Echo: {txt}", "avatar": "🤖"},
        ]
        # No need to assign to widget-managed keys; the return-handling above is enough.
        # Rerun is optional since writing to session_state triggers a rerun.
        st.rerun()

    # Example: present a multiple choice question
    question = "Do you want to continue?"
    options = ["Yes", "No", "Maybe"]

    st.write(f"🤖 {question}")
    cols = st.columns(len(options))
    for idx, option in enumerate(options):
        if cols[idx].button(option, key=f"option_{option}"):
            # Append user's answer to chat history
            st.session_state.history[st.session_state.current_chat].append(
                {"role": "user", "content": option, "avatar": "🙂"}
            )
            # Optionally, append assistant's response
            st.session_state.history[st.session_state.current_chat].append(
                {"role": "assistant", "content": f"You chose: {option}", "avatar": "🤖"}
            )
            st.rerun()

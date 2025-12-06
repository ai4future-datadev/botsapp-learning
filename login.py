"""Login logic for Streamlit WhatsApp-style chat app."""

import streamlit as st


def login():
    with st.sidebar:
        st.title("🔐 User Login")
        username = st.text_input("Username", key="login_username", value="alice")
        password = st.text_input(
            "Password", type="password", key="login_password", value="wonderland123"
        )
        login_btn = st.button("Login", key="login_btn")
        # Retrieve valid users from Streamlit secrets
        valid_users = st.secrets.get("users", {})
        if login_btn:
            if username and password:
                if username in valid_users and valid_users[username] == password:
                    st.session_state["logged_in_user"] = username
                    st.success(f"Logged in as {username}")
                else:
                    st.error("Invalid username or password.")
            else:
                st.error("Please enter both username and password.")

    # Optionally, block access to chat if not logged in
    if "logged_in_user" not in st.session_state:
        st.stop()

"""CSS patch for full left alignment of chat buttons."""

import streamlit as st


def apply_css_patch():
    st.markdown(
        """
        <style>
          /* works for every st.button rendered below */
          div.stButton > button {
              text-align: left !important;        /* left-justify text */
              display: flex !important;           /* turn wrapper into flexbox */
              flex-direction: column !important;  /* stack multiple label lines */
              align-items: flex-start !important; /* hug the left edge */
              justify-content: flex-start !important;
              white-space: normal !important;     /* allow Markdown line breaks */
          }
        </style>
        """,
        unsafe_allow_html=True,
    )

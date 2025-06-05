import streamlit as st
from responder import generate_response
from feedback_logger import log_feedback
from PIL import Image
from datetime import datetime
import pandas as pd
import os

user_img = Image.open("assets/user_avatar.png")
bot_img = Image.open("assets/bot_avatar.png")

# Set Streamlit page title
st.set_page_config(page_title="Placement Query Bot", layout="centered")

st.markdown("""
    <h1 style='font-family: calibri; color: #111B21;'>
        🎓SPMVV Placement Chatbot
    </h1>
""", unsafe_allow_html=True)


# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Define a callback function to handle input and clear text box
def handle_input():
    user_input = st.session_state.input
    if user_input:
        response = generate_response(user_input)
        st.session_state.messages.append({"role": "user", "text": user_input})
        st.session_state.messages.append({"role": "bot", "text": response})
        st.session_state.input = ""  # ✅ Now it's safe to reset

# ✅ Input box with callback
st.text_input("Ask your placement query 👇", key="input", on_change=handle_input)

messages = st.session_state.messages
paired_messages = [messages[i:i+2] for i in range(0, len(messages), 2)]

# Display chat history (Now the feeback is also added to our chat)
for i, pair in enumerate(reversed(paired_messages)):
    for msg in pair:
        if msg["role"] == "user":
            col1, col2 = st.columns([1,9])
            with col1:
                st.image(user_img, width = 48)
            with col2:
                st.markdown(f"""
                <div style='background-color:#dcf8c6; padding:10px; border-radius:10px'>
                    <strong>You:</strong> {msg['text']}
                </div>
                """, unsafe_allow_html=True)
        else:
            col1, col2 = st.columns([1,9])
            with col1:
                st.image(bot_img, width = 48)
            with col2:
                st.markdown(f"""
                <div style='background-color:#f1f0f0;padding:10px;border-radius:10px'>
                    <strong>Bot:</strong> {msg['text']}
                </div>
                """, unsafe_allow_html=True)

            st.write("")
            # 👍 👎 Feedback buttons for the bot response
            feedback_col1, feedback_col2 = st.columns([5, 1])
            with feedback_col1:
                if st.button("👍 Yes", key=f"yes_{i}"):
                    from feedback_logger import log_feedback
                    log_feedback(pair[0]["text"], msg["text"], "Yes")
                    st.success("Thanks for your feedback! 🙌")

            with feedback_col2:
                if st.button("👎 No", key=f"no_{i}"):
                    from feedback_logger import log_feedback
                    log_feedback(pair[0]["text"], msg["text"], "No")
                    st.info("We'll try to improve that! 💡")
            
            st.write("")

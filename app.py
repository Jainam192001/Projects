import streamlit as st
import json
from openai import OpenAI

# Load resume data
with open("resume.json", "r") as f:
    resume_data = json.load(f)

resume_context = json.dumps(resume_data, indent=2)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

import streamlit as st

# Page config
st.set_page_config(page_title="🤖 Jainam Patel - Resume Chatbot", layout="centered")

# Main title with emoji and style
st.markdown(
    """
    <h1 style='text-align: center; color: #4A90E2;'>💼 Jainam Patel - Resume Chatbot</h1>
    """,
    unsafe_allow_html=True,
)

# Introductory message with style and spacing
st.markdown(
    """
    <div style='text-align: center; font-size:18px; color:#555;'>
        👋 Welcome! I'm your interactive assistant. <br>
        Ask me anything about <strong>Jainam Patel's resume</strong>, experience, skills, projects, and more.
    </div>
    <br>
    """,
    unsafe_allow_html=True,
)

# Optional: Add a decorative divider
st.markdown("---")


# User input
user_input = st.text_input("Your question:")

# Chat logic
if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Answer based only on this resume:\n{resume_context}"},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content
        st.success(answer)

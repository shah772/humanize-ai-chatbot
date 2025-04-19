import openai
import streamlit as st
import time
import random

openai.api_key = st.secrets["api_key"]

def type_like_human(text):
    output = ""
    for char in text:
        output += char
        time.sleep(random.uniform(0.01, 0.05))
    return output

st.set_page_config(page_title="Humanize AI Chatbot", page_icon="🤖")
st.title("🤖 Humanize AI Chatbot")
st.write("Chat with an AI that sounds more like a real human 👨‍💻")

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking like a human..."):
        prompt = f"""You are a friendly, casual AI assistant. Answer warmly and like a human.
User: {user_input}
AI:"""

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.8,
            top_p=1,
            frequency_penalty=0.3,
            presence_penalty=0.3
        )

        ai_reply = response['choices'][0]['text'].strip()
        humanized = type_like_human(ai_reply)

        st.markdown(f"**AI:** {humanized}")

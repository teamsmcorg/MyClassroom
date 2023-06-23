import streamlit as st
from streamlit_chat import message as st_message
st.set_page_config(page_title="Doubtbot", page_icon="🤖", layout="wide")


st.title("DoubtBot")


import openai

openai.api_key = '(api key)'
openai.api_base = 'https://api.pawan.krd/v1'
if "history" not in st.session_state:
    st.session_state.history = []
def generate_answer():
    user_message = st.session_state.input_text
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=user_message,
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    message_bot = response.choices[0].text
    st.session_state.history.append({"message": message_bot, "is_user": False})
    st.session_state.history.append({"message": user_message, "is_user": True})


st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)

for i, chat in enumerate(reversed(st.session_state.history)):
    st_message(**chat, key=str(i)) #unpacking

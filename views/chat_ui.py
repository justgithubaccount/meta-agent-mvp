import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from controllers.chat_controller import ChatController

st.set_page_config(page_title="🤖 Meta Agent MVP", layout="wide")
st.title("🤖 Meta-Agent: AI That Builds AI")

controller = ChatController()

user_input = st.chat_input("Введите запрос...")

if user_input:
    with st.spinner("Обработка запроса..."):
        response = controller.handle_user_input(user_input)
        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write(response)

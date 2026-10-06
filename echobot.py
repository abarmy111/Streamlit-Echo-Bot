import streamlit as st

with st.chat_message("user"):
    st.write("Hello 👋")

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


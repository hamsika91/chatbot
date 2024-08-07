import os
import streamlit as st
import google.generativeai as genai # type: ignore
 
GOOGLE_API_KEY = "AIzaSyBbSKh1MdyxJjXVCf0Are2SWOkWtNCA3KE"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
 
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
 
st.set_page_config(
    page_title="Chatbot ",
    page_icon=":brain:",  # Favicon emoji
    layout="wide")
 
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
 
st.title("ChatBot")
 
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
user_prompt = st.chat_input("Ask Anything...")
 
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
 
    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
 
    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
 
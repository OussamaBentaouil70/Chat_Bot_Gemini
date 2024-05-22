from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response = chat.send_message(question, stream=True)
    return response

## Initialize Streamlit app
st.set_page_config(page_title="Chatbot Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message  in st.session_state.messages:
  with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt:= st.chat_input("Type your message here:"):
  st.session_state.messages.append({"role":"user","content":prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
    
  with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    for response in get_gemini_response(prompt):
        full_response += response.text
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role":"assistant","content":full_response})




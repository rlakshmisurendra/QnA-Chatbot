from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Google Generative AI API
genai.configure(api_key="AIzaSyDxaI8tbMWFOSa7zW8pcFopZkz1yhr-Lqo")

# Function to load Gemini Pro and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


# Initialize Streamlit app
st.set_page_config(page_title="Q&A Chatbot")

st.header("Gemini LLM Application")

# Initialize chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state["chat_history"] = []

# Input field for user question
input_text = st.text_input("Input", key="input")
submit = st.button("Ask the Question")

# Process the user's question and get the response
if submit:
    response = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))

    st.subheader("Your response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display the chat history
st.subheader("Chat History:")
for role, text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")

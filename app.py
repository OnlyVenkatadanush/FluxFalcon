import streamlit as st
from openai import OpenAI
from groq1 import get_response
from test import print_models
import base64
def get_base64_of_image(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# Set page config
st.set_page_config(page_title="ChatBot AI", layout="wide",page_icon="photos/logo.jpeg")

# Sidebar
st.sidebar.title("ChatBot AI")
api_key = st.sidebar.text_input("Enter your API Key", type="password")

# Fetch and cache model list only once
if api_key and 'model_list' not in st.session_state:
    try:
        st.session_state['model_list'] = print_models(api_key)
    except Exception as e:
        st.session_state['model_list'] = []
        st.sidebar.error(f"Failed to fetch models: {str(e)}")

# Use cached model list if available
model_list = st.session_state.get('model_list', [])
selected_model = st.sidebar.selectbox("Select your model", model_list)

# Check if the selected model has changed and reset the chat history if it has
if 'previous_model' in st.session_state:
    if st.session_state['previous_model'] != selected_model:
        st.session_state['messages'] = []  # Clear the chat history

# Store the currently selected model in session state
st.session_state['previous_model'] = selected_model

# Initialize chat history if it doesn't exist
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Display chat history
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.write(f"{message['text']}")

# Chat input
prompt = st.chat_input("Type your message...")

# Handle user input
if prompt:
    with st.spinner("Generating response..."):
        # Add user message to the history
        st.session_state['messages'].append({"role": "user", "text": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        try:
            if not api_key:
                response = "Please enter your API key."
            else:
                response = get_response(prompt, api_key, selected_model)
        except Exception as e:
            response = f"Error: {str(e)}"

        # Add assistant's response to the history
        st.session_state['messages'].append({"role": "assistant", "text": response})
        with st.chat_message("assistant"):
            st.write(f"{selected_model}: {response}")
encoded_image = get_base64_of_image('photos/background.jpeg')

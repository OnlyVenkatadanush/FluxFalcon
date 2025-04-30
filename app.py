import streamlit as st
from response import get_response
from list_models import print_models_op, print_models_gq
import base64
import requests

# Function to get base64 of an image
def get_base64_of_image(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set page config
st.set_page_config(page_title="Flux Falcon", layout="wide", page_icon="photos/logo.jpeg")

# Function to start chat and handle user input
def start():
    if 'previous_model' in st.session_state:
        if st.session_state['previous_model'] != selected_model:
            st.session_state['messages'] = []  # Clear the chat history

    # Store the currently selected model in session state
    st.session_state['previous_model'] = selected_model

    # Initialize chat history if it doesn't exist
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Display chat history
    with st.expander("Chat History"):
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
                    response = get_response(prompt, api_key, selected_model, selected_platform)
            except Exception as e:
                response = f"Error: {str(e)}"

            # Add assistant's response to the history
            st.session_state['messages'].append({"role": "assistant", "text": response})
            with st.chat_message("assistant"):
                st.write(f"{selected_model}: {response}")

# Sidebar selection
with st.sidebar:
    col1, col2 = st.columns([2,6])
    with col1:
        st.image("photos/background.jpg")
    with col2:
        st.markdown("""
            <h1 style='font-size: 40px;color: #87CEEB'>
                Flux Falcon
            </h1>
            """, unsafe_allow_html=True)
    selected_platform = st.selectbox("Choose model platform", ["OpenRouter", "Groq"])

# Improved API key validation function
def validate_api_key_and_fetch_models(platform, api_key):
    endpoints = {
        "OpenRouter": "https://openrouter.ai/api/v1/models",
        "Groq": "https://api.groq.com/openai/v1/models"
    }

    if platform not in endpoints:
        return None, "⚠ Invalid platform."

    headers = {"Authorization": f"Bearer {api_key}"}
    url = endpoints[platform]

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        if platform == "OpenRouter":
            if "error" in data:
                return None, f"❌ OpenRouter error: {data['error'].get('message', 'Unknown error')}"
            elif api_key:
                return data, None
            else:
                return None, "⚠ Unexpected response from OpenRouter."

        if response.status_code == 200:
            if "data" in data and isinstance(data["data"], list):
                return data, None
            elif "error" in data:
                return None, f"❌ API error: {data['error'].get('message', 'Unknown error')}"
            else:
                return None, "⚠ Unexpected response format."
        elif response.status_code == 401:
            return None, "❌ Invalid API key."
        else:
            return None, f"⚠ Unexpected error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return None, f"❌ Request failed: {str(e)}"

if selected_platform == "OpenRouter":
    api_key = st.sidebar.text_input("Enter your API Key (OpenRouter)", type="password")
    if api_key:
        models, error = validate_api_key_and_fetch_models("OpenRouter", api_key)
        if models:
            st.sidebar.success("✅API key is entered")
            if 'by_family' not in st.session_state:
                try:
                    st.session_state['by_family'] = print_models_op(api_key)
                except Exception as e:
                    st.session_state['by_family'] = {}
                    st.sidebar.error(f"⚠Failed to fetch models: {str(e)}")
            by_family = st.session_state.get('by_family', {})
            family = st.sidebar.selectbox("Select a model family", list(by_family.keys()))
            selected_model = st.sidebar.selectbox(f"Select a model from {family}", by_family.get(family, []))
            st.sidebar.success(f"You selected: {selected_model}")
            start()
        else:
            st.sidebar.error(error)

elif selected_platform == "Groq":
    api_key = st.sidebar.text_input("Enter your API Key (Groq)", type="password")
    if api_key:
        models, error = validate_api_key_and_fetch_models("Groq", api_key)
        if models:
            st.sidebar.success("✅API key is valid")
            if 'model_list' not in st.session_state:
                try:
                    st.session_state['model_list'] = print_models_gq(api_key)
                except Exception as e:
                    st.session_state['model_list'] = []
                    st.sidebar.error(f"⚠Failed to fetch models: {str(e)}")
            model_list = st.session_state.get('model_list', [])
            selected_model = st.sidebar.selectbox("Select your model", model_list)
            st.sidebar.success(f"You selected: {selected_model}")
            start()
        else:
            st.sidebar.error(error)

# Fetch image in base64 format
encoded_image = get_base64_of_image('photos/background.jpg')

st.markdown(
    f"""
    <style>
    html, body, .stApp {{
        height: 100%;
        margin: 0;
        padding: 0;
        background-image: url("data:image/jpeg;base64,{encoded_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: 25% 25%;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
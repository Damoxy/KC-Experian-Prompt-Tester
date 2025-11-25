"""
Streamlit Prompt Tester App
Test and modify AI prompts for the Knowledge Core IQ Search application
"""

import streamlit as st
import requests
import json
from prompts import CATEGORY_PROMPTS
import os
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

# Page configuration
st.set_page_config(
    page_title="Prompt Tester - KC IQ Search",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        color: #2E3B55;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        color: #5A6C7D;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .prompt-section {
        background-color: #f8f9fa;
        border-left: 4px solid #2E3B55;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .response-section {
        background-color: #e8f5e9;
        border-left: 4px solid #4caf50;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-top: 1.5rem;
    }
    .error-section {
        background-color: #ffebee;
        border-left: 4px solid #f44336;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">🧪 KC Experian Prompt Tester</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Test and modify AI prompts for KC ProspectIQ Search</p>', unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.header("⚙️ Configuration")

st.sidebar.subheader("📋 Input Data")
first_name = st.sidebar.text_input("First Name", placeholder="e.g., John", key="first_name")
last_name = st.sidebar.text_input("Last Name", placeholder="e.g., Smith", key="last_name")
city = st.sidebar.text_input("City", placeholder="e.g., Phoenix", key="city")
state = st.sidebar.text_input("State", placeholder="e.g., AZ", key="state")

full_name = f"{first_name} {last_name}".strip()

st.sidebar.markdown("---")

st.sidebar.subheader("📝 Select Prompt Category")
selected_category = st.sidebar.selectbox(
    "Choose a category:",
    list(CATEGORY_PROMPTS.keys()),
    index=0,
    help="Select which prompt template to use",
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

model = st.sidebar.selectbox(
    "AI Model",
    [
        "google/gemini-2.5-flash",
        "google/gemini-2.0-flash-001",
        "google/gemini-3-pro-preview",
        "google/gemini-2.5-pro",
        "openai/gpt-4.1-mini",
        "openai/gpt-5-mini",
        "openai/gpt-4o-mini",
        "openai/gpt-5",
        "openai/gpt-4.1",
        "x-ai/grok-code-fast-1",
    ],
    index=0,
    help="Select the AI model to use"
)

# Get API key from environment
api_key = os.getenv("OPENROUTER_API_KEY", "")

# Main layout - Edit Prompt on left, Response on right
col1, col2 = st.columns([1, 1], gap="medium")

with col1:
    st.header("✏️ Edit Prompt")
    
    # Get the current prompt
    current_prompt = CATEGORY_PROMPTS[selected_category]
    
    # Editable prompt area
    edited_prompt = st.text_area(
        "Prompt Template",
        value=current_prompt,
        height=400,
        help="Edit the prompt template. Use {full_name}, {city}, {state} as variables."
    )

with col2:
    st.header(f"📥 {model} Response")
    response_placeholder = st.empty()

# Generate response section
st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    generate_btn = st.button("Generate Response", type="primary", use_container_width=True)

with col2:
    reset_btn = st.button("Reset to Default", use_container_width=True)

# Handle reset button
if reset_btn:
    st.session_state.edited_prompt = CATEGORY_PROMPTS[selected_category]
    st.rerun()

# Handle generate button
if generate_btn:
    if not api_key:
        with col2:
            st.error("❌ API key not found in environment variables.")
    elif not full_name or not city or not state:
        st.error("❌ Please fill in all required fields: First Name, Last Name, City, and State.")
    else:
        # Format the prompt with user input
        try:
            formatted_prompt = edited_prompt.format(
                full_name=full_name,
                city=city,
                state=state
            )
            
            # Call the OpenRouter API
            with st.spinner("🤖 Generating AI response..."):
                try:
                    response = requests.post(
                        "https://openrouter.ai/api/v1/chat/completions",
                        headers={
                            "Authorization": f"Bearer {api_key}",
                            "HTTP-Referer": "https://localhost:3000",
                            "X-Title": "KC ProspectIQ Prompt Tester",
                        },
                        json={
                            "model": model,
                            "messages": [
                                {
                                    "role": "user",
                                    "content": formatted_prompt
                                }
                            ],
                            "temperature": 0.7,
                            "max_tokens": 2048,
                        },
                        timeout=60
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        ai_response = data['choices'][0]['message']['content']
                        
                        # Display the response in the right column
                        with response_placeholder.container():
                            st.markdown('<div class="response-section">', unsafe_allow_html=True)
                            st.markdown(ai_response)
                            st.markdown('</div>', unsafe_allow_html=True)
                    
                    else:
                        error_data = response.json()
                        error_msg = error_data.get('error', {}).get('message', 'Unknown error')
                        with response_placeholder.container():
                            st.markdown('<div class="error-section">', unsafe_allow_html=True)
                            st.error(f"❌ API Error: {error_msg}")
                            st.markdown('</div>', unsafe_allow_html=True)
                
                except requests.exceptions.Timeout:
                    with response_placeholder.container():
                        st.markdown('<div class="error-section">', unsafe_allow_html=True)
                        st.error("❌ Request timeout. The API took too long to respond.")
                        st.markdown('</div>', unsafe_allow_html=True)
                except requests.exceptions.RequestException as e:
                    with response_placeholder.container():
                        st.markdown('<div class="error-section">', unsafe_allow_html=True)
                        st.error(f"❌ Request failed: {str(e)}")
                        st.markdown('</div>', unsafe_allow_html=True)
        
        except KeyError as e:
            with response_placeholder.container():
                st.markdown('<div class="error-section">', unsafe_allow_html=True)
                st.error(f"❌ Prompt formatting error: Missing variable {e}. Use {{full_name}}, {{city}}, {{state}}.")
                st.markdown('</div>', unsafe_allow_html=True)



import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
from pathlib import Path

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("GOOGLE_API_KEY")
print("Loaded key:", api_key)  # Debug line
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# App Config
st.set_page_config(page_title="Trotwear Customer Service", page_icon="🧢", layout="centered")

# Mobile-optimized CSS styling
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #FFFFFF;
        }
        .stApp {
            background-color: #000000;
        }
        h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
            color: #FFFFFF !important;
        }
        .stTextInput > div > input {
            background-color: #1a1a1a;
            color: #FFFFFF;
            border: 1px solid #00AEEF;
            font-size: 16px;
            padding: 12px;
        }
        .stButton>button {
            background-color: #00AEEF;
            color: #FFFFFF;
            border-radius: 8px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stSpinner {
            color: #00AEEF !important;
        }

        @media screen and (max-width: 600px) {
            h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
                font-size: 16px !important;
            }
            .stTextInput > div > input {
                font-size: 14px !important;
                padding: 10px;
            }
            .stButton>button {
                font-size: 14px !important;
                padding: 10px 20px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# UI
st.title("🧢 Trotwear Customer Service")
st.write("Welcome! Ask anything about Trotwear’s products, shipping, returns, or sizing.")

# Business context
BUSINESS_CONTEXT = """
You are a friendly and professional AI customer service assistant for Trotwear, 
a modern fashion and apparel brand known for stylish boxers. 
Help customers with questions about products, sizes, shipping, returns, and more.

Shipping Policy:
- Delivery Time: 3-7 (Working Days)
- Payment Method: COD, Online Payments IBFT
- Delivery Charges: Rs: 200, Free Delivery on Orders above Rs: 3,000
- Return/Exchange: Unused products can be exchanged or returned within 30 days with the original invoice.
- Boxers or briefs cannot be returned or exchanged for hygiene reasons.
- Manufacturing defect claims must be made within 30 days. The company may offer repair or replacement.
"""

# Initialize session state for chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input field
user_input = st.text_input("What can I help you with today?")

# Handle chat
if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    with st.spinner("Trotwear is typing..."):
        try:
            chat = model.start_chat(history=[
                {"role": "user", "parts": BUSINESS_CONTEXT},
                *[
                    {"role": msg["role"], "parts": msg["text"]}
                    for msg in st.session_state.chat_history
                ]
            ])

            response = chat.send_message(user_input)
            st.session_state.chat_history.append({"role": "model", "text": response.text})

            st.markdown(f"**Trotwear AI:** {response.text}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

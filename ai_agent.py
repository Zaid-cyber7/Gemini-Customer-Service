import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")
 
# App Config
st.set_page_config(page_title="Trotwear Customer Service", page_icon="🧢", layout="centered")

# Custom CSS for styling
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
            border: 1px solid #00AEEF; /* blue highlight */
        }
        .stButton>button {
            background-color: #00AEEF;
            color: #FFFFFF;
            border-radius: 8px;
            border: none;
        }
        .stSpinner {
            color: #00AEEF !important;
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
This is the shipping policy of trotwear:
Delivery Time: 3-7 (Working Days)
Payment Method: COD, Online Payments IBFT
Delivery Charges: Rs: 200, Free Delivery on Orders above Rs: 3,000
Return/Exchange: Unused products can be exchanged or returned within 30 days from the date of purchase by presenting the product with an original invoice.
Due to hygiene issues Boxer shorts or Boxers Briefs can not be returned or exchanged

In case of any manufacturing defect, a claim can be presented within 30 days from the date of purchase.
To settle a claim, company reserves the right to either repair the product or offer a new one in exchange.
"""

# Input box
user_input = st.text_input("What can I help you with today?")

# AI Response
if user_input:
    with st.spinner("Trotwear is typing..."):
        try:
            response = model.generate_content(f"{BUSINESS_CONTEXT}\nCustomer: {user_input}")
            st.markdown(f"**Trotwear AI:** {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

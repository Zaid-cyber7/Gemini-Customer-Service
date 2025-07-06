import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load the model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="Gemini AI Agent")
st.title("🤖 Gemini Customer Service Agent")

user_input = st.text_input("Ask a question:")
if user_input:
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(f"""
You are a professional and friendly AI customer service assistant for Trotwear, 
which offers boxers and t-shirts. Always respond clearly, concisely, and helpfully. within a limit of 200 words.

Customer says: {user_input}
""")

            st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

import streamlit as st
import google.generativeai as genai

# UI setup
st.set_page_config(page_title="Customer Support Chatbot", page_icon="💬")
st.title("💬 Gemini Customer Service Bot")

# Ask for Gemini API key
api_key = st.text_input("Enter your Gemini API Key:", type="password")

# Get user prompt
prompt = st.text_area("What would you like to ask?", height=150)

if st.button("Send") and api_key and prompt:
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)

        # Load Gemini model
        model = genai.GenerativeModel("gemini-pro")

        # Send the user prompt
        response = model.generate_content(prompt)

        # Display the response
        st.success("🤖 Bot: " + response.text)

    except Exception as e:
        st.error(f"❌ Error: {e}")

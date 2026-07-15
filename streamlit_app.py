import streamlit as st
from src.chatbot import ask_chatbot

st.title("🤖 Azure AI Learning Assistant")

# -----------------------------
# Create conversation history
# -----------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

# -----------------------------
# Display conversation
# -----------------------------
for message in st.session_state.messages:

    # Don't display the system prompt
    if message["role"] != "system":

        with st.chat_message(message["role"]):
            st.write(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input("Ask me anything...")

if user_input:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    
    # Send the COMPLETE conversation to Azure OpenAI
    response = ask_chatbot(st.session_state.messages)
    
    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
    '''st.json(st.session_state.messages)'''
    # Refresh the page to display the latest messages
    st.rerun()
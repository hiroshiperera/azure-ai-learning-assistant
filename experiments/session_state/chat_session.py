import streamlit as st

st.title("🤖 Azure AI Learning Assistant")

# Create the chat history only once
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
user_input = st.chat_input("Ask me anything...")

if user_input:

    # Save the user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display the user message
    with st.chat_message("user"):
        st.write(user_input)
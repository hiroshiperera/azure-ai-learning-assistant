''' Day 3,4 --> streamlit_app.py handles the responsibility for session management. Removes the session management capability of chatbot.py

from openai import OpenAI

from src.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
)

client = OpenAI(
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
)

# This is for Terminal Chatbot code, but without Memory - Day 1

def ask_chatbot(user_message: str) -> str:

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response.choices[0].message.content

# This is memorized chatbot - Day 2

# Conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

def ask_chatbot(user_message: str) -> str:

    # Add user's message
    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=messages
    )

    answer = response.choices[0].message.content

    # Save assistant's response
    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return answer

'''

'''-----------------Day 5-----------------'''

from openai import OpenAI
import streamlit as st

from src.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
)

client = OpenAI(
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
)


def ask_chatbot(messages: list[dict]):

    '''st.json(st.session_state.messages)'''


    response = client.chat.completions.create(

        model=AZURE_OPENAI_DEPLOYMENT,
        messages=messages,

        temperature=0,
        max_completion_tokens=300
    )

    print(type(response.choices[0].message.content))
    print(repr(response.choices[0].message.content))

    return response.choices[0].message.content
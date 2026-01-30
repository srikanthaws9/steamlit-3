import streamlit as st

st.set_page_config(page_title="Simple Chatbot")

st.title("💬 My First Chatbot")

# Session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type a message...")

# Simple bot logic
def bot_reply(text):
    text = text.lower()
    
    if "hello" in text:
        return "Hi there! 👋"
    elif "how are you" in text:
        return "I'm just code, but I'm doing great 😄"
    elif "devops" in text:
        return "DevOps is awesome! 🚀"
    elif "bye" in text:
        return "Goodbye! Have a nice day!"
    else:
        return "I’m not sure how to answer that 🤔"

# When user sends message
if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    
    st.chat_message("user").write(user_input)

    # Bot response
    response = bot_reply(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    
    st.chat_message("assistant").write(response)

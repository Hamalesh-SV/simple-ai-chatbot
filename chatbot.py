import streamlit as st
import ollama

st.title("AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
            You are a helpful and friendly AI assistant.
            Answer questions clearly and concisely.
            Give detailed answers only when the user asks for them.
            """
        }
    ]

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# User input
if prompt := st.chat_input("Ask me anything..."):

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Generate response
    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        answer = ""

        stream = ollama.chat(
            model="llama3.2",
            messages=st.session_state.messages,
            stream=True,
            keep_alive="10m"
        )

        for chunk in stream:

            text = chunk["message"]["content"]

            answer += text

            response_placeholder.markdown(answer)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
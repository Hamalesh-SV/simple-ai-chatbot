import ollama

messages = [
    {
        "role": "system",
        "content": "You are a helpful and friendly AI chatbot. Answer clearly and concisely."
    }
]

while True:

    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    print("\nChatbot: ", end="", flush=True)

    stream = ollama.chat(
        model="llama3.2",
        messages=messages,
        stream=True
    )

    answer = ""

    for chunk in stream:
        text = chunk["message"]["content"]
        print(text, end="", flush=True)
        answer += text

    print()

    messages.append({
        "role": "assistant",
        "content": answer
    })
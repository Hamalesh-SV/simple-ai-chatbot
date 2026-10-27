import ollama

messages = [
    {
        "role":"Assistance",
        "content":"You are helpfull chatbot.You have answers simply and clearly to the user questions"
    }
]
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("Chatbot:", response["message"]["content"])
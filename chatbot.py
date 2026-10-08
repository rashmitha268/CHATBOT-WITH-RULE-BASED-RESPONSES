print("ChatBot: Hello! I am a simple rule-based chatbot.")
print("ChatBot: Type 'bye' or 'exit' to end the conversation.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("ChatBot: Hello! Nice to meet you.")

    elif "how are you" in user_input:
        print("ChatBot: I'm doing great! Thank you for asking.")

    elif "your name" in user_input:
        print("ChatBot: My name is SimpleBot.")

    elif "what can you do" in user_input:
        print("ChatBot: I can answer simple questions using predefined rules.")

    elif "thank" in user_input:
        print("ChatBot: You're welcome!")

    elif user_input in ["bye", "exit"]:
        print("ChatBot: Goodbye!")
        break

    else:
        print("ChatBot: Sorry, I don't understand that.")
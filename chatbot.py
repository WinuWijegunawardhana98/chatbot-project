
def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hi there! How can I help?",
        "bye": "Goodbye! Have a great day!",
        "how are you": "I'm just a bot, but I'm doing well. How about you?",
        "thank you": "You're welcome! Anything else I can help with?",
        "what is your name": "I'm your friendly chatbot.",
        "what can you do": "I can chat with you, answer basic questions, and make your day better!"

    }
    # Return a response or a default message
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

if __name__ == "__main__":
    print("Chatbot: Hi! I'm your assistant. Type 'bye' to exit.")
    
    # Start a chat loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Bye! Take care.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

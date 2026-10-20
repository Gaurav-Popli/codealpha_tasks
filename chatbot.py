def get_bot_response(user_input):
    # Normalize input
    text = user_input.lower().strip()

    # Rule-Based Conditions
    if text in ["hello", "hi", "hey", "greetings"]:
        return "Hi there! How can I help you today?"
    
    elif text in ["how are you", "how are you doing", "how's it going"]:
        return "I'm doing great, thank you for asking! How are you?"
    
    elif text in ["what is your name", "who are you"]:
        return "I am a simple rule-based Python chatbot created for CodeAlpha."
    
    elif text in ["codealpha", "what is codealpha"]:
        return "CodeAlpha is a platform offering virtual skill-building internships!"
    
    elif text in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a fantastic day ahead!"
    
    else:
        return "I'm sorry, I don't understand that yet. Try asking 'hello' or 'how are you'."

def start_chat():
    print("==========================================")
    print("         WELCOME TO PYTHON CHATBOT        ")
    print("==========================================")
    print("Type 'bye' or 'exit' anytime to stop the chat.\n")

    while True:
        user_msg = input("You: ")
        
        if not user_msg.strip():
            continue

        response = get_bot_response(user_msg)
        print(f"Bot: {response}\n")

        # Exit loop if user says goodbye
        if user_msg.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    start_chat()
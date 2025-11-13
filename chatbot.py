import re

def get_response(user_message):
    # Make everything lowercase for easier matching
    user_message = user_message.lower()

    # Greet if user says hello/hi/hey
    if re.search(r'\b(hi|hello|hey)\b', user_message):
        return "Hey there! What can I help you with?"

    # Check for 'how are you'
    elif 'how are you' in user_message  or "what about you" in user_message :
        return "I'm just code, but I'm feeling pretty good! How about you?"

    # Name inquiry
    elif "your name" in user_message or "what is your name" in user_message:
        return "You can call me Chatbot. I'm just a small Python chatbot!"

    # Respond to thanks
    elif "thank you" in user_message or "thanks" in user_message:
        return "You're welcome! Anything else on your mind?"

    # Farewell words
    elif re.search(r'\b(bye|goodbye|exit|quit)\b', user_message):
        return "See you later! Take care!"

    # Default for anything else
    else:
        return "Hmm, not sure I follow. Can you ask me differently?"

def chatbot():
    print("Chatbot: Hi! I'm Chatbot - type something and let's see if I understand. Type 'bye' to end.")

    while True:
        user_input = input("You: ")
    
        if re.search(r'\b(bye|goodbye|exit|quit)\b', user_input.lower()):
            print("Chatbot: See you later! Take care!")
            break

        reply = get_response(user_input)
        print("Chatbot:", reply)

if __name__ == "__main__":
    chatbot()

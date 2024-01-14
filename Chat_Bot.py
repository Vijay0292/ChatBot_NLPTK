import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am fine, thank you!', 'I am doing well. How about you?']),
    (r'(.*) your name?', ['I am a simple chatbot.', 'Call me ChatBot.']),
    (r'quit', ['Bye! Take care.']),
]

# Create a chatbot using the patterns and reflections
chatbot = Chat(patterns, reflections)

# Function to start the chat
def chatbot_interaction():
    print("Hello! I'm a simple chatbot. You can type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Bye! Take care.")
            break
        else:
            response = chatbot.respond(user_input)
            print("ChatBot:", response)

# Run the chatbot interaction
if __name__ == "__main__":
    nltk.download('punkt')  # Ensure the punkt tokenizer is downloaded
    chatbot_interaction()
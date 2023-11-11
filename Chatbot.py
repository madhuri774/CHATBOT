import random

greetings = ["hello", "hi", "hey", "what's up"]
goodbyes = ["bye", "goodbye", "see you later", "have a nice day"]
questions = {
    "what is your name?": "My name is Chatbot!",
    "how are you?": "I'm doing well, thanks for asking!",
    "what do you like to do?": "I like to chat with people!",
    "where are you from?": "I was born and raised in the cloud.",
    "what is the meaning of life?": "That's a deep question. What do you think?"
}

def chatbot():
    print("Hello! I'm a chatbot. What can I help you with today?")

while True:
    user_input = input("> ").lower()

    if user_input in goodbyes:
        print("Goodbye!")
        break
    elif user_input in questions:
        print(questions[user_input])
    else:
        print(random.choice(greetings))

chatbot()

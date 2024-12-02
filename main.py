from detect_unallowed_word import detect_unallowed_word
from detect_offensive_word import detect_offensive_word
from log_chat_history import log_chat_history

SYSTEM = "system"

while True:
    user_id = input("User ID: ")
    if user_id.lower() in ["exit", "quit"]:
        print("Exiting...")
        break

    message = input("Message: ")
    if message.lower() in ["exit", "quit"]:
        print("Exiting...")
        break

    log_chat_history(user_id, message)

    if detect_unallowed_word(message) or detect_offensive_word(message):
        response = "I'm sorry, but I can't assist with that request"
    else:
        response = f"I hear you say: {message}"

    print(f"Chatbot: {response}")
    log_chat_history(SYSTEM, response)

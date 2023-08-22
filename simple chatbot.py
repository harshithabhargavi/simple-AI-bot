def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to assist you!"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "good morning" in user_input:
        return "very good morning to u harshitha"
    elif "good night" in user_input:
        return "sleep well"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"


while True:
    user_question = input("HARSHITHA : ")
    if user_question.lower() == "exit":
        print("Chatbot: BYE HARSHITHA")
        break
    response = simple_chatbot(user_question)
    print("Chatbot:",response)

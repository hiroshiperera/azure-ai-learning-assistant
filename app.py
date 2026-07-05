from src.chatbot import ask_chatbot


print("=" * 50)
print(" Azure AI Learning Assistant ")
print("=" * 50)

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    answer = ask_chatbot(question)

    print("\nAI:")
    print(answer)
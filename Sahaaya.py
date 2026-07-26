import random

print("=" * 55)
print("                  SAHAAYA")
print("         Your Mental Wellness Companion")
print("=" * 55)

greetings = [
    "Hey!",
    "Hello there!",
    "Hi! Nice to see you!",
    "Heyyy! How can I help?"
]

quotes = {
    "motivation": [
        "Success comes from consistent effort.",
        "Every expert was once a beginner.",
        "Keep moving forward."
    ],
    "study": [
        "Focus on progress, not perfection.",
        "One hour of focused study is better than five hours of distraction.",
        "Small daily improvements lead to big results."
    ],
    "life": [
        "Be kind whenever possible.",
        "Your future is created by what you do today.",
        "Every day is a fresh beginning."
    ]
}

conversation_count = 0


def quote_of_the_day():

    print("\nSahaaya : Choose a category")
    print("1. Motivation")
    print("2. Study")
    print("3. Life")

    choice = input("\nYou : ")

    if choice == "1":
        print("\nSahaaya :", random.choice(quotes["motivation"]))

    elif choice == "2":
        print("\nSahaaya :", random.choice(quotes["study"]))

    elif choice == "3":
        print("\nSahaaya :", random.choice(quotes["life"]))

    else:
        print("\nSahaaya : Invalid choice.")


def stress_support():

    print("\nSahaaya : I'm sorry you're feeling overwhelmed.")
    print("You don't have to solve everything at once.")
    print("Let's focus on one small step.")

    print("\n1. Studying")
    print("2. Assignment or Homework")
    print("3. Project")
    print("4. Something Else")

    choice = input("\nYou : ")

    if choice == "1":
        print("\nSahaaya : Your ONE SMALL STEP")
        print("- Open your notes.")
        print("- Choose ONE topic.")
        print("- Study for just 10 minutes.")
        print("- Small steps count.")

    elif choice == "2":
        print("\nSahaaya :")
        print("- Open the assignment.")
        print("- Read the first question.")
        print("- Finish only that question.")

    elif choice == "3":
        print("\nSahaaya :")
        print("- Open your project.")
        print("- Choose one small task.")
        print("- Work for only 10 minutes.")

    elif choice == "4":
        print("\nSahaaya :")
        print("Choose one small thing you can do right now.")

    else:
        print("\nSahaaya : Invalid choice.")


def sad_support():

    print("\nSahaaya : I'm sorry you're feeling this way.")
    print("It's okay to have difficult days.")

    print("\n1. I want to talk")
    print("2. I need a distraction")
    print("3. Self Care")
    print("4. I'm not sure")

    choice = input("\nYou : ")

    if choice == "1":
        print("\nSahaaya :")
        print("I'm here to listen.")
        print("What's on your mind?")

    elif choice == "2":
        print("\nSahaaya : Try one of these:")
        print("- Listen to music")
        print("- Go for a short walk")
        print("- Watch something you enjoy")

    elif choice == "3":
        print("\nSahaaya :")
        print("- Drink some water.")
        print("- Take deep breaths.")
        print("- Rest for five minutes.")

    elif choice == "4":
        print("\nSahaaya :")
        print("That's okay.")
        print("Let's take one slow breath together.")

    else:
        print("\nSahaaya : Invalid choice.")

def happy_support():

    print("\nSahaaya : I'm really glad to hear that.")
    print("Let's hold on to that feeling for a moment.")

    print("\n1. Something good happened")
    print("2. Someone made me happy")
    print("3. I achieved something")
    print("4. I just feel good today")

    choice = input("\nYou : ")

    if choice == "1":
        print("\nSahaaya :")
        print("That's wonderful.")
        print("Take a moment to appreciate it.")

    elif choice == "2":
        print("\nSahaaya :")
        print("Maybe thank that person.")
        print("A little appreciation goes a long way.")

    elif choice == "3":
        print("\nSahaaya :")
        print("Be proud of yourself.")
        print("You earned this feeling.")

    elif choice == "4":
        print("\nSahaaya :")
        print("Enjoy your day.")
        print("Keep spreading positive energy.")

    else:
        print("\nSahaaya : Invalid choice.")


def suggest_activity():

    print("\nSahaaya : Choose an activity")

    print("1. Relax")
    print("2. Study")
    print("3. Exercise")
    print("4. Fun")

    choice = input("\nYou : ")

    if choice == "1":
        print("\nSahaaya :")
        print("Listen to calming music.")
        print("Practice deep breathing for 5 minutes.")

    elif choice == "2":
        print("\nSahaaya :")
        print("Choose one topic.")
        print("Study for 20 focused minutes.")

    elif choice == "3":
        print("\nSahaaya :")
        print("Go for a short walk.")
        print("Or do some stretching.")

    elif choice == "4":
        print("\nSahaaya :")
        print("Watch something funny.")
        print("Read a book.")
        print("Call a friend.")

    else:
        print("\nSahaaya : Invalid choice.")


username = input("\nSahaaya : Hello! What's your name?\nYou : ").strip().title()

print("\nSahaaya : Nice to meet you,", username + "!")
print("Sahaaya : I'm here whenever you need support.")

print("\nYou can ask me:")
print("- Hi")
print("- Help")
print("- Check in")
print("- I am stressed")
print("- I am sad")
print("- I am happy")
print("- Quote")
print("- Activity")
print("- Stats")
print("- Who am I")
print("- Bye")

while True:

    conversation_count += 1

    userinput = input("\nYou : ").lower().strip()

    if userinput in ["bye", "exit", "quit"]:

        print("\nSahaaya : Goodbye,", username + "!")
        print("Take care and have a wonderful day.")
        break

    elif userinput in ["hey", "hi", "hello", "hii", "heyy"]:

        print("\nSahaaya : Hello,", username + "!")
        print("Sahaaya :", random.choice(greetings))

    elif userinput in ["how are you", "how are u", "how are you doing"]:

        print("\nSahaaya : I'm doing great! Thanks for asking!")

    elif userinput in ["who am i", "do you know me"]:

        print("\nSahaaya : Your name is", username + ".")

    elif userinput in [
        "what is your name",
        "what's your name",
        "who are you",
        "tell me your name"
    ]:

        print("\nSahaaya : I'm Sahaaya, your AI companion.")

    elif userinput in [
        "what can you do",
        "what do you do",
        "help",
        "your capabilities"
    ]:

        print("\nSahaaya : Here's what I can do.")
        print("1. Daily Check-in")
        print("2. Stress Support")
        print("3. Sadness Support")
        print("4. Positive Reflection")
        print("5. Quote Generator")
        print("6. Activity Suggestions")
        print("7. Session Statistics")

    elif userinput in ["thank you", "thanks"]:

        print("\nSahaaya : You're welcome,", username + "!")

    elif userinput in ["check in", "daily check in", "how am i feeling"]:

        print("\nSahaaya : Let's check in with you.")
        print("How are you feeling today?")

        print("\n1. I am feeling good")
        print("2. I am feeling stressed")
        print("3. I am feeling sad")
        print("4. I am feeling overwhelmed")
        print("5. I'm not sure")

        choice = input("\nYou : ")

        if choice == "1":
            happy_support()

        elif choice == "2":
            stress_support()

        elif choice == "3":
            sad_support()

        elif choice == "4":
            stress_support()

        elif choice == "5":
            print("\nSahaaya : That's okay.")
            print("You don't have to understand every feeling immediately.")
            print("Take one moment at a time.")

        else:
            print("\nSahaaya : Please choose a number from 1 to 5.")

    elif userinput in [
        "i am stressed",
        "i'm stressed",
        "i am overwhelmed",
        "i'm overwhelmed"
    ]:

        stress_support()

    elif userinput in [
        "i am sad",
        "i'm sad",
        "i feel sad",
        "i am feeling low"
    ]:

        sad_support()

    elif userinput in [
        "i am happy",
        "i'm happy",
        "i feel great",
        "i am feeling good"
    ]:

        happy_support()

    elif userinput in [
        "quote",
        "motivate me",
        "motivation"
    ]:

        quote_of_the_day()

    elif userinput in [
        "activity",
        "suggest activity",
        "what should i do"
    ]:

        suggest_activity()

    elif userinput == "stats":

        print("\nSahaaya : Session Statistics")
        print("Your Name :", username)
        print("Messages Exchanged :", conversation_count)

    else:

        print("\nSahaaya : I didn't understand that.")
        print("Type 'help' to see what I can do.")
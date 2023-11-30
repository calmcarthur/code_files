import time

def ask_question(question, options, correct_answer):
    print(question)
    time.sleep(1)

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_answer = input("Your choice (enter the number): ")

    try:
        user_answer = int(user_answer)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return ask_question(question, options, correct_answer)

    if 1 <= user_answer <= len(options):
        if options[user_answer - 1] == correct_answer:
            print("Correct! Well done.")
            return True
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")
            return False
    else:
        print("Invalid choice. Please enter a number between 1 and {len(options)}")
        return ask_question(question, options, correct_answer)

def quiz():
    score = 0

    questions = [
        {
            'question': "What is the capital of Canada?",
            'options': ['Toronto', 'Ottawa', 'Vancouver', 'Montreal'],
            'correct_answer': 'Ottawa'
        },
        {
            'question': "Which planet is known as the Red Planet?",
            'options': ['Earth', 'Mars', 'Venus', 'Jupiter'],
            'correct_answer': 'Mars'
        },
        {
            'question': "What is the largest mammal in the world?",
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 'Blue Whale'
        }
    ]

    for question_data in questions:
        if ask_question(**question_data):
            score += 1
        time.sleep(1)

    print(f"You scored {score}/{len(questions)} in the quiz.")

if __name__ == "__main__":
    quiz()

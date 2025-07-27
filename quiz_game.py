# quiz_game.py

"""
Quiz Game - First Functional Software by Sayan
----------------------------------------------
A modular, expandable quiz game with support for multiple question types.
"""

from questions import multiple_choice_questions, True_false_questions
import time

# ---------------------------- Helper Functions ----------------------------

def display_question(question, answers, correct, question_type="multiple_choice"):
    """
    Displays a question and its possible answers in a formatted manner.
    """
    print(f"\nQuestion: {question}")
    if question_type == "multiple_choice":
        for i, answer in enumerate(answers, 1):
            print(f"{i}. {answer}")
    elif question_type == "true_false":
        print("Options: True / False")
    else:
        print("Please type your answer:")


def check_answer(user_answer, correct, question_type):
    """
    Checks if the user's answer matches the correct one.
    """
    if question_type == "multiple_choice":
        return int(user_answer) - 1 == correct
    elif question_type == "true_false":
        return user_answer.lower() == correct.lower()
    else:
        return user_answer.strip().lower() == correct.strip().lower()


def show_feedback(is_correct, question_type, correct=None):
    """
    Shows feedback to the user based on their answer.
    """
    if is_correct:
        print("✅ Correct! Well done!")
    else:
        if question_type == "multiple_choice":
            print(f"❌ Wrong. The correct answer was option {correct + 1}.")
        elif question_type == "true_false":
            print(f"❌ Wrong. The correct answer was '{correct}'.")
        else:
            print("❌ Wrong. Better luck next time!")


def initialize_game():
    """
    Initializes the game state and welcomes the user.
    """
    print("\n" * 50)
    print("****************************************************")
    print("*           WELCOME TO THE QUIZ GAME!              *")
    print("****************************************************\n")
    print("Test your knowledge across different categories!\n")
    user = input("Enter your name: ")
    print(f"\nWelcome {user}, let's begin the game!")
    time.sleep(1)
    return 0, 0, 1  # score, current_question, round


def game_over(score):
    """
    Handles the game over screen.
    """
    print("\n🎮 Game Over!")
    print(f"🏆 Your final score: {score}")
    print("Thanks for playing! See you next time.")


# ---------------------------- Game Loop ----------------------------

def start_game(questions, score, current_question, rounds):
    """
    Manages the full game flow.
    """
    while True:
        print(f"\nRound {rounds} - Score: {score}\n")
        q = questions[current_question]

        try:
            question_text = q['text']
            answers = q['answers']
            correct = q['correct']
            q_type = q['type']
        except KeyError as e:
            print(f"⚠️ Missing key in question: {e}")
            current_question += 1
            continue

        display_question(question_text, answers, correct, q_type)
        user_answer = input("Your answer: ").strip()

        if q_type == "multiple_choice":
            if not user_answer.isdigit() or not (1 <= int(user_answer) <= len(answers)):
                print("⚠️ Invalid input. Please enter a valid number.")
                continue

        is_correct = check_answer(user_answer, correct, q_type)

        if is_correct:
            score += 10

        show_feedback(is_correct, q_type, correct)

        current_question += 1
        if current_question >= len(questions):
            current_question = 0

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
        rounds += 1

    game_over(score)


# ---------------------------- Entry Point ----------------------------

if __name__ == "__main__":
    all_questions = multiple_choice_questions + True_false_questions
    score, current_question, rounds = initialize_game()
    start_game(all_questions, score, current_question, rounds)

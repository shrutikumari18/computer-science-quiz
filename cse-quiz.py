import urllib.request
import json
import html
import random

# Fetching questions through API
def fetch_questions(amount):
    url = f"https://opentdb.com/api.php?amount={amount}&category=18&type=multiple"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        return data["results"]
    except Exception as e:
        print("Error fetching questions:", e)
        return []

# input from user as how much quetions they want.
def start_quiz():
    try:
        num = int(input("Enter number of questions: "))
    except ValueError:
        print("Invalid number! Defaulting to 5 questions.")
        num = 5

    questions = fetch_questions(num)
    if not questions:
        print("No questions available. Exiting.")
        return


# Starting of the Quiz
    score = 0
    print("\n LET'S START COMPUTER SCIENCE QUIZ \n")

    for i, q in enumerate(questions, start=1):
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])

        options = q["incorrect_answers"] + [correct]
        random.shuffle(options)

        option_map = {
            "a": html.unescape(options[0]),
            "b": html.unescape(options[1]),
            "c": html.unescape(options[2]),
            "d": html.unescape(options[3]),
        }

        print(f"Q{i}. {question}")
        for k, v in option_map.items():
            print(f"  {k}) {v}")

        while True:
            ans = input("Answer (a/b/c/d): ").lower()
            if ans in option_map:
                break
            print("Invalid input!")

        if option_map[ans] == correct:
            print(" ✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong!")
            print(" Correct Answer:", correct, "\n")

    
# Declare that the quiz has ended and show them score and percentage.
    print("Quiz has been ended. Let's check your score:- ")
    print("Score:", score, "/", num)
    print("Percentage:", (score / num) * 100, "%")

if __name__ == "__main__":
    start_quiz()

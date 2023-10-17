from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

URL = "https://opentdb.com/api.php"
# ?amount=10&type=boolean
res = requests.get(URL, params={
    "amount": 10,
    "type": "boolean",
    "category": 18,
})

data_json = res.json()["results"]
question_bank = []
for question in data_json:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

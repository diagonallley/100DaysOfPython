from question_model import Question
from data import question_data
from quiz_brain import Quiz
question_bank=[]

for question in question_data:
    question_bank.append(Question(question["question"],question["correct_answer"]))
    
new_quiz=Quiz(question_bank)
# new_quiz.next_question()

while new_quiz.still_has_question():
    new_quiz.next_question()

print("You completed the quiz")
print(f"Your final score was {new_quiz.score}/{new_quiz.question_number} ")
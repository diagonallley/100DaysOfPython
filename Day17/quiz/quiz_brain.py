

class Quiz:
    def __init__(self,question_list) -> None:
        self.question_number=0
        self.question_list=question_list
        self.score=0
    def next_question(self):
        self.question_number+=1
        user_answer=input((f"Q.{self.question_number}: {self.question_list[self.question_number-1].text} (True/False)?: "))
        answer=self.question_list[self.question_number-1].answer
        if self.answer_is_right(user_answer,answer):
            print("Right")
            self.score+=1
            
        else:
            print(f"Wrong, the answer is {answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print('\n')

    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False

    def answer_is_right(self,user_answer,correct_answer):
        return user_answer.lower()==correct_answer.lower()

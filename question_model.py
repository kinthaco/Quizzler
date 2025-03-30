class QuestionBrain:
    def __init__(self,ques,answer):
        self.ques=ques
        self.answer=answer
    def ask_question(self,number):
        choice=input(f"Q{number}. {self.ques} (True/False)").lower()
        return choice
    def question_validation(self,choice):
        if choice==self.answer.lower():
            print("The answer is right")
            print(f"The correct answer is {self.answer}")
            return True
        else:
            print("The answer is wrong")
            print(f"The correct answer is {self.answer}")
            return False
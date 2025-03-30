from data import question_data
from question_model import QuestionBrain
from user import User
name=input("Please,enter you name:\n")
user_1= User(name)
question_bank=[]
q=1
score=0
for item in question_data:
    ques=item['text']
    ans=item['answer']
    question=QuestionBrain(ques,ans)
    choice=question.ask_question(q)
    q+=1
    mark=question.question_validation(choice)
    if mark:
        score+=1
        user_1.add_points(score)
    else:
        user_1.add_points(score)
    
print(f"\n\nYour final score is {user_1.score}")
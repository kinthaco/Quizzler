class User:
    def __init__(self,name):
        self.name=name
        self.score=0
    def add_points(self,score):
        self.score=score
        print(f"Your score is {self.score}\n\n")

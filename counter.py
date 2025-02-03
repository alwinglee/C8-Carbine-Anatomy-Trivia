from turtle import Turtle

class Counter(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-541, 130)
        self.total_parts = 22
        self.display_counter()

    def display_counter(self):
        self.write(f"Completed:{self.score}/{self.total_parts}", move=False, align="left", font=("Arial", 20, "bold"))

    def update_counter(self):
        self.score += 1
        self.clear()
        self.display_counter()

    def reset_counter(self):
        self.score = 0
        self.clear()
        self.display_counter()






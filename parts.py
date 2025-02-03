from turtle import Turtle

class Parts(Turtle):
    guessed_parts_list = []

    def __init__(self,part,x_coordinate,y_coordinate):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_coordinate, y_coordinate)
        self.write(part, True, align="left", font=("Arial", 11, "normal"))
        Parts.guessed_parts_list.append(self)

    @classmethod
    def reset_parts(cls):
        for part in cls.guessed_parts_list:
            part.clear()
        cls.guessed_parts_list = []
from turtle import Turtle

class Parts(Turtle):
    """
    Represents the labels for each part of the C8 Carbine firearm.
    Each instance is assigned its appropriate name and coordinates and is displayed on the screen.
    The class also keeps track of all the successfully guessed parts to support the Reset feature.
    """

    # List to track all guessed C8 Carbine parts
    guessed_parts_list = []

    def __init__(self,part,x_coordinate,y_coordinate):
        """
        Creates an instance of the firearm part label after the user guesses it correctly.

        :param part: The name of the successfully guessed firearm part.
        :param x_coordinate: The horizontal position on the screen where the label will appear.
        :param y_coordinate: The vertical position on the screen where the label will appear.

        :return: None
        """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_coordinate, y_coordinate)
        self.write(part, True, align="left", font=("Arial", 11, "normal"))
        Parts.guessed_parts_list.append(self)

    @classmethod
    def reset_parts(cls):
        """
        Remove all visible labels on the screen and empties the guessed parts list.

        :return: None
        """
        for part in cls.guessed_parts_list:
            part.clear()
        cls.guessed_parts_list = []
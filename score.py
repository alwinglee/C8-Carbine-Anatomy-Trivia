import pandas
from turtle import Turtle
import os

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.lowest_time = "--:--"
        self.hideturtle()
        self.goto(-541, 290)
        self.check_file_exists()

    def display_score(self):
        self.clear()
        self.write(f"Record | {self.lowest_time}", move=False, align="left", font=("Arial", 30, "bold"))

    def check_file_exists(self):
        file = "C8_Carbine_Score.csv"
        if not os.path.exists(file):
            default_time = {
                "Time": ["--:--"],
                "Seconds": [float('inf')]
            }
            pandas.DataFrame(default_time).to_csv("C8_Carbine_Score.csv", index=False)
        else:
            data = pandas.read_csv("C8_Carbine_Score.csv")
            self.lowest_time = data.loc[0,"Time"]
        self.display_score()

    def update_score(self,minute,seconds):
        total_seconds = minute*60+seconds
        data = pandas.read_csv("C8_Carbine_Score.csv")
        if ( total_seconds< data.loc[0,"Seconds"]):
            self.lowest_time = f"{minute:02}:{seconds:02}"
            self.display_score()
            data.loc[0,"Time"] = self.lowest_time
            data.loc[0,"Seconds"] = total_seconds
            data.to_csv("C8_Carbine_Score.csv",index=False)









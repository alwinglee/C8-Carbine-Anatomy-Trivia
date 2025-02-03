from turtle import Turtle
from score import Score

class Timer(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.penup()
        self.hideturtle()
        self.goto(-541, 250)
        self.elapsed_time = 0
        self.time_minute = 0
        self.time_second = 0
        self.timer_on = False
        self.score = Score()
        self.start_timer()

    def update_timer(self):
        if self.timer_on:
            self.clear()
            self.time_minute=self.elapsed_time//60
            self.time_second=self.elapsed_time % 60
            self.write(f"Time | {self.time_minute:02}:{self.time_second:02}", move=False, align="left",
                       font=("Arial", 30, "bold"))
            self.elapsed_time += 1
            self.screen.ontimer(self.update_timer, 1000)

    def start_timer(self):
        if self.timer_on:
            return
        self.timer_on = True
        self.update_timer()

    def stop_timer(self):
        self.timer_on = False
        self.score.update_score(self.time_minute, self.time_second)

    def reset_timer(self):
        self.elapsed_time = 0
        self.time_minute = 0
        self.time_second = 0















from turtle import Turtle


class Point(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = -1
        self.goto(0, 300)
        self.print_score()
        self.hideturtle()

    def print_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=('Arial', 24, 'normal'))


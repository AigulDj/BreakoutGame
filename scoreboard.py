from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(250, 220)
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))

    def brick_bounce(self):
        self.score += 1
        self.update_scores()
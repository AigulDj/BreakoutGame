from turtle import Turtle
from playsound import playsound

class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__(shape='square')
        self.penup()
        self.goto(position)
        self.color('white')
        self.shapesize(0.5, 7)

    def go_right(self):
        x_cor = self.xcor() + 30
        playsound('sound/paddle.mp3', False)
        if self.xcor() <= 260:
            self.goto(x_cor, self.ycor())

    def go_left(self):
        x_cor = self.xcor() - 30
        playsound('sound/paddle.mp3', False)
        if self.xcor() >= -265:
            self.goto(x_cor, self.ycor())

    def dragging(self, x, y):
        self.ondrag(None)
        #if 260 >= self.xcor() >= -265:
        self.goto(x, self.ycor())
        self.ondrag(self.dragging)
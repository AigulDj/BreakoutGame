from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='images/ball_s.gif')
        self.penup()
        self.sety(-210)
        self.x_move = 10
        self.y_move = 10
        self.time_sleep = 0.2

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.hideturtle()
        self.goto((0, -210))
        self.showturtle()

    def speed_up(self):
        self.time_sleep -= 0.05
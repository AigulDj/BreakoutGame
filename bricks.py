from turtle import Turtle
from random import choice


class Brick(Turtle):
    colors = ['#24A19C', '#CAF7E3', '#F54291', '#325288', '#D96098', '#FF5959', '#D06224', '#533535', '#FFC947', '#F3F1F5']

    def __init__(self, x, y):
        super(Brick, self).__init__(shape='square')
        self.penup()
        self.speed('fastest')
        self.goto(x, y)
        self.shapesize(0.8, 3, 5)  # obj = 20px = ratio 1
        self.color(choice(self.colors))
        self.bricks_lst = []

    def build_wall(self):
        y1 = 200  # Build new line of bricks
        for i in range(5):
            if i % 2 == 0:
                x1 = -310
                n = 10
            else:
                x1 = -275
                n = 9
            for _ in range(n):
                self.bricks_lst.append(Brick(x1, y1))
                x1 += 68
            y1 -= 24

    def hide(self):
        #self.speed('slow')
        self.hideturtle()
        self.goto(0, -800)
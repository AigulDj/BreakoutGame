from turtle import Turtle


class Livesboard(Turtle):
    def __init__(self):
        super(Livesboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.lives = 3
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.goto(-260, 220)
        self.write(f'Lives: {self.lives}', align='center', font=('Courier', 20, 'normal'))

    def reduce_lives(self):
        self.lives -= 1
        self.update_lives()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over!\n', align='center', font=('Courier', 30, 'normal'))
        self.write(f'Press "space" button to continue.', align='center', font=('Courier', 20, 'normal'))

    def start_game(self):
        self.goto(0, 0)
        self.write(f'Hello there!\n', align='center', font=('Courier', 30, 'normal'))
        self.write(f'Press "space" button to continue.', align='center', font=('Courier', 20, 'normal'))


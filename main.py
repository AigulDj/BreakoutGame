from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
from livesboard import Livesboard
import time
from playsound import playsound

screen = Screen()
screen.setup(700, 500)
screen.bgcolor('black')
screen.title('Breakout Game')
#screen.bgpic('images/brick1.gif')
screen.register_shape('images/ball_s.gif')
screen.register_shape('images/brick1.gif')
screen.tracer(0)  # Helped to prevent slow motion effect

paddle = Paddle((0, -230))
ball = Ball()
scoreboard = Scoreboard()
livesboard = Livesboard()
brick = Brick(-900, 0)
brick.build_wall()
livesboard.start_game()


def play():
    playsound('sound/next-level.wav', False)
    game_on = True
    livesboard.update_lives()
    scoreboard.update_scores()
    while game_on:
        time.sleep(ball.time_sleep)
        ball.move()
        screen.update()  # Helped to prevent slow motion effect

        # Collision with W,E & N walls
        if ball.xcor() > 320 or ball.xcor() < -330:
            playsound('sound/jump-coin.wav', False)
            ball.bounce_x()
        if ball.ycor() > 230:
            ball.bounce_y()
            playsound('sound/wall-bounce.mp3', False)

        # Ball misses
        if ball.ycor() < -250:
            playsound('sound/death.wav', False)
            livesboard.reduce_lives()
            time.sleep(2)
            ball.reset_position()
            paddle.goto(0, -230)
            if livesboard.lives == 0:
                playsound('sound/game-over.wav', False)
                scoreboard.score = 0
                livesboard.lives = 3
                brick.build_wall()
                livesboard.game_over()
                game_on = False

        # Collision with paddle
        if ball.ycor() < -209 and ball.distance(paddle) < 75:
            ball.bounce_y()
            playsound('sound/jump.wav', False)

        # Collision with bricks
        for b in brick.bricks_lst:
            if ball.ycor() >= b.ycor() - 30 and ball.distance(b) < 40:
                if b.xcor() + 70 >= ball.xcor() >= b.xcor() - 70 and ball.distance(b) < 40:
                    playsound('sound/success-beeps.wav', False)
                    #ball.bounce_x()
                    ball.bounce_y()
                    b.hide()
                    brick.bricks_lst.remove(b)
                    scoreboard.brick_bounce()

        # Level passed, speed up
        if len(brick.bricks_lst) == 0:
            playsound('sound/next-level.wav', False)
            ball.reset_position()
            paddle.goto(0, -230)
            brick.build_wall()
            if ball.time_sleep > 0.05:
                ball.speed_up()


screen.onkeypress(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_right, 'Right')
screen.onkey(play, 'space')
paddle.ondrag(paddle.dragging)
screen.listen()

screen.mainloop()
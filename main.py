from turtle import Screen
from paddle import Paddle
from boxs import Boxs
from ball import Ball
from scoreboard import Scoredboard
import time


#create  a screen
screen = Screen()
screen.bgcolor("purple")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

#create and move a padddle
paddle = Paddle()

#create the ball nd mke it move
ball = Ball()

scoreboard = Scoredboard(lives=5)
boxs= Boxs() 

#yellow_paddle = Yellow()
#green_paddle = Green()




screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


#create a random paddle to entire screen
# detcet collision with the  wall and bounce
# detcet collision with the  random paddles and bounce
#detectwhwn the paddle misses
#keep the score
screen.exitonclick()
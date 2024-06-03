from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5 , stretch_wid=1)
        self.penup()
        self.goto(0, -300)

    
    def go_right(self):
        new_x = self.xcor() + 20
        self.setx( new_x)

    def go_left(self):
        new_x = self.xcor() - 20
        self.setx( new_x)


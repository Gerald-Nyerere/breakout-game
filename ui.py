from turtle import Turtle
import random
import time

COLORS_LIST = ['Blue', 'Green', 'Red', 'Orange', 'Yellow', 'Brown', 'Pink', 'Purple', 'Aqua', 'Black', 'Gray',
               'White', 'tomato', 'light sky blue',  'Cyan', 'Azure', 'Coral', 'Rust', 'Crims' ]



class Ui(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(COLORS_LIST))
        self.header()


  

    def header(self):
        self.clear()
        self.goto(x=0, y=-150)
        self.write('Breakout', align="center", font=("Courier", 80, "normal"))
        self.goto(x=0, y=-180)
        self.write('Press space to pauce or resume', align="center", font=("Courier", 80, "normal"))
        

    def change_color(self):
        self.clear()
        self.color(random.choice(COLORS_LIST))
        self.header()
    
    def paused(self):
        self.clear()
        self.change_color()
        time.sleep(0.5)

    def game_over(self, win):
        self.clear()
        if win == True:
            self.write("You won the game",  align="center", font=("Courier", 80, "normal"))
        else:
            self.write("Game is Over",  align="center", font=("Courier", 80, "normal"))
    
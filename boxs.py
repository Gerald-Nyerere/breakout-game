from turtle import Turtle
import random

COLORS_LIST = ['Blue', 'Green', 'Red', 'Orange', 'Yellow', 'Brown', 'Pink', 'Purple', 'Aqua', 'Black', 'Gray',
               'White', 'tomato', 'light sky blue',  'Cyan', 'Azure', 'Coral', 'Rust', 'Crims' ]

weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3, 1, 1, 1, 4, 1, 3, 2, 2, 1, 2, 1, 2, 1, 2, 1]

class Box(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS_LIST))
        self.shapesize(stretch_len=3 , stretch_wid=1.5)
        #self.penup()
        self.goto(x=x_cor, y=y_cor)

        self.quantity = random.choice(weights)
        
        #defining borders of the box
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15
        


class Boxs:
    def __init__(self):
        self.y_start = 0
        self.y_end = 300
        self.boxs = []
        self.create_all_lanes()
    
    def create_lane(self, y_cor):
        for i in range(-570, 570, 63):
            box = Box(i, y_cor)
            self.boxs.append(box)
    
    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)
    
   


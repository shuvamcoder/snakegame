from turtle import Turtle
import random


class Food(Turtle): # Turtle is the super class

    def __init__(self):
        super().__init__() # calling the super class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # instead of 20 by 20, we will use 10 by 10 circle
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270) # maximum is 300 by 300
        self.goto(random_x, random_y)
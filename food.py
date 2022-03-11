from turtle import Turtle
import random



 
class Food(Turtle):

    def __init__(self):
        super().__init__()
        #self.shape(shapes)
        self.penup()
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        #self.color("red")
        self.speed("fastest")
        self.refresh()

    #create pieces to food ramndom
    def refresh(self):
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x,random_y)
        clors = random.choice(["#2ef8a0","#ff0534","#c2ff05","#FF1493","#8ae0db","#FFFFFF","#fea444"])
        self.color(clors)
        shapes = random.choice(["square", "triangle", "circle"])
        self.shape(shapes)
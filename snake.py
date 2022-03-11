from turtle import Turtle,  forward


#build body to snake
STARTING_POSITION = [(-220,0),(-240,0),(-260,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180



class Snake:
    #constructor
    def __init__(self):
        #save to segment to sanake
        self.segments = []
        #Metodo que crea la serpiente
        self.create_snake()
        #head to sanke
        self.head = self.segments[0]
       
        
    def create_snake(self):
        for position in STARTING_POSITION:   #cycle for create a snake
            self.add_segment(position)
            

    def add_segment(self,position):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.color("#52c234")
        snake_segment.goto(position)
        self.segments.append(snake_segment) 


    def extend(self):
        self.add_segment(self.segments[-1].position())    


    def move(self):
        for seg_num in range(len(self.segments) -1 ,0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)
    

    def up(self):
        if self.head.heading() != DOWN:
          self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)    

    
        
        
    
    




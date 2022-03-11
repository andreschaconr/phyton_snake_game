from turtle import Turtle, color
import turtle


class Board(Turtle):

     def __init__(self):

        super().__init__()
        self.score = 0
        self.color("white")
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(200, -290)
        self.write(f"Score :  {self.score}",align="center", font=("Metrophobic", 18))
        self.UpdateScore
       



     def UpdateScore(self):
          self.write(f"Score :  {self.score}",align="center", font=("Metrophobic", 18))


     def IncreaseScore(self):
         self.clear()
         self.score += 1
         self.UpdateScore()


     def game_over(self):
        self.clear() 
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=("Metrophobic", 35))
        #self.goto(0,-30)  
        #self.write("press enter to play again",align="center", font=("Metrophobic", 18))
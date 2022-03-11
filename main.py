from shutil import move
from turtle import Turtle, Screen, forward, xcor
import time
from snake import Snake
from food import Food
from board import Board



#create board to game.
screen = Screen()
screen.setup(width=600,height=600)# create size to screen 
screen.bgcolor("#021504")
screen.title("snake game")
screen.tracer(0)

#animation sanake
game_is_on = True
#create object food
food = Food()
#create snake
newsnake= Snake()

#create board to put score
board= Board()

#metodo to action keys
screen.listen()
screen.onkey(newsnake.up,"Up")
screen.onkey(newsnake.up,"w")

screen.onkey(newsnake.right,"Right")
screen.onkey(newsnake.right,"d")

screen.onkey(newsnake.down,"Down")
screen.onkey(newsnake.down,"s")

screen.onkey(newsnake.left,"Left")
screen.onkey(newsnake.left,"a")









while game_is_on:
    screen.update()
    time.sleep(0.15) #speed to snake
    newsnake.move()
    


    if newsnake.head.distance(food) < 15:
        food.refresh()
        board.IncreaseScore()
        newsnake.extend()


    #wall colision
    if newsnake.head.xcor() > 290 or newsnake.head.xcor() < -290 or newsnake.head.ycor() > 290 or newsnake.head.ycor() < -290 : 
        game_is_on = False ##crete a fuction
        board.game_over()

    for segment in newsnake.segments:  #optimize whit slice
        if segment == newsnake.head:
            pass
        elif newsnake.head.distance(segment)  < 10:
            game_is_on = False
            board.game_over()




screen.exitonclick()
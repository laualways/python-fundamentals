import turtle as t
from turtle import Screen

tim = t.Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

# Example of turtle moving forward by clicking "space":

# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()
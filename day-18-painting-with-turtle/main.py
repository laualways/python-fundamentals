from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("SpringGreen4")

# this is to draw a square with a for loop:
for _ in range(4):
    tim.forward(100)
    tim.right(90)


import heroes
print(heroes.gen())

# this is to draw a dashed line:
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


















screen = Screen()
screen.exitonclick()
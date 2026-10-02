import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# With function:

# tim = Turtle()
# tom = Turtle()
# tum = Turtle()
#
# def turtle_type(turtle):
#     turtle.shape("square")
#     turtle.color("white")
#
# turtle_type(tim)
# turtle_type(tom)
# turtle_type(tum)
#
# tom.setposition(-20, 0)
# tum.setposition(-40, 0)


# With tuple and for loop:

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)



















screen.exitonclick()
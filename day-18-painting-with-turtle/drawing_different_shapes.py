import random
from turtle import Turtle, Screen

tim = Turtle()

num_sides = 5

colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink",
    "cyan", "magenta", "turquoise", "gold", "violet", "maroon", "navy",
    "skyblue", "lime", "darkgreen", "chocolate", "brown", "gray",
           "hotpink", "deepskyblue", "gold", "forestgreen", "turquoise"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)




screen = Screen()
screen.exitonclick()
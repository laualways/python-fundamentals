import random
import turtle as t
from time import time

tom = t.Turtle()
t.colormode(255)
tom.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

# MY SOLUTION
# for _ in range(36):
#     tom.color(random_color())
#     tom.circle(100)
#     tom.left(10)
#     tom.tilt(10)

def draw_spirograph(size_of_gap):
    # Calculates exact steps needed for a full 360° circle based on the gap size,
    # then draws circles and shifts the absolute heading incrementally.
    for _ in range(int(360/size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
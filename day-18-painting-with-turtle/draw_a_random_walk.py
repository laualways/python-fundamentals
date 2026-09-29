import random
import turtle as t  # Import the whole module with an alias to have everything ready with 't.'

tom = t.Turtle()

colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink",
    "cyan", "magenta", "turquoise", "gold", "violet", "maroon", "navy",
    "skyblue", "lime", "darkgreen", "chocolate", "brown", "gray",
           "hotpink", "deepskyblue", "gold", "forestgreen", "turquoise"]

directions = [0, 90, 180, 270]
tom.width(20)
tom.speed("fast")

for _ in range(200):
    tom.color(random.choice(colours))
    tom.forward(50)
    tom.setheading(random.choice(directions)) # Set absolute direction (0=East, 90=North, 180=West, 270=South)



screen = t.Screen()
screen.exitonclick()
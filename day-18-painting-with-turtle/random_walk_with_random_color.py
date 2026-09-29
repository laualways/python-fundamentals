import random
import turtle as t  # Import the whole module with an alias to have everything ready with 't.'

tom = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

directions = [0, 90, 180, 270]
tom.width(20)
tom.speed("fast")

for _ in range(200):
    tom.color(random_color())
    tom.forward(50)
    tom.setheading(random.choice(directions)) # Set absolute direction (0=East, 90=North, 180=West, 270=South)



screen = t.Screen()
screen.exitonclick()
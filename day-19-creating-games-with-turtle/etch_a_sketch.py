import turtle as t

tom = t.Turtle()
tom.shape("turtle")
screen = t.Screen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def move_right():
    tom.right(10)

def move_left():
    tom.left(10)

def clear_all():
    tom.clear()
    tom.penup()
    tom.home() # Moves turtle to the original position point but need penup e pendown to don't draw weird lines
    tom.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey( clear_all, "c")
screen.exitonclick()




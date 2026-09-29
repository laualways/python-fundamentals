# This is needed to get the colors from an image in RGB format:
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random

tom = t.Turtle()
t.colormode(255)



color_list = [(250, 151, 58), (139, 49, 106), (164, 169, 38), (244, 80, 57),
 (3, 143, 57), (216, 235, 231), (241, 66, 140), (2, 143, 184), (244, 99, 161),
 (162, 55, 52), (48, 203, 227), (249, 221, 227), (254, 230, 0), (21, 165, 126),
 (246, 225, 40), (213, 238, 242), (28, 196, 219), (118, 183, 146), (235, 164, 192)]



tom.speed("fast")
tom.penup()
x = -200
y = -200

for _ in range(10):
    for _ in range(10):
        tom.setpos(x, y)
        tom.dot(10, random.choice(color_list))
        x += 50
    y += 50
    x = -200
tom.hideturtle()





screen = t.Screen()
screen.exitonclick()






















screen = t.Screen()
screen.exitonclick()
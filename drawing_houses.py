import turtle
import random
turtle.speed(10)
def draw_house(size, roof_color, wall_color):
    turtle.pendown()
    turtle.begin_fill()
    for x in range(4):
        turtle.color(wall_color)
        turtle.fd(size)
        turtle.lt(90)
    turtle.end_fill()
    turtle.lt(90)
    turtle.fd(size)
    turtle.rt(90)
    turtle.begin_fill()
    for x in range(3):
        turtle.color(roof_color)
        turtle.fd(size)
        turtle.lt(120)
    turtle.end_fill()
    turtle.penup()

draw_house(100, "black", "red")
turtle.goto(110,0)
draw_house(50, "blue", "grey")
turtle.goto(170,0)
draw_house(75, "black", "black")
turtle.goto(-135,0)
draw_house(125, (random.random(), random.random(),random.random()), (random.random(), random.random(),random.random()))
turtle.exitonclick()

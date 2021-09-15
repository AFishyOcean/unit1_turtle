import turtle
turtle.speed(10)
turtle.hideturtle()
turtle.color("blue")
turtle.rt(90)
for x in range(12):
    for x in range(6):
        turtle.fd(100)
        turtle.rt(60)
    turtle.rt(30)
turtle.color("black")
turtle.penup()
turtle.goto(-120, 0)
turtle.pendown()
turtle.circle(120)

turtle.exitonclick()
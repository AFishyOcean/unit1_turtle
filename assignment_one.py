import turtle
turtle.speed(10)
turtle.hideturtle()


# design 1
turtle.penup()
turtle.goto(-200, 200)
turtle.color("blue")
turtle.pendown()
turtle.rt(90)
for x in range(12):
    for x in range(6):
        turtle.fd(100)
        turtle.rt(60)
    turtle.rt(30)
turtle.color("black")
turtle.penup()
turtle.goto(-320, 200)
turtle.pendown()
turtle.circle(120)

# design 2
turtle.penup()
turtle.goto(200, 200)
turtle.color("red")
turtle.pendown()
turtle.rt(90)
for x in range(24):
    for x in range(4):
        turtle.fd(100)
        turtle.rt(90)
    turtle.rt(15)
turtle.color("purple")
for x in range(12):
    for x in range(3):
        turtle.fd(100)
        turtle.rt(120)
    turtle.rt(30)

# design 3
turtle.penup()
turtle.goto(-200, -200)
turtle.color("green")
turtle.pendown()
turtle.rt(90)
for x in range(18):
    for x in range(8):
        turtle.fd(50)
        turtle.rt(45)
    turtle.rt(20)
turtle.color("black")
for x in range(6):
    for x in range(5):
        turtle.fd(100)
        turtle.rt(144)
    turtle.rt(60)
turtle.penup()

turtle.exitonclick()
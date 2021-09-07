import turtle
turtle.hideturtle()
turtle.speed(5)
# goto for spacing shapes
turtle.penup()
turtle.goto(50,100)
turtle.pendown()
# square
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
# goto
turtle.penup()
turtle.goto(150,-100)
turtle.pendown()
# circle
turtle.circle(50)
# goto
turtle.penup()
turtle.goto(-50,-150)
turtle.pendown()
# triangle
turtle.left(90)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
# goto
turtle.penup()
turtle.goto(-75,0)
turtle.pendown()
# pentagon
turtle.forward(75)
turtle.right(72)
turtle.forward(75)
turtle.right(72)
turtle.forward(75)
turtle.right(72)
turtle.forward(75)
turtle.right(72)
turtle.forward(75)
turtle.right(72)
# view product
turtle.exitonclick()

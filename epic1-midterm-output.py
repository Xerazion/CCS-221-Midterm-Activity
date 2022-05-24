import turtle
turtle.bgcolor("black")

t = turtle.Turtle()
t.hideturtle()
t.pensize(3)
t.speed(0)
t.penup()
t.goto(-95,0)
t.pendown()
turtle.colormode(255)


for i in range(152):
    t.color(0,225-i,0+i)
    t.forward(i*5)
    t.circle(220,54)
    t.right(150)

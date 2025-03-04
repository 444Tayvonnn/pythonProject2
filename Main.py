import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('tan')

t = turtle.Turtle()


t.setheading(135)
# square
t.fillcolor("cyan")
t.begin_fill()
t.penup()
t.goto(0,0)
t.pendown()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.setheading(45)
# square 2
t.fillcolor("brown")
t.begin_fill()
t.penup()
t.goto(0,0)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()


turtle.done()
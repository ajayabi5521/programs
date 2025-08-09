import turtle
def draw_arrow(pen):
    # arrow
    pen.pendown()
    pen.begin_fill()
    pen.backward(80)
    pen.left(42)
    pen.forward(147)
    pen.right(83)
    pen.forward(140)
    pen.forward(227)
    pen.end_fill()


avengers = turtle.Turtle()
avengers.speed(1)
avengers.pensize(10)
avengers.pencolor("red")
avengers.penup()    

draw_arrow(avengers)



avengers.penup()

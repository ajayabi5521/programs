import turtle
for i in [-190,-180,-170,-160, -150]:
    turtle.penup()
    turtle.setposition(0,i)
    turtle.pendown()
    for i in["blue","green","pink","orange","red"]:
        turtle.pensize(5)
        turtle.pencolor("white")
        turtle.fillcolor(i)  # Set only the fill color
        for i in[500,400,300,200,100]:
                turtle.begin_fill()
                turtle.speed(20)
                turtle.circle(i)
                turtle.end_fill()

turtle.done()



import turtle
import time
import threading
def symbol():
    turtle.bgcolor("black")
    turtle.penup()
    turtle.setposition(0,-200)
    turtle.pendown()
    turtle.speed(10)
    turtle.pensize(5)
    turtle.color("lightblue")
    turtle.pencolor("gray")
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()

    turtle.penup()
    turtle.hideturtle()
    turtle.home()
    turtle.color("silver")
    turtle.pencolor("gray")
    turtle.begin_fill()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(200)
    turtle.backward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.backward(200)
    turtle.right(240)
    turtle.forward(200)
    turtle.left(170)
    turtle.forward(190)
    turtle.right(41.5)
    turtle.forward(182)
    turtle.left(162)
    turtle.forward(182)
    turtle.right(40)
    turtle.forward(185)
    turtle.left(160)
    turtle.forward(184)
    turtle.right(41.5)
    turtle.forward(184)
    turtle.end_fill()

def company(name):
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.pencolor("white")
    pen.penup()
    pen.goto(-200,230)
    pen.pendown()
    pen.speed(5)
    for i in name:
        pen.write(i,font=("Arial",24,"bold"))
        pen.forward(25)
        time.sleep(0.2)
  
    time.sleep(0.1)




symbol()
company("WELCOME TO BENZ LOGO")






turtle.done()




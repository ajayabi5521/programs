import turtle
import time

turtle.penup()
turtle.setposition(70,-270)
turtle.pendown()
turtle.speed(10)
turtle.bgcolor("lightpink")
turtle.pencolor("gray")
turtle.pensize(10)
turtle.fillcolor("lightblue")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()
turtle.setposition(70,-270)
'''turtle.left(60)

turtle.forward(340)
turtle.right(60)
turtle.backward(340)
turtle.goto(70,-270)
turtle.pendown()'''
turtle.left(90)
turtle.forward(400)
turtle.backward(180)
turtle.left(120)
turtle.forward(200)
turtle.backward(200)
turtle.left(120)
turtle.forward(200)
def write(name):
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-200,200)
    pen.pendown()
    pen.speed(5)
    for i  in name:
           if i=="I" :
                  
                  pen.write(i,font=("Times New Roman",25,"normal"))
                 
                  pen.forward(18)
                  time.sleep(0.2)
           else:
                  pen.write(i,font=("Times New Roman",25,"normal"))
                 
                  pen.forward(30)
                  time.sleep(0.2)
         
                  
    turtle.done()       
write("THIS IS PEACE SYMBOL")       






    
turtle.done()

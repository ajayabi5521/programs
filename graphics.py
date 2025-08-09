# import package
import turtle
a=100
b=0
for i in range(0,1):
    turtle.goto(a,a)
    turtle.goto(a,-a)
    
    turtle.goto(b,b)
    turtle.goto(-a,-a)
    turtle.goto(-a,a)
    turtle.home()
    turtle.goto(b,a)
    turtle.goto(b,-a)
    turtle.goto(-a,b)
    turtle.goto(a,b)
    turtle.goto(b,a)
    turtle.goto(-a,b)
    turtle.goto(a,b)
    turtle.goto(b,-a)
    turtle.goto(a,-a)
    turtle.goto(a,a)
    turtle.goto(-a,a)
    turtle.goto(-a,-a)
    turtle.goto(b,-a)
    turtle.goto(0,0)
    turtle.goto(0,100)
    turtle.goto(-100,200)
    turtle.goto(0,300)
    turtle.goto(100,200)
    turtle.goto(0,100)
    turtle.goto(0,300)
    turtle.goto(100,300)
    turtle.goto(100,100)
    turtle.goto(-100,100)
    turtle.goto(-100,300)
    turtle.goto(100,100)
    turtle.goto(-100,100)
    turtle.goto(100,300)
    turtle.goto(100,200)
    turtle.goto(-100,200)
    turtle.goto(-100,300)
    turtle.goto(0,300)
   

 
    
    



#turtle.home()

# stop execution
turtle.done()
'''
import tkinter as tk

def move_ball():
    canvas.move(ball, 2, 0)  # move ball (x=2, y=0)
    canvas.after(20, move_ball)  # repeat every 20ms

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

ball = canvas.create_oval(10, 100, 30, 120, fill="blue")
move_ball()

root.mainloop()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

def update(frame):
    line.set_ydata(np.sin(x + frame / 10))
    return line,

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()'''



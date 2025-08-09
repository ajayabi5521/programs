
from tkinter import*
from random import randint
def move():
    num =randint(0,20)
    print(num)
   
    canvas.move(ball,5,num)
    root.after(50,move)
root=Tk()
root.title("ball game")
root.resizable(False,False)
canvas=Canvas(root,width=300,height=300)
canvas.pack()
ball=canvas.create_oval(10,10,20,20,fill="red")
canvas.create_rectangle(3,3,300,300)
root.after(10,move)
root.mainloop()
'''
import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

ball = canvas.create_oval(10, 10, 30, 30, fill='blue')
dx = 1  # slow speed

def move_ball():
    canvas.move(ball, dx, 0)
    window.after(30, move_ball)  # Higher value = slower animation

move_ball()
window.mainloop()'''


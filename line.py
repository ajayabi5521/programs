import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle for logo
logo = turtle.Turtle()
logo.hideturtle()
logo.speed(0)
logo.pensize(5)

# Turtle for text
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(-200, 230)
pen.pendown()

text = "WELCOME TO BENZ SYMBOL"
text_index = 0

# --- Draw Logo Step-by-Step ---
logo_steps = []

def prepare_logo_steps():
    logo.penup()
    logo.setposition(0, -200)
    logo.pendown()
    logo.color("lightblue")
    logo.pencolor("gray")
    logo.begin_fill()
    logo.circle(200)
    logo.end_fill()

    logo.penup()
    logo.home()
    logo.color("silver")
    logo.pencolor("gray")
    logo.begin_fill()
    logo.pendown()
    logo_steps.extend([
        lambda: logo.left(90) or logo.forward(200),
        lambda: logo.backward(200),
        lambda: logo.left(120) or logo.forward(200),
        lambda: logo.backward(200),
        lambda: logo.right(240) or logo.forward(200),
        lambda: logo.left(170) or logo.forward(190),
        lambda: logo.right(41.5) or logo.forward(182),
        lambda: logo.left(162) or logo.forward(182),
        lambda: logo.right(40) or logo.forward(185),
        lambda: logo.left(160) or logo.forward(184),
        lambda: logo.right(41.5) or logo.forward(184),
        lambda: logo.end_fill()
    ])

prepare_logo_steps()

def draw_logo_step():
    if logo_steps:
        step = logo_steps.pop(0)
        step()
        screen.ontimer(draw_logo_step, 50)  # Delay between steps

def write_text_step():
    global text_index
    if text_index < len(text):
        pen.write(text[text_index], font=("Arial", 24, "bold"))
        pen.forward(25)
        text_index += 1
        screen.ontimer(write_text_step, 200)  # Delay between letters

# Start both animations
draw_logo_step()
write_text_step()

turtle.done()

import turtle as t
from turtle import Turtle, Screen
from random import choice, randint


t.colormode(255)
timmy = Turtle()
timmy.shape('classic')
timmy.pensize(7)
timmy.speed('fastest')

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b) 


directions = [0, 90, 180, 270]

def walk(turtle, step_size):
    turtle.setheading(choice(directions))
    turtle.forward(step_size) 

for _ in range(200):
    timmy.color(random_color())
    walk(timmy, 20)         


screen = Screen()
screen.exitonclick()
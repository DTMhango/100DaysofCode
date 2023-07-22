
import turtle as t
from turtle import Turtle, Screen
from random import choice, randint


t.colormode(255)
timmy = Turtle()
timmy.shape('classic')
timmy.pensize(2)
timmy.speed('fastest')

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b) 


angle = 10
for _ in range(int(360/angle)):
    timmy.color(random_color())
    timmy.circle(100)
    current_heading = timmy.heading()
    timmy.setheading(current_heading + angle)



screen = Screen()
screen.exitonclick()
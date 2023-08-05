import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor("black")
t.speed(0.1)
n = 100
h = 0


for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    t.color(c)

    t.left(1)
    t.fd(0)
    turtle.hideturtle

    for j in range(2):
        t.left(1)
        t.circle(260)

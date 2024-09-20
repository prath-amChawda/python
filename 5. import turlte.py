import turtle
import colorsys

screen= turtle.Screen()
screen.setup(width=5,height=4)
screen.bgcolor("white")

turtle.speed(2)
turtle.hideturtle()

n=360
hue=0
for i in range(360):
   color=colorsys.hsv_to_rgb(hue,1.0,1.0)
   turtle.pencolor(color)
   turtle.width(1 // 100+1)
   turtle.forward(1)
   turtle.right(50)
   hue+= 1/n

turtle.hideturtle()
turtle.done()
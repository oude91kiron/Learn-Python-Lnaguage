

import turtle
window = turtle.Screen()
window.bgcolor("black")

def draw_rhombus(turtle, size, small_angle):
    for i in range(2):
        turtle.forward(size)
        turtle.right(small_angle)
        turtle.forward(size)
        turtle.right((360-2*small_angle)//2)


def draw_flower(turtle, size, angle):
    for i in range(360//angle):  
        draw_rhombus(turtle, size, 60)
        turtle.right(angle)
    turtle.right(90)            # draws the leg of the flower
    turtle.forward(size*3)
    window.exitonclick()       


myTurtle = turtle.Turtle("arrow")
myTurtle.color("green")
myTurtle.shape("arrow")
myTurtle.speed(7)


draw_flower(myTurtle, 100, 3)









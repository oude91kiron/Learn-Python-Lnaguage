
import turtle

def draw_square():
	window = turtle.Screen()  
	window.bgcolor("green")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(0.7)
	for i in range(0,4):
		brad.forward(200)
		brad.right(90)
	window.exitonclick()

print draw_square()
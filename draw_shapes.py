
import turtle

def draw_square(turtle4):
	for i in range(0, 4):
	    turtle4.forward(100)
	    turtle4.right(90)


def draw_hexagon(arrow6):
	for i in range(0, 8):
		arrow6.forward(100)
		arrow6.left(45)

def draw_triangle(turtle3):
	turtle3.forward(150)
	turtle3.left(120)
	turtle3.forward(150)
	turtle3.left(120)
	turtle3.forward(150)

def draw_circle(angie):
	angie.circle(100)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("white")
	# Create the object brad - Draws a square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("black")
	brad.speed(0.7)
	draw_square(brad)

	#Create the object Angie - Draws a circle
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("green")
	draw_circle(angie)
	


	#Create the object Angle - Draws a hexagon
	angle = turtle.Turtle()
	angle.shape("classic")
	angle.color("blue")
	angle.speed(0.7)
	draw_hexagon(angle)


	#Create the object Tree - Draws a triangle4
	tree = turtle.Turtle()
	tree.shape("classic")
	tree.color("yellow")
	tree.speed(0.7)
	draw_triangle(tree)




	window.exitonclick()


print draw_art()
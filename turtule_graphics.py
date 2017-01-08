import turtle

def draw_sqaure(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    #create the turtle Brad- Draw a sqare
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("pink")
    brad.speed(3)
    for i in range(1,37):
        
        draw_sqaure(brad)
        brad.right(10)
        
    #create the turtle Angie - Draw a circle
    #angie = turtle.Turtle()
    #angie.circle(100)

    window.exitonclick()


draw_art()

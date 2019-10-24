import turtle


def main():
   t=turtle.Turtle()
   t.hideturtle()
   roof(t)
   house(t)
   door(t)
   windows(t)
  


def roof(t):
    t.pencolor("black")
    t.pensize(2)
    t.fillcolor("brown")
    t.up
    t.begin_fill()
    t.goto(-100,0)
    t.down()
    t.goto(100,0)
    t.goto(0,150)
    t.goto(-100,0)
    t.end_fill()
    t.up()
#Roof is a triangle with black outline and brown fill.  The base of the triangle has a width of 200 pixels and the height is 150 pixels
    return t


def house(t):
    t.pencolor("black")
    t.pensize(2)
    t.fillcolor("red")
    t.up
    t.begin_fill()
    t.goto(-80,0)
    t.down()
    t.goto(80,0)
    t.goto(80,-200)
    t.goto(-80,-200)
    t.goto(-80,0)
    t.end_fill()
    t.up()
#House is a black outlined red filled rectangle that has a height of 200 pixels and a width of 160 pixels.
    return t

def door(t):
    t.pencolor("black")
    t.pensize(2)
    t.fillcolor("blue")
    t.up
    t.begin_fill()
    t.goto(25,-200)
    t.down()
    t.goto(25,-125)
    t.goto(-25,-125)
    t.goto(-25,-200)
    t.goto(25,-200)
    t.end_fill()
    t.up()
#Door is a black outlined blue filled rectangle with a width of 50 pixels and height of 75 pixels
    return t


def windows(t):
    t.pencolor("black")
    t.pensize(2)
    t.fillcolor("white")
    t.up
    t.begin_fill()
    t.goto(30,-30)
    t.down()
    t.goto(70,-30)
    t.goto(70,-70)
    t.goto(30,-70)
    t.goto(30,-30)
    t.end_fill()
    t.up()
    t.pencolor("black")
    t.pensize(2)
    t.fillcolor("white")
    t.up
    t.begin_fill()
    t.goto(-30,-30)
    t.down()
    t.goto(-70,-30)
    t.goto(-70,-70)
    t.goto(-30,-70)
    t.goto(-30,-30)
    t.end_fill()
    t.up()
#Windows are black outline white filled squares with a width of 50 pixels.
    return t



main()

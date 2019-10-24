
import turtle
t=turtle.Turtle()
t.hideturtle()

def main():
   t=turtle.Turtle()
   t.hideturtle()
   t=redsquare(t)
   t=bluesquare(t)
   t=purplesquare(t)
  


def redsquare(t):
    t.pencolor("red")
    t.pensize(5)
    t.up()
    t.goto(50,50)
    t.down()
    t.goto(50,50+100)
    t.goto(50+100,50+100)
    t.goto(50+100,50)
    t.goto(50,50)
    return t



def bluesquare(t):
    t.pencolor("blue")
    t.pensize(7)
    t.up()
    t.goto(63,63)
    t.down()
    t.goto(63+74,63)
    t.goto(63+74,63+74)
    t.goto(63,63+74)
    t.goto(63,63)
    t.up()
    return t


def purplesquare(t):
    t.pencolor("black")
    t.pensize(5)
    t.fillcolor("purple")
    t.up
    t.begin_fill()
    t.goto(76,76)
    t.down()
    t.goto(76+50,76)
    t.goto(76+50,76+50)
    t.goto(76,76+50)
    t.goto(76,76)
    t.end_fill()
    t.up()
    return t



main()

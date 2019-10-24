
import turtle 



def main():
    t=turtle.Turtle()
    t.hideturtle()

    #draw square
    t.pencolor("blue")
    t.up()
    t.goto(-100,50)
    t.down()
    t.goto(-100,200)
    t.goto(100,200)
    t.goto(100,50)
    t.goto(-100,50)
    #FILL square2
    t.fillcolor("green")
    t.up()
    t.begin_fill()
    t.goto(-100,50)
    t.goto(-100,-200)
    t.goto(100,-200)
    t.goto(100,-50)
    t.goto(-100,-50)
    t.end_fill()

    #circle out
    t.up()
    t.pencolor("red")
    t.pensize(5)
    t.goto(0,-50)
    t.down()
    t.circle(50)

    #inter circle
    t.up()
    t.pencolor("brown")
    t.goto(0,0)
    t.down()
    t.dot(100)


    #diamond
    t.pencolor("purple")
    t.pensize(10)
    t.up()
    t.goto(0,100)
    t.down()
    t.goto(-100,0)
    t.goto(0,-100)
    t.goto(100,0)
    t.goto(0,100)


    
main()
    

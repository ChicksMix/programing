import turtle




def main():
    
    t=turtle.Turtle()
    t.hideturtle()

    #blackline
    t.pencolor("black")
    t.pensize(5)
    t.up()
    t.goto(20,30)
    t.down()
    t.goto(80,90)
    t.up()


    
    #yellow dots
    t.up
    t.pencolor("yellow")
    t.goto(20,30)
    t.down()
    t.dot(15)
    t.up()
    t.goto(80,90)
    t.down()
    t.dot(15)
    t.up()

    #blueslant
    t.pencolor("blue")
    t.pensize(5)
    t.up
    t.goto(15,200)
    t.down()
    t.goto(150,200)
    t.up()

    #redcircle
    t.pencolor("red")
    t.up
    t.goto(70,150)
    t.down()
    t.dot(100)
    t.up()

    #bluedots
    t.pencolor("dark blue")
    t.up
    t.goto(200,50)
    t.down()
    t.dot(100)
    t.up()
    t.pencolor("blue")
    t.up
    t.goto(200,50)
    t.down()
    t.dot(50)
    t.up()

    #purpleline
    t.pencolor("purple")
    t.pensize(5)
    t.up()
    t.goto(-25,-55)
    t.down()
    t.goto(-80,-40)
    t.up()


    #violet
    t.up
    t.pencolor("violet")
    t.goto(-25,-55)
    t.down()
    t.dot(20)
    t.up()
    t.goto(-80,-40)
    t.down()
    t.dot(20)
    t.up()

    #green
    t.fillcolor("dark green")
    t.up()
    t.begin_fill()
    t.goto(-160,-160)
    t.goto(-160,-60)
    t.goto(-60,-60)
    t.goto(-60,-160)
    t.goto(-160,-160)
    t.end_fill()
    t.up()

    #orange
    t.fillcolor("orange")
    t.up()
    t.begin_fill()
    t.goto(50,-100)
    t.goto(50,-20)
    t.goto(130,-20)
    t.goto(130,-100)
    t.goto(50,-100)
    t.end_fill()
    t.up()
    #redborder
    t.pencolor("red")
    t.pensize(3)
    t.up()
    t.goto(50,-100)
    t.down()
    t.goto(50,-20)
    t.goto(130,-20)
    t.goto(130,-100)
    t.goto(50,-100)

    #righttri
    t.pencolor("magenta")
    t.pensize(5)
    t.up()
    t.goto(-100,50)
    t.down()
    t.goto(-40,50)
    t.goto(-100,110)
    t.goto(-100,50)
    #equaltri
    
    t.pencolor("cyan")
    t.pensize(5)
    t.up()
    t.goto(-150,150)
    t.down()
    t.goto(-50,150)
    t.goto(-100,250)
    t.goto(-150,150)

main()
    

import turtle


chs=["Chantilly","Chargers"]

def main():
    
    t=turtle.Turtle()
    t.hideturtle()
    t.pensize(5)
    t.pencolor("purple")
    t.speed(100)
    t.up()
    n=5
    drawStar(n,t)
    school(t,chs)


def drawStar(n,t):
    t.goto(-150,150)
    t.down()
    
    for i in range(5):
        t.forward(300)
        t.right(144)

def school(t,chs):
    t.up()
    t.goto(0,100)
    t.down()
    t.write(chs[0],align = "center", font=("OCR A Std",10,"bold"))
    t.up()
    t.goto(0,80)
    t.down()
    t.write(chs[1],align = "center", font=("OCR A Std",10,"bold"))
    

main()

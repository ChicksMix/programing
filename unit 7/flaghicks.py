#flag

import turtle

t=turtle.Turtle()


def main():
    t.speed(0)
    t.up()
    t.pencolor("black")
    t.pensize(1)
    t.goto(-200,130)
    t.down()
    t.goto(200,130)
    t.goto(200,-130)
    t.goto(-200,-130)
    t.goto(-200,130)
    t.up()

    redS(t)
    bluecrnr(t)
    whiteStars(t)



def redS(t):
    s=-200
    s2=130
    
    while s2>-130:
        t.fillcolor("red")
        t.up()
        t.begin_fill()
        t.goto(s,s2)
        t.goto(s*-1,s2)
        t.goto(s*-1,s2-20)
        t.goto(s,s2-20)
        t.goto(s,s2)
        t.end_fill()
        t.up()
        t.pencolor("black")
        t.pensize(1)
        t.goto(s,s2)
        t.down()
        t.goto(s*-1,s2)
        t.goto(s*-1,s2-20)
        t.goto(s,s2-20)
        t.goto(s,s2)
        s2=s2-40


def bluecrnr(t):
        t.fillcolor("blue")
        t.up()
        t.begin_fill()
        t.goto(-200,130)
        t.goto(-30,130)
        t.goto(-30,-10)
        t.goto(-200,-10)
        t.goto(-200,130)
        t.end_fill()
        t.pencolor("black")
        t.pensize(1)
        t.goto(-200,130)
        t.down()
        t.goto(-30,130)
        t.goto(-30,-10)
        t.goto(-200,-10)
        t.goto(-200,130)


def whiteStars(t):
    t.up()
    t.fillcolor("white")
    row=[6,5,6,5,6,5,6,5,6]
    c=0
    cx = 0
    cy = 0
    for i in range(len(row)):
        if row[i] == 6:
            cx = 0
        else:
            cx = 13
    
        for outer in range(row[i]):
            t.begin_fill()
            t.goto(-186+c+cx-10,97-cy+10)
            t.goto(-180+c+cx-10,119-cy+10)
            t.goto(-174+c+cx-10,97-cy+10)
            t.goto(-191+c+cx-10,109-cy+10)
            t.goto(-169+c+cx-10,109-cy+10)
            t.goto(-186+c+cx-10,97-cy+10)
            t.end_fill()
            c=c+30
        c=0
        cy += 14


main()

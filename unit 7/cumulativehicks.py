import turtle



def main():
    t=turtle.Turtle()
    t.hideturtle()
    t.speed(500)
    cp=["navy blue","red","forest green","cyan","magenta"]
    c=0
    i=2
    x=0
    y=-100
    r=100
    s=0
    d=0
    while d<3:
        squaredesign(t,i,x,y,cp,c,r,s)
        circledesign(t,i,x,y,cp,c,r,d)
        d=d+1
  
    
           
        
   
   

def squaredesign(t,i,x,y,cp,c,r,s):
    while i<4 :
        if i <4:
            t.up()
            t.pencolor(cp[c])
            t.goto(x+r,y+r+100)
            t.down()
            t.goto(x-r,y+r+100)
            t.goto(x-r,y-r+100)
            t.goto(x+r,y-r+100)
            t.goto(x+r,y+r+100)
            t.up()
        r=r-10
        c=c+1
        if c==5:
            i=i+1
            c=c-5
    t.clear()
    s=s+1
    return s

def circledesign(t,i,x,y,cp,c,r,d):
    while i<4 :
        if i <4:
            t.up()
            t.pencolor(cp[c])
            t.goto(x,y)
            t.down()
            t.circle(r)
        y=y+10
        r=r-10
        c=c+1
        if c==5:
            i=i+1
            c=c-5
    t.clear()
    d=d+1
    return d

main()


import turtle



t=turtle.Turtle()
t.hideturtle()






def main():
    chs=["C","h","a","n","t","i","l","l","y"]
    color=["red","yellow","orange","blue","green","purple"]
    c=0
    x=2
    while x<3 :
        if x <5:
#1
            t.goto(-100,0)
            t.speed(1)
            t.pencolor(color[c])
            t.write(chs[0],align = "center", font=("OCR A Std",20,"bold"))
            
            
#2
            t.goto(-75,0)
            t.speed(1)
            t.pencolor(color[c])
            t.write(chs[1],align = "center", font=("OCR A Std",20,"bold"))
            
            
#3
            t.goto(-50,0)
            t.speed(1)
            t.pencolor(color[c])
            t.write(chs[2],align = "center", font=("OCR A Std",20,"bold"))
           
            
#4
            t.goto(-25,0)
            t.speed(1)
            t.pencolor(color[c])
            t.write(chs[3],align = "center", font=("OCR A Std",20,"bold"))
            
            
#5
            t.goto(0,0)
            t.speed(1)
            t.pencolor(color[c])
            t.write(chs[4],align = "center", font=("OCR A Std",20,"bold"))
            t.goto(0,0)
            
#6
            t.goto(25,0)
            t.speed(1)
            t.pencolor(color[c])
            t.write(chs[5],align = "center", font=("OCR A Std",20,"bold"))
            
            
#7
            t.goto(50,0)
            t.speed(1)
            t.pencolor(color[c])
            t.write(chs[6],align = "center", font=("OCR A Std",20,"bold"))
            
            
#8
            t.goto(75,0)
            t.speed(1)
            t.pencolor(color[c])
            t.write(chs[7],align = "center", font=("OCR A Std",20,"bold"))
            
            
#9
            t.goto(100,0)
            t.speed(1)
            t.pencolor(color[c])
            t.write(chs[8],align = "center", font=("OCR A Std",20,"bold"))
            
        c=c+1
        if c==6:
            c=c-6
        
        
        



    #t.goto(-100,100)
    #t.down()
    #t.write("Chantilly")

    
    
main()

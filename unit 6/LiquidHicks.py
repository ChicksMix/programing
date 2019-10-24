





def main():
    l,c= enter()
    ans=GtoL(l,c)
    ans2=LtoG(l,c)

    
    if validentry(l)== True:
        if c==1:
            print l,"Gallons are",ans,"liters"
        elif c==2:
            print l,"Liters are",ans2,"gallons"
        else:
            print "selection is not valid"
    else:
        print "measurment is not vaild"





def enter():
    l=float(input("Enter the liquid measurement: "))
    print "Enter 1 to convert Gallons to Liters"
    print "Enter 2 to convert Liters to Gallons"
    c=int(input("Enter your selection: "))
    return l,c



def validentry(l):
    if l >0:
        return True
    else:
        return False


def GtoL(l,c):
    ans=round((l*3.78541),2)
    return ans
    



def LtoG(l,c):
    ans2=round((l*0.264172),2)
    return ans2



main()
    

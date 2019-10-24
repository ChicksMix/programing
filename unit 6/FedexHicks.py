#Carter Hicks
#fedex
#3/5/18

def main():
    weight=float(input("Enter the weight of your package in ounces: "))

    p=cost(weight)

    print "\nThe cost to airmail the letter is: $"+str(p)
    print

def cost(w):
    nweight=ceil(w)
    print "\nThe adjusted weight is: "+str(nweight)
    c= ((nweight-1)*.10)+.05
    return c
 
    


def ceil(w):
    if w >int(w):
        return (int(w)+1)
    else:
        return int(w)

main()




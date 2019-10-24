


b=int(input("Enter the number of symbols to be used in the base: "))


for n in range(1,b+1,2): # counting by two to add the next line
    space=1
    while space <=int((b-n)/2):
        print " ",
        space+=1
    for x in range (1,n+1):
        if x < n:
            print str("*"),
        else:
            print str("*")


    

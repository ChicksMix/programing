b=int(input("Enter the number of symbols to be used in the base: "))
b2= b-2

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
for s in range(b2,0,-2):
    space2=b2
    while space2 >=int((b2+s)/2):
        print " ",
        space2-=1
    for p in range(1,s+1):
        if p < s:
            print str("*"),
        else:
            print str("*")

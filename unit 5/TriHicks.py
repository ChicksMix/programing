#Carter hicks
#right triangle

s=raw_input("Enter a symbol desired to be used in the shape: ")
b=int(input("Enter the number of symbols to be used in the base: "))
for n in range(1,b+1):
    for x in range(1,n+1):
        if x < n:
            print str(s),
        else:
            print str(s)

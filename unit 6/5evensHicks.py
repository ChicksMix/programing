#Carter Hicks
#5's evens


def main():
    num= int(input("Enter a whole number: "))
    
    if evenM5(num):
        print "\n",str(num),"is an even number or a multiple of 5: "
    else:
        print "\n",str(num),"is not an even number or a multiple of 5: "

def evenM5(e):
    if e % 2 == 0 or e % 5 == 0:
        return True
    else:
        return False

main()

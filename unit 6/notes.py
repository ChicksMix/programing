

def main():
    average()

    print "The average of 100 and 500 is: ", average2(100,500)

def average():
    total=0.0
    count=0
    num=0.0
    while num <>-1:
        num= float(input("Enter a number >= 0 or -1 to quit: "))
        if num <> -1:
            count +=1
            total +=num


    avg= float(round(total/count,2))
    print "The average is: ", avg


def average2 (num1,num2):
    Avg=float(round((num1+num2)/2,2))
    return Avg

main()

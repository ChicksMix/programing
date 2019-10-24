#Carter Hicks
#1/2/18

count = int(input("Enter your starting number: "))
num = int(input("Enter your ending number: "))
Sum = 0
while count <= num:
    Sum = Sum + count
    if count < num:
        print count,"+",
    else:
        print count,"=",Sum 
    count= count + 1



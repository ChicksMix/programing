#Carter Hicks

def main():
    num1 = float(input("Enter a number:  "))
    num2 = float(input("Enter a number:  "))

    print "The average is: ", average(num1, num2)
    print "The product is: ", product(num1, num2)
    print "The quotient is: ", quotient(num1, num2)
    print "The difference is: ", difference(num1, num2)
    print "The ", num1," to the power of ", num2," is: ", power(num1, num2)

def average(num1,num2):
    average=(num1+num2)/2
    return average

def product(num1,num2):
    product= num1+num2
    return product

def quotient(num1,num2):
    if num1> num2:
        quotient= num1/num2
    elif num1<num2:
        quotient= num2/num1
    else:
        quotient=1
    return quotient

def difference(num1,num2):
    if num1>= num2:
        difference= num1-num2
    else:
        difference= num2-num1
    return difference 

def power(num1,num2):
    power= num1**num2
    return power
    
main()

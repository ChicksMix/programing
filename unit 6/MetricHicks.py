#Carter Hicks
#Metric


def main():
    conv= float(input("Enter the measurement: "))
    print "1-Inches to Centimeters"
    print "2-Feet to Centimeters"
    print "3-Yards to Meters"
    print "4-Miles to Kilometers"
    print "5-Centimeters to Inches"
    print "6-Centimeters to Feet"
    print "7-Meters to Yards"
    print "8-Kilometers to Miles"
    num=int(input("Enter the number of your selection: "))
    if num== 5:
        print "There are",conv,"Inches in",conv * 2.54,"Centimeters"
    elif num==6:
        print "There are",conv,"Feet in",conv * 30,"Centimeters"
    elif num==7:
        print "There are",conv,"Yards in",.91 * conv,"Meters"
    elif num==8:
        print "There are",conv,"Miles in",conv * 1.6,"Kilometers"
    elif num==1:
        print "There are",conv,"Centimeters in",conv/2.54,"Inches"
    elif num==2:
        print "There are",conv,"Centimeters in",conv/30,"Feet"
    elif num==3:
        print "There are",conv,"Meters in",conv/.91,"Yards"
    else:
        print "There are",conv,"Kilometers in",conv/1.6,"Miles"
        

def a(num,conv):
    if num == 5:
        return conv * 2.54
def b(num,conv):
    if num== 6:
        return conv * 30
def c(num,conv):
    if num==7:
        return .91 * conv
def d(num,conv):
    if num==8:
        return conv * 1.6
def e(num,conv):
    if num==1:
        return conv/2.54
def f(num,conv):
    if num==2:
        return conv/30
def g(num,conv):
    if num==3:
        return conv/.91
def h(num,conv):
    if num==4:
        return conv/1.6

main()




#Carter Hicks

def main():
    g =InputGrade()
    print "\nThe letter grade earned is: "+str(g)
    print

def InputGrade(g):
    g=float(input("\nEnter the test grade: "))
    return LetterGrade(g)

def LetterGrade(g):
    if g>=91:
        return "A"
    elif g >=81:
        return "B"
    elif g >=71:
        return "C"
    elif g >=61:
        return "D"
    else:
        return "F"
main()

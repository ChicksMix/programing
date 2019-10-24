#monogram



def main():
    n=enter()
    lf,cl,lm=mono(n)
    dis(lf,cl,lm)

def enter():
    n= raw_input("Enter your first, middle, and last name: ")
    return n



def mono(n):
    sp= n.find(" ")
    sp2 = n.rfind(" ")
    F = n[0]
    M = n[sp+1:sp+2]
    L = n[sp2+1]
    lf = F.lower()
    cl = L.upper()
    lm = M.lower()
    return lf,cl,lm

def dis(lf,cl,lm):
    print "Your monogram is",lf+cl+lm

main()
    

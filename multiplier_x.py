x = int(input("Met welke getal wilt u de tafel zien? "))
def multi(getal):
    for i in range(1, 11):
        m = getal * i 
        print(str(getal) + " * " + str(i) + " = " + str(m) )

multi(x)
def pelda():
    for i in range(5):
        if i <= 3:
            print(i, end=", ")
        if i == 4:
            print(i)

def pelda_1():
    range1 = 4
    for i in range(range1):
        print(i, end=", ")
    print(range1)

def pelda2():
    for i in range(6, 8):
        print(i, end=", ")
    print(8)

def pelda3():
    for i in range(5, 41, 5):
        print(i, end=" ")

def pelda3_1():
    for i in range(40, 4, -5):
        print(i, end=" ")
    
def feladat_1():
    a = input("Add meg a kedvenc márkádat: ")
    for i in range(3):
        print(a)

def feladat_2():
    a = int(input("Adj meg egy egész pozitiv számot 1-5 közöt: "))
    if a not in range(1, 6):
        a = int(input("Hiba! Adj meg egy egész pozitiv számot 1-5 közöt: "))
    for i in range(a):
        print("*",end="")

def feladat_3():
    for i in range(0,21):
        print(i, end=" ")

def feladat_4():
    for i in range(20,57,2):
        print(i, end=" ")

def feladat_5():
    for i in range(77,-77,-4):
        print(i, end=" ")

def feladat_6():
    a = int(input("1. szám: "))
    b = int(input("2. szám: "))
    if a > b:
        for i in range(b,a+1):
            print(i, end=" ")
    elif b > a:
        for i in range(a,b+1):
            print(i, end=" ")
    else:
        print("ugyan annyi a szám.")

def feladat_7():
    a = int(input("Add meg az 'a' számot: "))
    b = int(input("Add meg a 'b' számot: "))
    for i in range(0,a*b+1):
        print(i)

def feladat_7_1():
    a = int(input("Add meg az 'a' számot: "))
    b = int(input("Add meg a 'b' számot: "))
    valaszto = a
    for i in range(2):
        for i in range(0,3):
            print(valaszto*i, end=" ")
        valaszto = b
        print()
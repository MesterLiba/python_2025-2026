import random
def feladat_1():
    for i in range(0, 151, 2):
        print(i, end=" ")
        if i % 5 == 0:
            print()
    
def print1(i):
    if i % 2 == 0:
        print(i, end=" ")
        if i % 5 == 0:
            print()

def print2(szam):
    for i in range(szam):
        if i != 0 and i % 10 == 0:
            print()
        print("*",end=" ")

def feladat_1full():
    a = int(input("Add meg a értéket: "))
    b = int(input("Add meg b értéket: "))
    for i in range(a, b+1):
        print1(i)

def feladat_3():
    szam = int(input("Adj meg egy 10-zel osztható számot!: "))
    rontas_szam = 0
    while not(szam % 10 == 0):
        rontas_szam += 1
        szam = int(input("Hiba! Adj meg egy 10-zel osztható számot!: "))
    if rontas_szam < 5:
        print("Nagyon ügyes vagy birtál írni egy 10-zel osztható számot yayyy!!")
        print2(szam)
    else:
        print("Te mentálisan nyomorék vagy mi tartott idáig!")
        print2(szam)
    
def feladat_4():
    szam = int(input("Adj meg egy kétjegyű és páros számot!: "))
    while not((9 < szam < 100 and szam % 2 == 0) or (-9 > szam > -100 and szam % 2 == 0)):
        szam = int(input("Hiba! Adj meg egy kétjegyű és páros számot!: "))
    print2(szam)

def feladat_5():
    i = int(input("Pozitív páratlan szám: "))
    while not (i > 0 and i % 2 == 1): 
        i = int(input("Hiba! Pozitív páratlan szám: "))
    print(i)

def Collatz_Conjecture():
    save = []
    for i in range(5):
        veletlen = random.randint(1, 200)
        save.append(veletlen)
        while not (veletlen == 1):
            if veletlen % 2 == 1:
                veletlen * 3
                return veletlen
            if veletlen % 2 == 0:
                veletlen / 2
                return veletlen
            save.append(veletlen)
    print(save)

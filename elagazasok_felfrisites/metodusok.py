# 1. A program oldja meg az a*x+b=0 alakú egyenletet! Kérje be a konzolról az a és b valós típusú változókat! 
    # Ha az a értéke nem nulla, akkor a program számítsa ki és írja ki a megoldást (x=-b/a) a konzolra, illetve 
    # értékelje ki az egyéb lehetőségeket is!
def egyenlet():
    a = float(input("Add meg az 'a' értéket: "))
    b = float(input("Add meg a 'b' értéket: "))
    if a != 0:
        x = -b / a
        print("A megoldás: x =", x)
    elif b != 0:
        print("Nincs megoldás.")
    else:
        print("Végtelen megoldás van.")

# 2. Bekérünk két egész számot, és az összes jellemzőt kiíratjuk az alábbiak közül, ha teljesül rá:
    #ha a számok alapján képezhető téglalap (a számok a téglalap oldalai) területe és a kerülete is kisebb, mint 100 egység, akkor kiíratjuk, hogy “kis téglalap”.
    #ha ez egy négyzet, azt is kiíratjuk.
    #ha az egyik oldal jóval kisebb (kisebb, mint a harmada), mint a másik, kiíratjuk, hogy “keskeny téglalap”.
    #Ha a fentiek közül semmi nem érvényes, kiíratjuk azt, hogy “Ez egy egészen normális téglalap.”
def teglalapjel():
    eredmeny = []
    jell = 0
    a = int(input("Add meg az 'a' értéket: "))
    b = int(input("Add meg a 'b' értéket: "))
    if 2*(a+b) < 100 and a*b < 100:
        eredmeny.append("kis téglalap")
        jell += 1
    if a == b:
        eredmeny.append("ez egy négyzet")
        jell += 1
    if a/3 > b or b/3 > a:
        eredmeny.append("keskeny téglalap")
        jell += 1
    if jell == 0:
        eredmeny.append("Ez egy egészen normális téglalap.")
    for eredmeny in eredmeny:
        print(eredmeny,end=" ")
    
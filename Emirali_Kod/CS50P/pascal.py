def main():
    n = int(input("Number: "))

    for i in range(1, n+1):
        liste = list(range(1, i+1))
        str_liste = []
        ters_liste = []
        for _ in liste:
            str_liste.append(str(_))
            ters_liste.append(str(_))
        ters_liste.remove(str(i))
        ters_liste.reverse()
    
        bosluklar = []
        yazilar = "".join(str_liste) + "".join(ters_liste)
        while n>=1:
            bosluklar.append(n+1)
            n -=1
        
        for i in range(n):
            bosluk_sayisi = bosluklar[i]
            print(" " * bosluk_sayisi + yazilar[i])

if __name__ == "__main__":
    main()
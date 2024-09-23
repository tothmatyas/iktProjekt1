import random
import string

f = open("fe.txt","w",encoding="utf-8")
lines = f.writelines


print("Válassz az alábbi lehetőségek közül:\n"
          "1. Adott darabszámú véletlen egész számok generálása adott határok között.\n"
          "2. Adott darabszámú véletlen szöveg generálása az angol ABC nagybetűiből vagy kisbetűiből.")
    
lehetosegek = int(input("Válassz!(1/2): "))

match lehetosegek:
    case 1:
        darabSzam = int(input("Hány darab szám generálódjon?: "))
        nagySzam = int(input("A legnagyobb generálható szám: "))
        kisSzam = int(input("A legkisebb generálható szám: "))

        Szamok = []
        while len(Szamok) < darabSzam:
            Szamok.append(random.randint(kisSzam,nagySzam))
    case 2:
        betuk = "abcedfghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ"
        szovegek = []
        darabSzoveg = int(input("Hány darab szöveg generálódjon?: "))
        while len(szovegek) < darabSzoveg:
            szavak = []
            for _ in range(random.randint(1,20)):
                szavak.append(random.choice(betuk))
            szavak = "".join(szavak)
            szovegek.append(szavak)

print(szovegek)

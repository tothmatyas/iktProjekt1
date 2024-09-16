import random

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
        betuk = "abcedfghijklmnopqrstuvwxyz"
        for betu in betuk:
            

        darabSzoveg = int(input("Hány darab szöveg generálódjon?: "))
        
        szovegek = []
        while len(szovegek) < darabSzoveg:
            szovegek.append(''.join(random.sample(betuk,len(betuk))))
print(szovegek)



  


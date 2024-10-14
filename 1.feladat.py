import random

f = open("ki.txt","w",encoding="utf-8")
lines = f.writelines
while True:
    print("Válassz az alábbi lehetőségek közül:\n"
            "1. Adott darabszámú véletlen egész számok generálása adott határok között.\n"
            "2. Adott darabszámú véletlen szöveg generálása az angol ABC nagybetűiből vagy kisbetűiből.\n"
            "3. Adott darabszámú véletlen egész számok leellenőrzése egy adott fájlból.\n"
            "4. Adott darabszámú véletlen szöveg leellenőrzése egy adott fájlból.\n"
            "x. Kilépés a programból\n"
            "(A teszeléshez először futtatni kell az 1-es vagy 2-es lehetőséget)")
        
    lehetosegek = int(input("Válassz!(1/2/3/4): "))

    match lehetosegek:
        case 1:
            darabSzam = int(input("Hány darab szám generálódjon?: "))
            kisSzam = int(input("A legkisebb generálható szám: "))
            nagySzam = int(input("A legnagyobb generálható szám: "))

            Szamok = []
            while len(Szamok) < darabSzam:
                Szamok.append(random.randint(kisSzam,nagySzam))
            
            for szam in Szamok:
                f.write(f"{szam};")
            f.close()

        case 2:
            betuk = "abcedfghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ"
            darabSzoveg = int(input("Hány darab szöveg generálódjon?: "))
            szovegek = []
                    
            while len(szovegek) < darabSzoveg:
                szavak = []
                for _ in range(random.randint(1,20)):
                    szavak.append(random.choice(betuk))
                szavak = "".join(szavak)
                szovegek.append(szavak)

            for szoveg in szovegek:
                f.write(f"{szoveg};")
            f.close()

        case 3:
            f = open("ki.txt","r",encoding="utf-8")
            lines = f.readlines()
            lines = str(lines[0])
            lines = lines[:-1]

            darabSzamEL = int(input("Hány darab szám generálódott?: "))
            kisSzamEL = int(input("A legkisebb generáldott szám: "))
            nagySzamEL = int(input("A legnagyobb generálódott szám: "))

            szamok = []
            a = int(nagySzam)
            b = int(kisSzam)
            print(lines)
            for i in lines.split(";"):
                szamok.append(i)
                if int(i) < int(a):
                    a = i
            list(map(int, szamok))

            if len(szamok) != darabSzam:
                print("Nem ugyanolyan hosszú!")
            else:
                print("A lista hossza megegyezik!")

            if int(b) > int(b):
               print("A legkisebb szám nem egyezik meg!")
            else:
                print("A legkisebb szám megegyezik!")

            if int(a) > int(a):
               print("A legnagyobb szám nem egyezik meg!")
            else:
                print("A legnagyobb szám megegyezik!")
            break
        
        case 4:
            f = open("ki.txt","r",encoding="utf-8")
            lines = f.readlines()
            lines = str(lines)

            if len(szovegek) == darabSzoveg:
                print("A lista hossza megegyezik!")
            else:
                print("A lista nem ugyanolyan hosszú")
            break
        
        case "x":
            exit()
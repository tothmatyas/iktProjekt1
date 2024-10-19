import random

f = open("ki.txt","w",encoding="utf-8")

while True:
    print("Válassz az alábbi lehetőségek közül:\n"
            "1. Adott darabszámú véletlen egész számok generálása adott határok között.\n"
            "2. Adott darabszámú véletlen szöveg generálása az angol ABC nagybetűiből vagy kisbetűiből.\n"
            "3. Adott darabszámú véletlen egész számok leellenőrzése egy adott fájlból.\n"
            "4. Adott darabszámú véletlen szöveg leellenőrzése egy adott fájlból.\n"
            "5. Kilépés a programból\n"
            "(A teszeléshez először futtatni kell az 1-es vagy 2-es lehetőséget)")
        
    lehetosegek = int(input("Válassz!(1/2/3/4/5): "))

    match lehetosegek:
        case 1:
            darabSzam = int(input("Hány darab szám generálódjon?: "))
            kisSzam = int(input("A legkisebb generálható szám: "))
            nagySzam = int(input("A legnagyobb generálható szám: "))

            Szamok = []
            while len(Szamok) < darabSzam:
                Szamok.append(random.randint(kisSzam,nagySzam))
            
            max = 0
            min = 10000000
            for szam in Szamok:
                if szam < min:
                    min = szam
                if szam > max:
                    max = szam
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

            nums = []
            a = int(nagySzam)
            b = int(kisSzam)
            c = int(darabSzam)
            
            for i in lines.split(";"):
                nums.append(i)
                if int(i) < int(a):
                    a = i
            list(map(int, nums))

            maxEL = 0
            minEL = 10000000
            for num in nums:
                if int(num) < int(minEL):
                    minEL = num
                if int(num) > int(maxEL):
                    maxEL = num

            print(maxEL,minEL,min,max)
            if len(nums) != len(Szamok):
                print("Nem ugyanolyan hosszú!")
            else:
                print("A lista hossza megegyezik!")

            if int(minEL) == int(min):
               print("A legkisebb szám megegyezik!")
            else:
                print("A legkisebb szám nem egyezik meg!")

            if int(maxEL) == int(max):
               print("A legnagyobb szám megegyezik!")
            else:
                print("A legnagyobb szám nem egyezik meg!")
            break
        
        case 4:
            f = open("ki.txt","r",encoding="utf-8")
            lines = f.readlines()
            lines = str(lines[0])
            lines = lines[:-1]
            lines = lines.split(";")

            if len(lines) == darabSzoveg:
                print("A lista hossza megegyezik!")
            else:
                print("A lista nem ugyanolyan hosszú!")
            break
        
        case 5:
            exit()
import random

f = open("ki.txt","r", encoding="utf-8")
lines = f.readlines()
f.close()

arr = ''.join(lines)
arr = arr.split(";")


#megnézi hogy az arr int vagy string
arrIsInt = arr[0].isnumeric()

#megnézi hogy helyes e az array (nagyon csúnyán)
if arrIsInt:
    try:
        for i in arr:
            int(i)
    except:
        print("nem mind int")
        exit()

if not arrIsInt:
    try:
        for i in arr:
            int(i)
        print("nem ind string")
        exit()
    except:
        pass

#megcsinálja a bubble sort-ot
def bubbleSort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1] :
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


#megcsinalja a beszúrásos rendezést
def insertionSort(arr):
    while arr == arr.sort():
        lenght = len(arr)
        
        for i in range(1, lenght):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
 
# megcsiálja a bogosort-ot
def bogoSort(a):
    n = len(a)
    while (is_sorted(a)== False):
        shuffle(a)
 
#megnezi hogy az arr sorrndbe van-e
def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True
 
#a tömb permutációjának létrehozása
def shuffle(a):
    n = len(a)
    for i in range (0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]

#dolgok hozáadásának az eljárása
def insert(thing : str):
    thingIsInt = thing.isnumeric()

    if thingIsInt and arrIsInt:
        arr.append(thing)

    elif not thingIsInt and not arrIsInt:
        arr.append(thing)
    
    else:
        print("nem jó a type")
        exit()

#algoritus kiválasztása
print("Milyen algoritmust használjon a program? 1: bubble sort | 2:  beszúrásos rendezés | 3: bogosort")
inp = int(input())

match inp:
    case 1:
        bubbleSort(arr)
    case 2:
        insertionSort(arr)
    case 3:
        bogoSort(arr)
    case _:
        print("nem helyes számot adtál")

#array elem hozzáadása
print("akarsz hozzáadni egy új elemet 1: igen | 2: nem")
inp = int(input())

match inp:
    case 1:
        print("az új elem: ")
        insert(input())
        bubbleSort(arr)

#eldönti hogy növekvő vagy csökkenő legyen
print("1:növekvő vagy 2:csökkenő legyen? ")
inp = int(input())

match inp:
    case 1:
        pass
    case 2:
        arr = arr[::-1]
    case _: 
        print("nem helyes számot adtál meg")
        #print("🤡")
        exit()

print(arr)




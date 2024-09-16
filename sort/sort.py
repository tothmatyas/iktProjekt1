f = open("ki.txt","r", encoding="utf-8")
lines = f.readlines()
f.close()

arr = ''.join(lines)
arr = arr.split(";")


if arr[0].isdigit():
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1] :
                arr[i], arr[i+1] = arr[i+1], arr[i]

else:
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if  len(arr[i]) > len(arr[i+1]) :
                arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)







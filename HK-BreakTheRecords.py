str = "10 10 10 10 10"
arr = []
for i in str.split():
    arr.append(int(i))
print(arr)

hs = arr[0]
ls = arr[0]
chs = 0
cls = 0
for i in range(1,len(arr)):
    if hs < arr[i]:
        hs = arr[i]
        chs+=1
        emp1.append(hs)
    if ls > arr[i]:
        ls = arr[i]
        cls+=1
       
print(chs,cls)
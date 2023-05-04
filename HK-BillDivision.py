ar = [3,10,2,9]
k = 1
b = 12
s = 0
for i in ar:
    s = s + i
m = s - ar[k]
print(m)
val = b -  m/2
if val != 0:
    print(int(val))
else:
    print("Bon Appetit")
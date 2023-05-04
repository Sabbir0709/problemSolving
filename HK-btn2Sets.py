a = [2,4]
b = [16,32,96]
min_array1 = min(a)
max_array2 = max(b)
count = 0
for i in range(min_array1, max_array2+1):

    if all(i % num == 0 for num in a) and all(num % i == 0 for num in b):
        # print(i)
        count+=1

print(count)
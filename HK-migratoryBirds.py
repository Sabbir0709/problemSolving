a = [1,1,2,2,3]
output = {}
for i in range(0, len(a)):
    if a[i] not in output:
        output[a[i]] = a.count(a[i])
    
print(output)
# print(min(output.keys()))
print(output.items())
keys = []
for k,v in output.items():
    maxi = max(output.values())
    if v == maxi:
        keys.append(k)

print(min(keys))   
#ShortHand
        
max_ids = [k for k,v in output.items() if v == max(output.values())]

print(min(max_ids))
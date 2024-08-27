# FIND UNIOIN AND INTERSECTION .......
set1 = (1,2,3,4,5)
set2 = (4,5,6,7,8)

union = []
intersection = []

for i in range(0,len(set1)):
    num = set1[i]
    for j in range(0,len(set2)):
        if(num==set2[j]):
            intersection.append(num)

for i in range(0,len(set1)):
    num = set1[i]
    for j in range(0,len(set2)):
        if(num!=set2[j]):
            union.append(num)
            break

for i in range(0,len(set2)):
    num = set2[i]
    for j in range(0,len(set1)):
        if(num!=set1[j]):
            union.append(num)
            break

print(f"intesection of set{set1} , and set{set2} = {intersection}")
print(f"union of set{set1} , and set{set2} = {list(set(union))}")
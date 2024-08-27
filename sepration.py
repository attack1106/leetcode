arr = [1,2,3,4,-3,-4,-6]

for i in range(0,len(arr)):
    for j in range (i+1,len(arr)):
        if(arr[j]<0):
            temp = arr[i]
            arr[i]= arr[j]
            arr[j]=temp
print(arr)
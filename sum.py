def sum_index(arr , num):
    for i in range(0 , len(arr)):
        for j in range(i+1,len(arr)):
            if((arr[i]+arr[j])==num):
                print(f"sum of element {arr[i]} at index {i} and {arr[j]} at index {j} = {num}")

arr=[6, 3, 5, 7,5]
num = 10 

sum_index(arr , num)

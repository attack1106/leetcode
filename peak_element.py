# find the peak element fron the element
def peak(arr):
    for i in range(1,4):
        if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
            print(f"peak element of array = {arr[i]}")
            break

arr = [5,10,20,15]
peak(arr)




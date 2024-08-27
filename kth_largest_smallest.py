# dsa kth largest and smallest element of an array 
def lagest_smallest(arr):
    mini=arr[0]
    k = int(input("enter value of k : "))
    max = arr[0]
    for i in range(k-1):
        if(arr[i]>max):
            max = arr[i]        
        if(arr[i]<mini):
            mini = arr[i]

    print(f"max = {max}")
    print(f"mini = {mini}")

arr = [1,23,4,5,6,7,0]
lagest_smallest(arr)
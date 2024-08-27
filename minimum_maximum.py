def minimun(arr):
    mini =0 
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]<arr[j]):
                mini = arr[i]
                break
            elif(arr[j]<arr[i]):
                mini = arr[j]
    print(f"minimum element = {mini}")

def maximum(arr):
    max = 0 
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]<arr[j]):
                max = arr[j]
            elif(arr[j]<arr[i]):
                max = arr[i]
                break
    print(f"maximum element in an array = {max}")
arr = [1,5,7,0,6]
minimun(arr)
maximum(arr)
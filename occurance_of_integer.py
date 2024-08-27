# occurance of an integer in an array 
def occurance(arr , k):
    count = 0 
    for i in range(len(arr)):
        if(arr[i]==k):
            count+=1
    print(f"occurance of number{k} in an array = {count}")
while(1):
    arr = [0,0,0,0,0,0,0,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2]
    k = int(input("enter the number "))
    occurance(arr,k)

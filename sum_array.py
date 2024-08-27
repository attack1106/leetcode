class calculate:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
        
    def sum_of_array(self):
        result = []
        for i in range(len(self.l1)):
            result.append(self.l1[i]+self.l2[i])

        return result

arr1=[1,2,3]
arr2=[4,5,6] 
obj = calculate(arr1,arr2)

print(obj.sum_of_array())
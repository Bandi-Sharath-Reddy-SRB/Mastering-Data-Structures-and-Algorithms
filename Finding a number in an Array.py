import numpy as np

myArray=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def missing_number(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return True
        
    return None

print(missing_number(myArray,21))
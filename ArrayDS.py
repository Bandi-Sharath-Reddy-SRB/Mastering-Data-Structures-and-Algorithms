from array import *
arr1 = array('i',[1,2,3,4,5,6])

def accesselement(array,index):
    if index>=len(array):
        print("Index out of range")
    else:
        print(array[index])
accesselement(arr1,2)

def linear_search(array,targetvalue):
    for i in range(0,len(array)):
        if array[i]==targetvalue:
           return i
    return "Element not found"
print(linear_search(arr1,10))
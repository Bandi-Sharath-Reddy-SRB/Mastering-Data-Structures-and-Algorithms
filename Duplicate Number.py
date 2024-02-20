'''
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]

'''


def remove_duplicates(arr):
    a=[]
    for i in arr:
        if i not in a:
            a.append(i)
        
    return a

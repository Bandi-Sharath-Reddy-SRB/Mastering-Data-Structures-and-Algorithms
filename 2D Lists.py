'''
2D Lists
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
diagonal_sum(myList2D) # 15

'''

def diagonal_sum(matrix):
    a=[]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i]==matrix[j]:
                a.append(matrix[i][j])
    return sum(a)
                
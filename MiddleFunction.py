''' Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
'''

def middle(lst):
    newlist=lst
    newlist.remove(newlist[0])
    newlist.remove(max(newlist))
    return (newlist)
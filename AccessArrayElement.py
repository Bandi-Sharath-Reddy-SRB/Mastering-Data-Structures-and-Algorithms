import array
my_array=array.array('i',[1,2,3,4,5,6])
def accessarrayelement(array,index):
    if index>=len(array):
        print("There is no Element")
    else:
        print(array[index])
accessarrayelement(my_array,2)
accessarrayelement(my_array,6)
accessarrayelement(my_array,8)
import array
my_array=array.array('i',[1,2,6,8,10])
print(my_array)
#At the beg
my_array.insert(0,50)
print(my_array)
#In the middle
my_array.insert(3,100)
print(my_array)
#At the end
my_array.insert(7,150)
print(my_array)
my_array.insert(9,1500)
print(my_array)
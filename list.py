a = ["ball","bat","wicket"]
print(a)

for i in range(len(a)):
    print(a[i])

b = [1,2,3,4,5]
print(b)
b[4]=100
print(b)
b.insert(0,50)
print(b)
b.insert(3,500)
print(b)
b.insert(len(b),1000)
print(b)

b.append(55)
print(b)

a.extend(b)
print(a)

print(b[2:5])

b.pop(1)
print(b)

del b[2]
print(b)

del b[2:4]
print(b)

b.remove(1000)
print(b)



exampleList = [10,30,50,40,80,70,90,100,36]
for i in range(len(exampleList)):
    print(exampleList[i])

target = 56
if target in exampleList:
    print(f"{target} is in the List.")
else:
    print(f"{target} is not in the List.")


def linearSearch(target,list1):
    for i in range(len(list1)):
        if list1[i]==target:
            print(f"{i} is the index of target element in the list.")
    return -1    

linearSearch(40,exampleList)


lst1=[1,2,30]
lst2=[4,5,6]
list3 = lst1+lst2
print(list3)


lst3 = [1]
list1 = lst3*5
print(list1)

lst4 = [1,2]
list2 = lst4*5
print(list2)


print(sum(list3))

print(sum(list3)/len(list3))


king = "Bandi Sharath Reddy"
convert = list(king)
print(convert)
conv = king.split()
print(conv)



#--To use array methods
import numpy
#--------------------List--------------------
myList = []

for  i in range(0,20,2):
    myList.append(i)

print(myList)

myList.insert(1,-1)
print(myList)

myList.remove(16)
print(myList)

x=myList.pop(3)
print(x)
print(myList)

print(myList.index(10))

myList.reverse()
print(myList)

myList.sort()
print(myList)

myList2 = ["A","B","C"]
myList.extend(myList2)
print(myList)

#--------------------Tuple--------------------
mytuple=(-2,-1,0,1,2,0,0)
print(mytuple)

print(mytuple.count(0))

print(mytuple.index(1))

#--------------------Array--------------------
#---without using any library

myArray=[]
for row in range(10):
    myArray.append([])
    for column in range(10):
        myArray[row].append(0)

print(myArray)

myArray2 = [[1 for column in range(10)] for row in range(10)]
print(myArray2)

#--- using  library numpy

a = numpy.zeros((10,10))
print(a) 
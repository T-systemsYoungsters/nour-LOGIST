import random
#-------------------------------[1]-------------------------------------
def min3(a,b,c):
    smallest_num = a
    if b < smallest_num:
        smallest_num = b
    
    if c < smallest_num:
        smallest_num = c
    
    return smallest_num

print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

print()
#-------------------------------[2]-------------------------------------

def box (height,width):
    for row in range(height):
        for column in range(width):
            print("*",end="")
        print()

box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across

print()
#-------------------------------[3]-------------------------------------

def find(my_list,key):
    for pos in range(len(my_list)):
        if my_list[pos] == key:
            print("Found",key,"at position", pos)

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
 
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

print()
#-------------------------------[4 / part 1]-------------------------------------
#-------[4.1]-----------

def create_list(size):
    list = []
    for i in range(size):
        list.append(random.randrange(1,7))
    return list

my_list = create_list(5)
print(my_list)

print()
#-------[4.2]-----------

def count_list(my_list,num):
    counter = 0
    for i in range(len(my_list)):
        if my_list[i] == num:
            counter += 1
    return counter

count = count_list([1,2,3,3,3,4,2,1],3)
print(count)


print()
#-------[4.2]-----------

def average_list(list):
    sum = 0
    size = len(list)
    for i in range(size):
        sum += list[i]
    average = sum/size
    return average

avg = average_list([1,2,3])
print(avg)

print()
#-------------------------------[4 / part 2]-------------------------------------

list = create_list(10000)

print("The number 1 is repeated",count_list(list,1),"times")
print("The number 1 is repeated",count_list(list,2),"times")
print("The number 1 is repeated",count_list(list,3),"times")
print("The number 1 is repeated",count_list(list,4),"times")
print("The number 1 is repeated",count_list(list,5),"times")
print("The number 1 is repeated",count_list(list,6),"times")
print()
print("The average of the list is : ",average_list(list))


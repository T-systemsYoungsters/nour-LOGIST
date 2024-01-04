print("------------1/2-------------")
#------------1/2-------------
for i in range(10):
    print("*",end=" ")
print()
for j in range(5):
    print("*",end=" ")
print()
for k in range(20):
    print("*",end=" ")
        
print("\n")

print("------------3-------------")
#------------3-------------
for row in range(10):
    for column in range(10):
        print("*",end=" ")
    print()
print("\n") 

print("------------4-------------")
#------------4-------------
for row in range(10):
    for column in range(5):
        print("*",end=" ")
    print()

print("\n") 

print("------------5-------------")
#------------5-------------
for row in range(5):
    for column in range(20):
        print("*",end=" ")
    print()

print("\n")

print("------------6-------------")
#------------6-------------
for row in range(10):
    for column in range(10):
        print(column,end=" ")
    print()

print("\n")

print("------------7-------------")
#------------7-------------
for row in range(10):
    for column in range(10):
        print(column,end=" ")
    print()

print("\n")

print("------------8-------------")
#------------8-------------
for row in range(10):
    n=row
    for column in range(10):
        if n>=column:
            print(column,end=" ")
    print()


print("\n")

'''easier way

for row in range(10):
    for column in range(row+1):
        print(column,end=" ")
    print()
'''

print("------------9-------------")
#------------9-------------
for row in range(10):
    for j in range(row):
        print(" ",end=" ")
    for j in range(10-row):
        print(j,end=" ")
    print("")

print("\n")

for row in range(10):
    for j in range(10-row):
        print(j,end=" ")
    for j in range(row):
        print(" ",end=" ")
    print()

print("\n")

print("------------10-------------")
#------------10-------------
for i in range(1,10):
    for j in range(1,10):
        if i*j <10:
            print(" ",end="")
        print(i*j,end=" ")
    print(" ")

print("\n")

for i in range(1,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print(" ")

print("\n")

for i in range(10):
    for j in range(10):
        print(i*j,end=" ")
    print(" ")

print("\n")

print("------------11-------------")
#------------11-------------
for r in range(1,10):
    for j in range(10-r):
        print (" ",end=" ")
    for c in range(1,r+1):
        print(c,end=" ")
        if c == r:
             for i in range(c-1,0,-1):
                print(i,end=" ")
    print(" ")
'''
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row

    print()
'''
print("\n")

print("------------12-------------")
#------------12-------------
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()

for i in range(10):
    # Print leading spaces
    for j in range(i+2):
        print (" ",end=" ")
    # Count down
    for j in range(1,9-i):
        print (j,end=" ")
    # Next row
    print()

print("\n")

print("------------13-------------")
#------------13-------------
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()
    
for i in range(10):
    for j in range(i+2):
        print (" ",end=" ")
    # Count up
    for j in range(1,9-i):
        print (j,end=" ")
    # Count down
    for j in range(7-i,0,-1):
        print (j,end=" ")
    # Next row
    print()

print("\n")

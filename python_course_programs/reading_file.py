file = open("super_villains.txt")
myList = []

for line in file:
    line = line.strip()
    myList.append(line)
    print(line)
file.close()

print(len(myList))


#Linear Search

key = "Morgiana the shrew"

i = 0

while i < len(myList) and myList[i] != key:
    i += 1
if i < len(myList):
    print("The name is at position ," , i)

else:
    print("The name was not found in the list")
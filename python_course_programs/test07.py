#printing the Month name from his number

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
 
month_number = int(input("Enter a month number: "))

start = (month_number-1)*3
end = start +3

print("Month =", months[start:end])


#This code prints out every letter of a string individually:

plain_text = "This is a test. ABC abc"
 
for c in plain_text:
    print(c, end="")
print()

# Create an empty associative array
# (Note the curly braces.)
x = {}
 
# Add some stuff to it
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1
 
for item in x:
    print(item)
# Fetch and print an item
print(x["fred"])

print()
list = []
for i in range(5):
    item = int(input("Enter a number please : "))
    list.append(item)
print(list)


sum = 0
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]

for i in range(len(my_list)):
    sum+=my_list[i]
average = sum / len(my_list)
print("Average = ",average)
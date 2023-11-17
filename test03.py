temperature = int(input("What is the temperature ?"))

if temperature >= 90 :   
    print("It is hot outside.")

elif temperature < 30 :
    print("It is cold outside.")
    
else :
    print("it is not hot outside.")

print("Done!")    

a=3
b=1

c = a==b

print(c)

A= "c"
if A == "B" or A == "b":
    print("a is equal to b.")
else:
    print("a is not b.")

number = int(input("Enter the number : "))

if number > 0 :
    print("the number is positive")
elif number < 0 :
    print("the number is negative")
else :
    print("the number is zero")

num = int(input("Enter the number : "))

if num > -10 and num < 10 :
    print("Success")

x = "-624.6"

if float(x) >= 0:
    print("x is positive.")
else:
    print("x is not positive.")


answer = input("What is the name of Dr. Bunsen Honeydewß's assistant? ")

if answer.lower() == "beaker" :
        print("Correct!")
else :
        print("Incorrect! It is Beaker.")
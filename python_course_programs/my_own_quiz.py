print("Question time :D\nAnswer the following five questions :\n")

number_of_correct_answers = 0

#First question
question1 = int(input("1. What is (4-8)**2 ? "))

if question1 == 16:
   number_of_correct_answers += 1
   print("Correct :)\n")
else:
   print ("Not correct :(\nThe correct answer is : 16\n")


#Secound question
question2 = int(input("2. What is this number 10010 in decimal system "))

if question2 == 18:
    number_of_correct_answers += 1
    print("Correct :)\n")
else:
   print ("Not correct :(\nThe correct answer is : 18\n")



#Third question
question3 = int(input("3. What is first programming language?\nEnter the correct answer number\n1. C\n2. Java\n3. Fortran\n"))
    
if question3 == 3:
    number_of_correct_answers += 1
    print("Correct :)\n")
else:
    print ("Not correct :(\nThe correct answer is : 3\n")


#Fourth question
question4 = input("4. What is the first name of the person who painted the Mona Lisa ? ")
    
if question4.lower() == "leonardo":
    number_of_correct_answers += 1
    print("Correct :)\n")
else:
    print ("Not correct :(\nThe correct answer is : leonardo\n")


#Fifth question
question5 = int(input("5. What is sin(0) ? "))
    
if question5 == 0:
    number_of_correct_answers += 1
    print("Correct :)\n")
else:
    print ("Not correct :(\nThe correct answer is : 0\n")


result = (number_of_correct_answers/5 )*100
print("Congratulations, you got", number_of_correct_answers ,"answers right.\nThat is a score of", result," percent.")
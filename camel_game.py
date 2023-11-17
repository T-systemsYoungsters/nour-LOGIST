import random
import math

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")

done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_distance = -20
drink = 3 

while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.\n")

    user_choice = input("Your choice? ")
    
    #-------------------------------------When the player wants to Quit--------------------------------------
    if user_choice.upper() == "Q":
        done = True
        print("Game Over !!")

    #--------------------------------------When the player wants to see the status----------------------------
    elif user_choice.upper() == "E":
        print("Miles traveled: ",miles_traveled,"\nDrinks in canteen: ",drink)
        print("The natives are ",miles_traveled - natives_distance," miles behind you.\n")

    #---------------------------------------When the player wants to rest--------------------------------------
    elif user_choice.upper() == "D":
        camel_tiredness = 0
        print("The Camel is happy\n")
        natives_distance += random.randrange(7,15)

    #--------------------------------------When the player wants to go full speed------------------------------
    elif user_choice.upper() == "C":
        miles_traveled += random.randrange(10,21)
        print("You have traveled ",miles_traveled," miles")
        thirst += 1
        camel_tiredness += random.randrange(1,3)
        natives_distance += random.randrange(7,14)
        print("The natives are",miles_traveled - natives_distance," miles behind you.\n")

    #--------------------------------------When the player wants to go moderate speed---------------------------
    elif user_choice.upper() == "B":
        miles_traveled += random.randrange(5,13)
        print("You have traveled ",miles_traveled," miles")
        thirst += 1
        camel_tiredness += 1
        natives_distance += random.randrange(7,14)
        print("The natives are",miles_traveled - natives_distance," miles behind you.\n")


    #-------------------------------------When the player wants to drink----------------------------------------
    elif user_choice.upper() == "A":
        if drink !=0:
            thirst = 0
            drink -= 1
        else:
            print("error,your canteen is empty")


    oasis = random.randrange(1,21)
    if oasis == 20:
        print("Congrats, you have found an oasis. :)\n")
        drink = 3
        thirst = 0
        camel_tiredness = 0

    #--------------------------------Check if the player has won or not-----------------------------------

    if miles_traveled >= 200:
        print("\nCongrats, You won. :D ")
        done =True
        
    elif natives_distance >= miles_traveled :
        print("\nThe native caught you.")
        print("Game Over !!")
        done = True
        
    elif thirst > 6 :
        print("\nYou died of thirsty.")
        print("Game Over !!")
        done = True
        
    elif camel_tiredness > 8:
        print("Your Camel is dead.")
        print("Game Over !")
        done = True
        

    else:
        if (miles_traveled - natives_distance) < 15 :
            print("The natives are getting close!")

        if thirst > 4 :
            print("\nYou are thirsty")

        if camel_tiredness > 5:    
             print("Your camel is getting tired. ")
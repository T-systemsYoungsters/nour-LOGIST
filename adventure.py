room_list = []
current_room = 0
done = False
user_choice_direction=""
# room = [roomName,North,South,East,West]

room= ["basement",3,None,None,None]
room_list.append(room)

room= ["bedroom 2",5,None,2,None]
room_list.append(room)

room= ["south_hall",6,None,3,1]
room_list.append(room)

room= ["dining room",7,0,None,2]
room_list.append(room)

room= ["bathroom",None,None,5,None]
room_list.append(room)

room= ["bedroom 1",None,1,6,4]
room_list.append(room)

room= ["north hall",8,2,7,5]
room_list.append(room)

room= ["kitchen",None,3,None,6]
room_list.append(room)

room= ["balcony", 9,6,None,None]
room_list.append(room)

room= ["stair", None,None,None,None]
room_list.append(room)

print("Welcome to the game .")
print("You are trapped in a house, try to find a way out.")

while not done:
   print()
    
   if current_room == 9:
      print("You found an escape stair, your are out of the hause.")
      print("Congratulations :) ")
      done = True
   else:
         print("You are in the",room_list[current_room][0],".")

         for i in range(1,5):
            if room_list[current_room][i] != None:
                  if i == 1:
                     print("There is a door to the north")
                  elif i == 2:
                     print("There is a door to the south")
                  elif i == 3:
                     print("There is a door to the east")
                  elif i == 4:
                     print("There is a door to the west")

         user_choice_direction= input("What direction?") 


         if user_choice_direction.upper() == "N" or user_choice_direction.upper() == "NORTH":
            next_room  =room_list[current_room][1]  
         
         elif user_choice_direction.upper() == "S" or user_choice_direction.upper() == "SOUTH":
            next_room  =room_list[current_room][2]
         
         elif user_choice_direction.upper() == "E" or user_choice_direction.upper() == "EAST":
            next_room  =room_list[current_room][3] 
         
         elif user_choice_direction.upper() == "W" or user_choice_direction.upper() == "WEST":
            next_room  =room_list[current_room][4]
         else:
            print("please enter North, South, East or West.") 
            user_choice_direction=""

         if user_choice_direction != "":
            if next_room == None:
               print("You can't go that way, there is no door.")
            else:
               current_room = next_room

   
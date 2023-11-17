import pygame
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

#------------------part 1------------------------

number = 10
for row in range(9):
    for column in range(row+1):
        print(number,end=" ")
        number += 1
    print()

print()
#------------------part 2------------------------
row_num = int(input("Enter the number of rows : "))
column_num = row_num*2

for r in range(1,row_num+1):
    for c in range(1,column_num+1):
        if r == 1 or r == row_num: 
            print("O",end=" ")
        elif c==1 or c==column_num:
            print("O",end=" ")
        else:
            print(" ",end=" ")
 
print()  
#------------------part 3------------------------
n = int(input("Enter the number of rows : "))
size = n*2

for i in range(1,size+1,2):
    for j in range(i, size+1,2):
        print(j,end=" ")
    for space in range(1,i):
        if space>10 :
            print("",end=" ")
        print(" ",end=" ")
    for k in range (size-1,i-2,-2):
        print(k,end=" ")
    print()

for i in range(size-1,-1,-2):
    for j in range(i,size+1,2):
        print(j,end=" ")
    for space in range(1,i):
        if space>10 :
          print("",end=" ")
        print(" ",end=" ")
    for k in range (size-1,i-2,-2):
        print(k,end=" ")
    print()

#------------------part 4------------------------
# -------- Main Program Loop -----------
pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 700
screen_height= 500
size = (screen_width,screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Part 4 from lab 6 :)")

# Loop until the user clicks the close button.
done = False
stars_num = 30

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Screen-clearing code goes here
    screen.fill(BLACK)

    #green rectamgels
    i_offset = 0 
    for i in range(0,screen_height+1,5):
        j_offset = 0
        for j in range(0,screen_width+1,5):
            pygame.draw.rect(screen,GREEN,[i+i_offset, j+j_offset, 5,5])
            j_offset += 10
        i_offset += 10
    '''
    offset = 0
    for i in range(screen_height+1):
        for j in range(screen_width+1):
            pygame.draw.rect(screen,GREEN,[i+offset, j, 10,10])
            offset += 10

    '''
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()
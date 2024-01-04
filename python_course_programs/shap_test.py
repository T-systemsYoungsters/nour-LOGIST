import pygame

pygame.init()

done = False
clock = pygame.time.Clock()#
score = 100
font = pygame.font.Font("c:/Windows/Fonts/BRADHITC.TTF",25)
screen = pygame.display.set_mode([1000,700])

pygame.display.set_caption("test")

while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")

    screen.fill([255,255,255])
   
    text = font.render("Hallo  from T-Systems", True,[0,0,0])
    text_2=font.render("Score = "+str(score), True,[0,0,0])
    screen.blit(text,[100,100])
    screen.blit(text_2,[100,200])




    pygame.display.flip()

pygame.quit()
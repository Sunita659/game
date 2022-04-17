import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))
font1=pygame.font.Font("freesansbold.ttf,26")
font1=pygame.font.Font("freesansbold.ttf",26)



while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      
name=font1.render("SPACE INVANDERS", False, (255,255,255))
screen.blit(name,[95,20])                                                                            
name=font2.render("SPACE INVANDERS", False, (255,255,255))
screen.blit(text,[95,20+50])                                                                            
   
    
     pygame.display.update()
     clock.tick(30)

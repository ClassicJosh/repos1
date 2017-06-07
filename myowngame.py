import pygame
 

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My Game')

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
 
display_instructions = True
instruction_page = 1
name = ""
 
# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                instruction_page += 1  
                if instruction_page == 3:
                    display_instructions = False                
 
    screen.fill(BLACK)
 
    if instruction_page == 1:
 
        text = font.render("Instructions", True, WHITE)
        screen.blit(text, [10, 10])
       
        text = font.render("Enter your name: ", True, WHITE)
        screen.blit(text, [10, 40])    
       
        text = font.render(name, True, WHITE)
        screen.blit(text, [220, 40])        
 
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 80])
       
        text = font.render("Page 1", True, WHITE)
        screen.blit(text, [10, 120])
 
    if instruction_page == 2:
    
        text = font.render("This program bounces a rectangle", True, WHITE)
        screen.blit(text, [10, 10])    
 
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 40])
 
        text = font.render("Page 2", True, WHITE)
        screen.blit(text, [10, 80])
        
    
# Loop until the user clicks close button
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # write game logic here
 
    # clear the screen before drawing
    screen.fill((255, 255, 255)) 
    # write draw code here
    text = font.render(True, WHITE)
    screen.blit(text, [10, 10])    
 
    # display what’s drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(20)
 
# close the window and quit
pygame.quit()
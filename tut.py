
import pygame 
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render(f"Score: {current_time}",False,(64,64,64))
    score_rect = score_surf.get_rect(center = (319,60))
    screen.blit(score_surf,score_rect)
    return current_time

pygame.init()
#screen = pygame.display.set_mode((width, height))

screen = pygame.display.set_mode((638,600))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
    #clock helps with setting maximum and minimum fps limits
text_font = pygame.font.Font('font/DisposableDroidBB.ttf', 50)
game_active = False
start_time = 0
score = 0
        #pygame.font.Font(remember capital letter on last font) = (font style, font size)
    #helps with setting limits for the least or highest amount of fps in the game 
    #pygame.surface(width, height) of the surface

sky_surface = pygame.image.load('graphics/sky.gif').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
                                            #convert() makes the pygame adjust the image to whats most suitable 
#score_surf = text_font.render('My Runner Game', False, (64,64,64))
                        #.render gives (text, AA(smooth edges or not),color)
#score_rect = score_surf.get_rect(center = (319,60))

enemy_surf = pygame.image.load('graphics/enemies/enemy2.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(bottomright = (550, 450))

player_surf = pygame.image.load('graphics/player/playerwalk2.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,450))
                        #get_rect- takes surface and draws rectangle around it, and allows you to choose specific points of the rectangle and give it coordinates
player_gravity = 0
'''íntro screen '''
player_stand = pygame.image.load('graphics/player/player_stop.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2.5)
                            #.scale(surface,(width,height))
                            #.scale2x(surface)
                            #.rotozoom(surface,angle,scale)
player_stand_rect = player_stand.get_rect(center = (319,300))
'''intro title and score'''
title_surf = text_font.render('My Runner Game',False, ('Black'))
title_rect = title_surf.get_rect(center = (319,60))

start_surf = text_font.render('To Start Running Press SPACE', False,('Black'))
start_surf2 = text_font.render('To Restart Press SPACE', False,('Black'))
start_rect2 = start_surf2.get_rect(center = (319,540))
start_rect = start_surf.get_rect(center = (319,540))

                #test_font.render(text, AA(to smooth out the letters), color)
        #pygame.image.load() = import photo as in sprite
'''test_surface = pygame.Surface((100,200))'''
# to go to the right increase x
#to go down increase y
'''test_surface.fill('gold')'''
      # above is the color to make the surface, but not needed if there is a sprite(i think)1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
                #pygame.quit is the polar opposite of pygame.init()
            exit()
                #exit() means we are exiting the while true loop
    # event = looks through all events
    # pygame.event.get() = gets all events into the equation
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                            #pygame.MOUSEMOTION- for movement of mouse
                            #pygame.MOUSEBOTTONDOWN- for when you click a button
                            #pygame.MOUSEBUTTONUP- for when you release the button
            
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 450: 
                    player_gravity = -20
                #button press -> mouse pos/collision -> jump = more efficient(checking collision on every frame would be wasteful)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 450:
                    player_gravity = -25
    # this else represents is the game_active is not true anymore
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    enemy_rect.left = 550
                    start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,450))
        #pygame.draw.rect(screen,'#c0e8ec',text_rect,12,50)
            #pygame.draw.(shape)= used to draw shape as if to give them shape
        #screen.blit(score_surf,score_rect)
        #     pygame.draw.line(screen,"red",(1,1),(350,350), 30)
                    #color: rgb_color = (red,green,blue)  hex_color = #rrggbb
        score = display_score()
        
        enemy_rect.x -= 10
        if enemy_rect.right <= 0: enemy_rect.left = 638
        screen.blit(enemy_surf,enemy_rect)
        
        
        #Player
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 450: player_rect.bottom = 450
        screen.blit(player_surf, player_rect)
            #screen.blit = coordinates of surface to display on the screenn
        if enemy_rect.colliderect(player_rect):
            game_active = False
# this next else is sort of the intro screen when the things above up to the if statement is the game 
    else:
        screen.fill((120,50,5))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(title_surf,title_rect)
        score_message = text_font.render(f'Your Score: {score}',False,('Black'))
        score_rect =score_message.get_rect(center = (319,120))
        
        if score == 0:
            screen.blit(start_surf,start_rect)

        else:
            screen.blit(score_message,score_rect)
            screen.blit(start_surf2,start_rect2)
                # the if statement is saying game_active which is defined as true, but the collision makes it become false    
        # .colliderect = lets the two rectangles register a collision
                #rect1.collidepoint((x,y)) = checks if a certain point collides with the rectangle
    # draw all our elements
    # update everything
        #pygame.mouse.get_pos = tells you x,y coordinates of the mouse
    #if player_rect.collidepoint(mouse_pos):
       #print(pygame.mouse.get_pressed())
            #pygame.mouse.get_pressed()= tells you which button in the mouse is being pressed
    
    #   keys = pygame.key.get_pressed()
    #   if keys[pygame.K_SPACE]:
        #   print('jump')
    #pygame.key.get_pressed()= gets all buttons and current state, says if they are being pressed or not

    pygame.display.update()
    clock.tick(60)
        # ceiling for the fps 
    
    # If regular surface is not attached to display surface then the surface will not be visible

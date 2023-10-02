from random import randint
from sys import exit

import pygame

pygame.init() #must initialize pygame
width, height, framerate = 800, 400, 60
playing = True

screen = pygame.display.set_mode((width, height)) #screen as variable
pygame.display.set_caption('Duncans game') #sets window title
clock = pygame.time.Clock() #gives us a clock obj
font = pygame.font.Font('Assets/ARCADECLASSIC.TTF', 50)

#GAME VARS
score = 0
moving = False

#MISC VARS
background = pygame.image.load('assets/background.jpg').convert()

scoresurf = font.render(str(score), False, '#045703') #Text, AA, color
scorerect = scoresurf.get_rect(center = (400, 100))

boxsurf = pygame.image.load('assets/box.png').convert()
boxrect = boxsurf.get_rect(center = (500, 200))

#PLAYER VARS
playersurface = pygame.image.load('assets/hero/heroidle.png').convert_alpha()
playersurface = pygame.transform.scale(playersurface, (75, 75))
playerrect = playersurface.get_rect(midbottom = (80, 400)) #creates a rectangle at that location
playerspeed = 0
accspeed = 0.1

while playing:
    for event in pygame.event.get(): #gets all events in pygame
        if event.type == pygame.QUIT: #checks if event is quit
            pygame.quit()
            exit()
    
    #--MISC--
    screen.blit(background, (0, 0))
    screen.blit(scoresurf, scorerect)
    scoresurf = font.render(str(score), False, '#045703') #Text, AA, color
    screen.blit(boxsurf, boxrect)
    
    #--PLAYER--
    screen.blit(playersurface, playerrect)
    if playerrect.colliderect(boxrect): print('Collided!') #returns 0 if no collision, returns 1 if yes
    
    keys = pygame.key.get_pressed() #Gets ALL of the keys input (dictionary)
    up = keys[pygame.K_w] or keys[pygame.K_UP]
    down = keys[pygame.K_s] or keys[pygame.K_DOWN]
    left = keys[pygame.K_a] or keys[pygame.K_LEFT]
    right = keys[pygame.K_d] or keys[pygame.K_RIGHT]
    
    if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]: moving = True
    else: moving = False
    
    if moving == True and playerspeed <= 3: playerspeed += accspeed 
    elif moving == False: playerspeed = 0
    
    move = pygame.math.Vector2(right - left, down - up)
    if move.length_squared() > 0:
        move.scale_to_length(playerspeed)
        playerrect.center += move  
        playerrect.topleft = round(playerrect.x), round(playerrect.y)   
    
    #--MOUSE--
    mousepos= pygame.mouse.get_pos()
    if boxrect.collidepoint(mousepos) and pygame.mouse.get_pressed()[0]: score += 1
    
    pygame.display.update() #updates screen to keep it running
    clock.tick(framerate) #tells while true loop to run not any faster than [framerate] frames per second
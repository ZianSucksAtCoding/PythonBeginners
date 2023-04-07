#import modules
import pygame
import random
import sys
import time

#variables
screen_width = 800
screen_height = 600
FPS = int(60)

#initialize pygame
pygame.init()

#screen setup & variables
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

#the project is indeed running
running = True

#game loop
while running:
    
    #make the screen color white
    screen.fill("White")
    
    #check if clicking the 'x' button to exit
    #if so, exit. else, continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        else:
            running = True

        #game code

        #update the screen with 60 FPS
        pygame.display.update()
        clock.tick(FPS)

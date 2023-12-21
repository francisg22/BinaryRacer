import pygame
import sys
import random
import time
from pygame.locals import *
#
# Checklist of things to do
    # First - create placeholder UI
    # Second - Display all UI in correct places
    #Third - Finish game mechanics
        #Things needed
            #Variable to keep track of current total number
            #Something to keep track if each bit is on or off (maybe object for each thing?)
            #Timer that will count down until the player gets the number right
            #Level selection - probably in the console before game starts up
                # levels - hexadecimal racer, regular binary, and negative binary
            #For hexadecimal - conversion from random integer to hexadecimal number to display
            #increasing difficulty- probably last thing to do
        
    

#Initialize Pygame
pygame.init()

#Set up the display
screen_width, screen_height = 1300, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Binary Racer")

#Load the image sprite
#sprite_image = pygame.transform.scale(pygame.image.load("images/EagleSprite.jpg"),(100,100))
#sprite_rect = sprite_image.get_rect()
#sprite_speed = 5

#Set the initial position of the sprite
#sprite_rect.x = screen_width // 2 - sprite_rect.width // 2
#sprite_rect.y = screen_height // 2 - sprite_rect.height // 2

# text_to_be_displayed = 'fortnite'

class button:
  def __init__(self,x, y, image)  :
   
    self.image = image
    self.rect = self.image.get_rect()
   
    self.rect.topleft = (x,y)
  


  


  def draw(self):
    screen.blit(self.image , (self.rect.x,self.rect.y))  # blit using the rectangle
    
    



  def onClick(self, x, y):
    
       
    if(self.type == "main" and y<=1000 and y >= 850 and x >=0 and x <= 500):
               #run
      pygame.quit()
      sys.exit()

image = pygame.image.load('images/1red.png').convert_alpha()
buttontest = button(0,0,image)
  
# text_rect = text_surface.get_rect()  # get bounding rectangle
# text_rect.center = (x, y)  # set the center of the rectangle
# screen.blit(text_surface, text_rect)  # blit using the rectangle
    

#testui = UI(image = 'a.png', scale = (1000, 700))
# ui = UI(image = 'GeneralUI.png', type="main", scale = (1000, 300))
# hp1 = UI(image = 'HPBarSelf.png', scale = (200, 20))
# hp1background = UI(image = 'HPBackground.png', scale = (200, 20))
# hp2 = UI(image = 'HPBarOther.png', scale = (200, 20))
# hp2background = UI(image = 'HPBackground.png', scale = (200, 20))
# ArenaBackground = UI(image = 'Background.png', scale = (1000, 700))
# titlescreen = UI(image = 'MainMenu.png', scale = (1000,1000))
# pokeball = UI(image = 'ESD_Pokeball.png', scale = (1000,1000))










# screen.blit(pokeball.sprite, pokeball.rect)
# screen.blit(titlescreen.sprite, titlescreen.rect)

pygame.display.flip()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
              
           
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_presses = pygame.mouse.get_pressed()
          if mouse_presses[0]:
            pos = pygame.mouse.get_pos()
            print(pos)
            
            
       

    
       
    
    
    
    buttontest.draw()
    pygame.display.flip()
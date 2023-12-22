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



class button:
  def __init__(self,x, y, image,scale,type,num,col)  :
    width = image.get_width()
    height = image.get_height()
    self.name = col
    self.image = pygame.transform.scale(image,(int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.num = num
    self.rect.topleft = (x,y)
    self.x = x
    self.y = y
    self.clicked = False
     
    self.type = type

  


  def draw(self):
    change = False
    screen.blit(self.image , (self.rect.x,self.rect.y))  # blit using the rectangle
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        
        if(self.type == 'num' and change == False):
          if 'red' in self.name:
            self.name = 'green'
            img = pygame.image.load('images/'+str(self.num)+'green.png').convert_alpha()
            self.image = img
            change = True  
            
          if 'green' in self.name and change == False:
            self.name = 'red'
            img = pygame.image.load('images/'+str(self.num)+'red.png').convert_alpha()
            self.image = img
            change = True  
            
          screen.blit(self.image , (self.rect.x,self.rect.y))
        elif(self.type == 'binaryquiz'):
          self.clicked = True
        elif(self.type  == 'hexquiz'):
          self.clicked = True
        elif(self.type  == 'submit'):
           return True
      
      if pygame.mouse.get_pressed()[0] == 0:
        self.clicked = False
        



  def onClick(self, x, y):
    
       
    if(self.type == "main" and y<=1000 and y >= 850 and x >=0 and x <= 500):
               #run
      pygame.quit()
      sys.exit()
#loading images
red1 = pygame.image.load('images/1red.png').convert_alpha()
red2 = pygame.image.load('images/2red.png').convert_alpha()
red4 = pygame.image.load('images/4red.png').convert_alpha()
red8 = pygame.image.load('images/8red.png').convert_alpha()
red16 = pygame.image.load('images/16red.png').convert_alpha()
red32 = pygame.image.load('images/32red.png').convert_alpha()
red64 = pygame.image.load('images/64red.png').convert_alpha()
red128 = pygame.image.load('images/128red.png').convert_alpha()
green1 = pygame.image.load('images/1green.png').convert_alpha()
green2 = pygame.image.load('images/2green.png').convert_alpha()
green4 = pygame.image.load('images/4green.png').convert_alpha()
green8 = pygame.image.load('images/8green.png').convert_alpha()
green16 = pygame.image.load('images/16green.png').convert_alpha()
green32 = pygame.image.load('images/32green.png').convert_alpha()
green64 = pygame.image.load('images/64green.png').convert_alpha()
green128 = pygame.image.load('images/128green.png').convert_alpha()
#initializing button objects
button1 = button(1000,500,red1,1,'num',1,'red')
button2 = button(875,507,red2,1,'num',2,'red')
button4 = button(750,507,red4,1,'num',4,'red')
button8 = button(625,507,red8,1,'num',8,'red')
button16 = button(500,507,red16,1,'num',16,'red')
button32 = button(375,507,red32,1,'num',32,'red')
button64 = button(250,507,red64,1,'num',64,'red')
button128 = button(125,507,red128,1,'num',128,'red')


bquiz = pygame.image.load('images/bquiz.png').convert_alpha()
hquiz = pygame.image.load('images/hquiz.png').convert_alpha()
buttonbquiz = button(525,300,bquiz,1,'binaryquiz',0,'none')
buttonhquiz = button(465,450,hquiz,1,'hexquiz',0,'none')

submit = pygame.image.load('images/submit.png').convert_alpha()
buttonsubmit = button(575,600,submit,1,'submit',0,'none')

class image:
  def __init__(self,x, y, image, scale)  :
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image,(int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x,y)
    self.x = x
    self.y = y
    
equals = pygame.image.load('images/equals.png').convert_alpha()
plus = pygame.image.load('images/plus.png').convert_alpha()

equalsign = image(1075,510,equals,1)
plus1 = image(190,510,plus,1)
plus2 = image(315,510,plus,1)
plus3 = image(440,510,plus,1)
plus4 = image(570,510,plus,1)
plus5 = image(690,510,plus,1)
plus6 = image(820,510,plus,1)
plus7 = image(940,510,plus,1)
plus8 = image(700,0,plus,1)







def sum(list):
  sum = 0
  for el in list:
    if(el.name == 'green'):
      sum += el.num
  return sum



font = pygame.font.Font('freesansbold.ttf', 32)
 

 

 




pygame.display.flip()
screenloc = 'menu'
firsttime = -1
num = -1
totalright = 0
while True:
    screen.fill((38, 4, 84))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
              
           
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_presses = pygame.mouse.get_pressed()
          if mouse_presses[0]:
            pos = pygame.mouse.get_pos()
            
            
            
       

    
    
    
    if(screenloc == 'menu'):
      text = font.render('BINARY RACER (Aplha)', True, (0, 255, 0))
      textRect = text.get_rect()
      textRect.center = (650 , 150 )
      screen.blit(text, textRect)

      buttonbquiz.draw()
      buttonhquiz.draw()
      if(buttonbquiz.clicked):
        screenloc = 'bquiz'
        firsttime = 1
      elif(buttonhquiz.clicked):
        screenloc = 'hquiz'
        firsttime = 1
        
      

    

      
    
    else:
      if(screenloc == 'bquiz'):
        
        if(firsttime == 1):
          rand = random.randrange(0, 256)
          num = str(rand)
          firsttime = 0
          
          
        if(firsttime == 0):
          pass
        
        if(buttonsubmit.draw()):
          if(rand == total):
            totalright +=1
            firsttime = 1  
          elif(num != total):
           
            
            firsttime = 1 
            totalright = 0
        
        
      elif(screenloc == 'hquiz'):
        if(firsttime == 1):
          rand = random.randrange(0, 256)
          num = str(hex(rand))[2:]
          firsttime = 0
          
          
        if(firsttime == 0):
          pass
        
        if(buttonsubmit.draw()):
          if(rand == total):
            totalright +=1
            firsttime = 1  
          elif(num != total):
           
            
            firsttime = 1 
            totalright = 0

      #displaying plus and equals
      screen.blit(equalsign.image, equalsign.rect)
      screen.blit(plus1.image, plus1.rect)
      screen.blit(plus2.image, plus2.rect)
      screen.blit(plus3.image, plus3.rect)
      screen.blit(plus4.image, plus4.rect)
      screen.blit(plus5.image, plus5.rect)
      screen.blit(plus6.image, plus6.rect)
      screen.blit(plus7.image, plus7.rect)
    
      #displaying buttons
      button1.draw()
      button2.draw()
      button4.draw() 
      button8.draw()
      button16.draw()
      button32.draw()
      button64.draw()
      button128.draw()
      buttonsubmit.draw()
      #taking the total and displaying it
      total = sum([button1,button2,button4,button8,button16,button32,button64,button128])
      text = font.render(str(total), True, (0, 255, 0))
      textRect = text.get_rect()
      textRect.center = (1200 , 540 )
      screen.blit(text, textRect)

      text = font.render("Number right: " + str(totalright), True, (0, 255, 0))
      textRect = text.get_rect()
      textRect.center = (650 , 400 )
      screen.blit(text, textRect)

      text = font.render(num, True, (0, 255, 0))
      textRect = text.get_rect()
      textRect.center = (650 , 300 )
      screen.blit(text, textRect)

    pygame.display.flip()
import pygame
import pygame.imageext
import os
import math
import time


#Class Used For Rendering the game Backgound
class Background(pygame.sprite.Sprite):
    def __init__(self, pos,rot):
        super(Background,self).__init__()
        self.og_image = pygame.image.load(os.path.join('Assets\images', 'map.png'))
        self.image = self.og_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = rot
        self.velocity = [0, 0]

    def rot(self,rot):
        og_pos = self.rect.center

        self.angle = rot
        self.image = pygame.transform.rotate(self.og_image,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = og_pos

        if self.angle > 360:
            self.angle = 0

        if self.angle < 0:
            self.angle = 360


        # Move for keypresses
    def move(self, pos):
        self.rect.center = pos

    def update(self):
        self.rect.move_ip(self.velocity)

class Button():
    def __init__(self,position,color,highlightColor,textColor,size,textSize,msg,function):
        super().__init__()
        self.pos = position
        self.textColor = textColor
        self.textSize = textSize
        self.color = color
        self.higlightColor = highlightColor
        self.size = size
        self.text = msg
        self.function = function
        self.currentColor = color

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.pos[0] < mouse[0] < self.pos[0]+self.size[0] and self.pos[1] < mouse[1] < self.pos[1]+self.size[1]:
            self.currentColor = self.higlightColor

            if click[0] == 1:
                self.function()
        else:
            self.currentColor = self.color


    def draw(self,screen):
        pygame.draw.rect(screen, self.currentColor, pygame.Rect(self.pos, self.size))

        largeText = pygame.font.SysFont('didot.ttc', self.textSize)
        TextSurf = largeText.render(self.text,True,self.textColor)
        TextRect = (self.pos[0]+10,self.pos[1]+10)
        screen.blit(TextSurf, TextRect)

backgroundRenderGroup = pygame.sprite.RenderPlain()
uiRenderGroup = pygame.sprite.RenderPlain()
foregroundRenderGroup = pygame.sprite.RenderPlain()
background = Background((300, 600),180)
backgroundRenderGroup.add(background)

interactiveUI = [
Button((375,300),(255,0,0),(155,0,0),(0,0,0),(400,100),50,"JOIN ROOM",(lambda : print("JOIN ROOM"))),
Button((375,450),(255,0,0),(155,0,0),(0,0,0),(400,100),50,"CREATE ROOM",(lambda : print("CREATE ROOM"))),
Button((375,600),(255,0,0),(155,0,0),(0,0,0),(400,100),50,"CREDITS",(lambda : print("CREDITS"))),
Button((375,750),(255,0,0),(155,0,0),(0,0,0),(400,100),50,"QUIT",(lambda : pygame.quit()))
]

def updateMainMenuGraphics(win):

    background.move((400-700*math.cos(time.time()*0.075),400-700*math.sin(time.time()*0.075)))

    background.rot(180+25*math.sin(time.time()*0.01))

    backgroundRenderGroup.update()

    win.fill ((255,255,255))

    backgroundRenderGroup.draw(win)

    largeText = pygame.font.SysFont('didot.ttc', 200)
    TextSurf = largeText.render("TANKIO",True,(255,0,0))
    TextRect = (((1152/2)-250),((864/2)-400))
    win.blit(TextSurf, TextRect)

    smallText = pygame.font.SysFont('didot.ttc', 20)
    TextSurf = smallText.render("A Game by MADSC",True,(255,0,0))
    TextRect = (10,844)

    for button in interactiveUI:
        button.update()
        button.draw(win)

    win.blit(TextSurf, TextRect)

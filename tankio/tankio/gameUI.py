import pygame
import pygame.imageext
import os
import math
import time

from PlayerObject import PlayerObject

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


playerList = [PlayerObject((1152/2,864/2),0,False),PlayerObject((1152/2+200,864/2+200),0,True),PlayerObject((1152/2-200,864/2-200),0,True)]

backgroundRenderGroup = pygame.sprite.RenderPlain()
background = Background((300, 600),180)
backgroundRenderGroup.add(background)

foregroundRenderGroup = pygame.sprite.RenderPlain()

for player in playerList:
    foregroundRenderGroup.add(player.playerSprite)
    foregroundRenderGroup.add(player.playerGun)

def updateGameGraphics(win):

    for player in playerList:
        player.update()

    win.fill ((255,255,255))

    background.move((0,0))


    backgroundRenderGroup.draw(win)


    foregroundRenderGroup.update()

    foregroundRenderGroup.draw(win)
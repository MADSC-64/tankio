import pygame
import pygame.imageext
import os
import math
import time

import mainMenu as menu
import gameUI as game

scene = 0

def updateEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def updateGraphics():
    if scene == 0:
        menu.updateMainMenuGraphics(win)
    elif scene == 1:
        game.updateGameGraphics(win)
    
    pygame.display.flip()

def changeScene(sceneID):
    global scene

    scene = sceneID

    print(scene)

    if scene == 1:
        game.createPlayerObjects()





pygame.init()
run = True
win = pygame.display.set_mode((1152, 864))
pygame.display.set_caption("tankio")

programIcon = pygame.image.load('Assets/icon.png')

pygame.display.set_icon(programIcon)

while 1:
    updateEvents()    
    updateGraphics()

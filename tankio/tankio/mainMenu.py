import pygame
import pygame.imageext
import pygame.time
import gameRenderer
import os
import math
import time
from main import mainGameLogic

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
        self.interactive = True
        self.function = function
        self.currentColor = color

    def update(self):
        if self.interactive == False:
            self.currentColor = self.higlightColor
            return


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

class InputField():
    def __init__(self,position,color,highlightColor,textColor,size,textSize,function):
        super().__init__()
        self.pos = position
        self.textColor = textColor
        self.textSize = textSize
        self.color = color
        self.higlightColor = highlightColor
        self.size = size
        self.text = ""
        self.active = False
        self.function = function
        self.currentColor = color

    def draw(self,screen):
        pygame.draw.rect(screen, self.currentColor, pygame.Rect(self.pos, self.size))

        largeText = pygame.font.SysFont('didot.ttc', self.textSize)
        TextSurf = largeText.render(self.text,True,self.textColor)
        TextRect = (self.pos[0]+10,self.pos[1]+10)
        screen.blit(TextSurf, TextRect)

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.pos[0] < mouse[0] < self.pos[0]+self.size[0] and self.pos[1] < mouse[1] < self.pos[1]+self.size[1]:
            self.currentColor = self.higlightColor

            if click[0] == 1:
                self.active = True
        else:
            self.currentColor = self.color

        for event in pygame.event.get():
            if self.active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_KP_ENTER:
                    self.function(self.text)
                elif event.key == pygame.K_RETURN:
                    self.function(self.text)
                else:
                    self.text  += event.unicode


def changeMainMenuScene(scene):
    global main_menu_scene

    main_menu_scene = scene

def createUser(msg):
    mainGameLogic.createUser(msg)

    changeMainMenuScene(0)

def joinRoom(msg):
    global joining_error

    if mainGameLogic.joinRoom(msg) == None:
        changeMainMenuScene(0)
        return

    changeMainMenuScene(3)



def createRoom():
    mainGameLogic.createRoom()

    changeMainMenuScene(3)

main_menu_scene = 1

backgroundRenderGroup = pygame.sprite.RenderPlain()
uiRenderGroup = pygame.sprite.RenderPlain()
foregroundRenderGroup = pygame.sprite.RenderPlain()
background = Background((300, 600),180)
backgroundRenderGroup.add(background)

interactiveUIMain = [
Button((375,300),(255,0,0),(155,0,0),(0,0,0),(400,100),50,"JOIN ROOM",(lambda : changeMainMenuScene(2))),
Button((375,450),(255,0,0),(155,0,0),(0,0,0),(400,100),50,"CREATE ROOM",(lambda : createRoom())),
Button((375,600),(255,0,0),(155,0,0),(0,0,0),(400,100),50,"CREDITS",(lambda : print("CREDITS"))),
Button((375,750),(255,0,0),(155,0,0),(0,0,0),(400,100),50,"QUIT",(lambda : pygame.quit()))
]

interactiveUICreation = [
InputField((375,450),(255,0,0),(155,0,0),(0,0,0),(400,100),50,(lambda a: createUser(a))),
]


interactiveUIJoining = [
InputField((375,450),(255,0,0),(155,0,0),(0,0,0),(400,100),50,(lambda a: joinRoom(a))),
]

interactiveUILobby = [
Button((375,750),(255,0,0),(155,0,0),(0,0,0),(400,100),50,"START GAME",(lambda : mainGameLogic.update_room_data("readyToJoin",True)))
]

def updateMainMenuGraphics(win):

    background.move((400-700*math.cos(time.time()*0.01),400-700*math.sin(time.time()*0.01)))

    background.rot(90+25*math.sin(time.time()*0.01))

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

    if main_menu_scene == 0:
        for button in interactiveUIMain:
            button.update()
            button.draw(win)

        win.blit(TextSurf, TextRect)

    elif main_menu_scene == 1:
        largeText = pygame.font.SysFont('didot.ttc', 50)
        TextSurf = largeText.render("NAME:",True,(255,0,0))
        TextRect = (((1152/2)-50),((864/2)-50))
        win.blit(TextSurf, TextRect)

        for button in interactiveUICreation:
            button.update()
            button.draw(win)

        win.blit(TextSurf, TextRect)

    
    if main_menu_scene == 2:
        largeText = pygame.font.SysFont('didot.ttc', 50)
        TextSurf = largeText.render("ID:",True,(255,0,0))
        TextRect = (((1152/2)-50),((864/2)-50))
        win.blit(TextSurf, TextRect)

        for button in interactiveUIJoining:
            button.update()
            button.draw(win)

        win.blit(TextSurf, TextRect)

    if main_menu_scene == 3:
        try:
            largeText = pygame.font.SysFont('didot.ttc', 50)
            TextSurf = largeText.render("ROOM #"+str(mainGameLogic.token)+" WAITING FOR OTHERS TO START:",True,(255,0,0))
            TextRect = ((50),((864/2)-200))
            win.blit(TextSurf, TextRect)

            roomData = mainGameLogic.getRoomData()

            if roomData == None:
                return

            player_count = 0

            ready_players = 0

            total_players = len(roomData["players"])

            for playerObject in roomData["players"]:
                player_count += 50
                player_name = str( playerObject["name"])
                player_id = str( playerObject["id"])

                player = "("+player_name+", "+player_id+")"

                player_text = player_name+"  #"+player_id+" connected"

                for events in roomData["roomEvents"][player]:
                    if events["eventName"] == "readyToJoin":
                        player_text += " and ready to join"
                        ready_players += 1

                TextSurf = largeText.render(player_text,True,(255,0,0))
                TextRect = ((50),((864/2)-200+ player_count))
                win.blit(TextSurf, TextRect)

            for button in interactiveUILobby:
                button.text = "Start Game "+str(ready_players)+"/"+str(total_players)

                button.update()
                button.draw(win)

            if ready_players == total_players:
                gameRenderer.changeScene(1)

            pygame.time.wait(50)

        except(Exception):
            return

        


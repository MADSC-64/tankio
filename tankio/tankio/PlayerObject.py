import pygame
import os
import pygame.imageext
import roomNetworking as network
import math

class PlayerObject(object):
    def __init__(self, pos,rot,is_npc,username,user_id,room_token):
        super(PlayerObject,self).__init__()
        self.playerSprite = Player((0,0),0,"blue")
        self.playerGun = PlayerGun((0,0),0,"Blue")
        self.is_npc = is_npc

        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.rot = rot
        self.weapon_rot = 0

        self.username = username
        self.user_id = user_id
        self.room_token = room_token

       
    def update(self):

        self.playerSprite.move((self.pos_x,self.pos_y))

        print(self.weapon_rot*(math.pi / 180))

        gun_x_pos,gun_y_pos = self.pos_x - math.sin(self.weapon_rot*(math.pi / 180))*8,self.pos_y 

        self.playerGun.move((gun_x_pos,gun_y_pos))

        self.playerSprite.rot(self.rot)
        self.playerGun.rot(self.weapon_rot)

        if self.is_npc:
            return

        pos_data = {'x':self.pos_x,'y':self.pos_y,'rotation':self.rot,'weaponRotation':self.weapon_rot}

        network.update_room_data(self.room_token,self.username,self.user_id,pos_data,'position')


        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.pos_x, mouse_y - self.pos_y

        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)-90

        self.weapon_rot = angle

        self.playerGun.rot(angle)

        if (pygame.key.get_pressed()[pygame.K_LEFT]):
            self.rot += 5
        if (pygame.key.get_pressed()[pygame.K_RIGHT]):
            self.rot += -5
        if (pygame.key.get_pressed()[pygame.K_UP]):
            self.pos_x  -= math.sin(self.rot*(math.pi / 180))*4
            self.pos_y -= math.cos(self.rot*(math.pi / 180))*4
        if (pygame.key.get_pressed()[pygame.K_DOWN]):
            self.pos_x  -= math.sin(self.rot*(math.pi / 180))*-4
            self.pos_y -= math.cos(self.rot*(math.pi / 180))*-4

        if self.rot > 360:
            self.rot = self.rot-360

        if self.rot < 0:
            self.rot = 360 - self.rot


class Player(pygame.sprite.Sprite):
    def __init__(self, pos,rot,color):
        super(Player,self).__init__()
        self.og_image = pygame.image.load(os.path.join('Assets\images', f'tankBody_{color}.png'))
        self.image = self.og_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = rot
        self.velocity = [0, 0]
        self.color = color

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

class PlayerGun(pygame.sprite.Sprite):
    def __init__(self, pos,rot,color):
        super(PlayerGun,self).__init__()
        self.og_image = pygame.image.load(os.path.join('Assets\images', f'tank{color}_barrel1_outline.png'))
        self.image = self.og_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = rot
        self.velocity = [0, 0]
        self.color = color

    def rot(self,rot):
        og_pos = self.rect.center

        self.angle = rot
        self.image = pygame.transform.rotate(self.og_image,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = og_pos 

        # Move for keypresses
    def move(self, pos):
        self.rect.center = pos

    def update(self):
        self.rect.move_ip(self.velocity)
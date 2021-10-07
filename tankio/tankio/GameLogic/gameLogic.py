import pygame
import pygame.imageext

def updateGraphics():
    while 1:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill ((255,255,255))
        largeText = pygame.font.SysFont('didot.ttc', 72)
        TextSurf = largeText.render("TANKIO",True,(255,0,0))
        TextRect = (((500/2)-100),((500/2)-75))
        win.blit(TextSurf, TextRect)
        pygame.display.update()


pygame.init()
run = True
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("tankio")

fonts = pygame.font.get_fonts()
print(len(fonts))
for i in range(7):
    print(fonts[i])

updateGraphics()


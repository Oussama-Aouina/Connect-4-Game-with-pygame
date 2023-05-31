import pygame
from gameView import *
class Pion(pygame.sprite.Sprite):
    #initialiser le pion par une image et une position
    def __init__(self,PionIcon,pos,goal):
        super().__init__()
        self.image = pygame.image.load(PionIcon)
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.goal=goal

    def move(self):
        if self.rect.center[1]<self.goal:
            self.rect.y+=3


class Player:
    def __init__(self,id,PlayerIcon,PionIcon):

        self.playerId=id
        self.playerIcon=pygame.image.load(PlayerIcon)
        self.playerIcon_rect=self.playerIcon.get_rect()
        self.Pions=pygame.sprite.Group()
        self.PionIcon=PionIcon

    def LacherPion(self,pos,goal):
        self.Pions.add(Pion(self.PionIcon,pos,goal))


# pygame.display.set_caption("Connect 4 Game")
# screen=pygame.display.set_mode((1080,720))
# jouer=True
# while jouer:
#
#     bg1=pygame.image.load("Assets/bg1.jpg")
#     screen.blit(bg1,(0,0))
#     p1=Player(1,"Assets/RedPlayerIcon.png","Assets/RedPion.png")
#     screen.blit(p1.playerIcon,p1.playerIcon_rect)
#     p1.LacherPion(p1.playerIcon_rect.center)
#     p1.Pions.draw(screen)
#     pygame.display.flip()
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             jouer =False
#             pygame.quit()

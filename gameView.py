

import pygame
from game import *
from player import *


class gameView:

    def __init__(self):

        self.pyGame = pygame
        # initialiser le jeu et regler l'ecran
        pygame.init()
        pygame.display.set_caption("Connect 4 Game")
        self.screen = pygame.display.set_mode((1080, 720))
        # initialiser le jeu et la matrice principale:
        self.game = game()
        # reglage des images de background
        self.bg1 = pygame.image.load("Assets/bg1.jpg")
        self.bg2 = pygame.image.load("Assets/bg2.jpg")

        # reglage de cursseur
        self.cur = pygame.image.load("Assets/cursor.png")
        self.cur_rect = self.cur.get_rect()

        # maitre le cursseur par défaut invisible
        pygame.mouse.set_visible(False)

        # reglage de Loading Assets
        self.Load = pygame.image.load("Assets/Loading ....png")
        self.Load_rect = self.Load.get_rect()
        self.Load_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2 + 50)
        self.Load_Symbol = pygame.image.load("Assets/Loading3.png")
        self.Load_Symbol_rect = self.Load_Symbol.get_rect()
        self.Load_Symbol_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2 - 50)
        self.Load_Symbol_origin = self.Load_Symbol
        self.Load_Symbol_angle = 0
        self.c1 = pygame.image.load("Assets/c1.png")
        self.c4 = pygame.image.load("Assets/c4.png")
        self.c3 = pygame.image.load("Assets/c3.png")
        self.c2 = pygame.image.load("Assets/c2.png")
        self.c1_rect = self.c1.get_rect()
        self.c1_rect.center = (0, 453)
        self.c2_rect = self.c2.get_rect()
        self.c2_rect.center = (-50, 453)
        self.c3_rect = self.c3.get_rect()
        self.c3_rect.center = (-100, 453)
        self.c4_rect = self.c1.get_rect()
        self.c4_rect.center = (-150, 453)

        # reglage de Powred by abd dedicace Assets:
        self.Powred_By = pygame.image.load("Assets/Powred By _.png")
        self.Powred_By_rect = self.Powred_By.get_rect()
        self.Powred_By_rect.center = (self.screen.get_width() // 2, self.screen.get_height() - 70)

        # reglage de starting Assets:
        self.Start_Trans = pygame.image.load("Assets/Start_ Transparent.png")
        self.Start_Clear = pygame.image.load("Assets/Start_Clair.png")
        self.Start_Trans_rect = self.Start_Trans.get_rect()
        self.Start_Clear_rect = self.Start_Clear.get_rect()
        self.Start_Clear_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2 - 10)
        self.Start_Trans_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2 - 10)
        self.Dedicace = pygame.image.load("Assets/Dedicace.png")
        self.Dedicace_rect = self.Dedicace.get_rect()
        self.Dedicace_rect.x = 40
        self.Dedicace_rect.y = 40
        self.GameBunner = pygame.image.load("Assets/GameBunner.png")
        self.GameBunner_rect = self.GameBunner.get_rect()
        self.GameBunner_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2 + 140)
        self.start = True

        # reglage de playing Assets:

        self.GameTable = pygame.image.load("Assets/GameTable3D.png")
        self.GameTable_rect = self.GameTable.get_rect()
        self.GameTable_rect.x = 50
        self.GameTable_rect.y = 120
        self.TurnOf = pygame.image.load("Assets/TurnOfPlayer.png")
        self.TurnOf_rect = self.TurnOf.get_rect()
        self.TurnOf_rect.y = 120 + self.GameTable.get_height() // 2
        self.TurnOf_rect.x = self.GameTable.get_width() + 80
        self.TurnOf_rect.bottom = self.GameTable_rect.bottom
        self.Pointer = pygame.image.load("Assets/Pointer.png")
        self.Pointer_rect = self.Pointer.get_rect()
        self.Pointer_rect.y = 20
        self.playing=True

        # les reference de tableau/l'echelle de conversion:

        # chaque position de pion sur l'axe x correspond au numero de colonne dans le tableau:
        self.codingColumns = {}
        j = 0
        for i in range(122, 630, 84):
            self.codingColumns[i] = j
            j += 1
        print(self.codingColumns)
        # chaque position de pion sur l'axe y correspond au numero de ligne dans le tableau:
        self.decodingLigns = {}
        j = 183
        for i in range(6):
            self.decodingLigns[i] = j
            j += 84
        print(self.decodingLigns)
        self.yellow = pygame.image.load("Assets/YellowPion.png")
        self.yellow_rect = self.yellow.get_rect()
        self.yellow_rect.center = (373, 20)

        # reglage des joueurs et de joueur courrant:
        self.p1 = Player(1, "Assets/RedPlayerIcon.png", "Assets/RedPion.png")
        self.p2 = Player(2, "Assets/YellowPlayerIcon.png", "Assets/YellowPion.png")
        if self.game.pions%2==0:
            self.crrentPlayer = self.p1
        else:
            self.crrentPlayer=self.p2
        self.crrentPlayer.playerIcon_rect.center = (self.TurnOf_rect.center[0], self.TurnOf_rect.center[1] + 25)

        #reglage des Assets de fin de jeu:
        self.EndScreen=pygame.image.load("Assets/Do you wanna play again _.png")
        self.EndScreen_rect=self.EndScreen.get_rect()
        self.TheWinnerIs=pygame.image.load("Assets/Winner.png")
        self.TheWinnerIs_rect=self.TheWinnerIs.get_rect()
        self.TheWinnerIs_rect.center=(self.EndScreen_rect.center[0],self.EndScreen_rect.center[1] - 100)
        self.Equal=pygame.image.load("Assets/NO ONE WINS ....png")
        self.Equal_rect=self.Equal.get_rect()
        self.Equal_rect.center=(self.TheWinnerIs_rect.center[0],self.TheWinnerIs_rect.center[1] +50)
        self.YesClear=pygame.image.load("Assets/Yes _clair.png")
        self.Yes_rect=self.YesClear.get_rect()
        self.Yes_rect.center=(720,550)
        self.YesTrans=pygame.image.load("Assets/Yes _Transparent.png")
        self.NoClear=pygame.image.load("Assets/No _Clair.png")
        self.NoTrans=pygame.image.load("Assets/No _transparent.png")
        self.No_rect=self.NoClear.get_rect()
        self.No_rect.center=(320,550)
        self.Player_rect=(self.EndScreen_rect.center[0] -50,self.EndScreen_rect.center[1])

    # reglage de loading Screen
    def Loading(self):

        self.screen.blit(self.bg1, (0, 0))
        self.screen.blit(self.Load, self.Load_rect)
        self.screen.blit(self.Load_Symbol, self.Load_Symbol_rect)
        self.screen.blit(self.Powred_By, self.Powred_By_rect)
        self.Load_Symbol_angle -= 10
        self.Load_Symbol = pygame.transform.rotozoom(self.Load_Symbol_origin, self.Load_Symbol_angle, 1)
        self.Load_Symbol_rect = self.Load_Symbol.get_rect(center=self.Load_Symbol_rect.center)

        self.screen.blit(self.c1, self.c1_rect)
        self.screen.blit(self.c2, self.c2_rect)
        self.screen.blit(self.c3, self.c3_rect)
        self.screen.blit(self.c4, self.c4_rect)
        if self.c1_rect.x < self.screen.get_width() // 3 - 150:
            self.c1_rect.x += 1
            self.c2_rect.x += 2
            self.c3_rect.x += 3
            self.c4_rect.x += 4

        else:
            self.c1_rect.x += 4
            self.c2_rect.x += 3
            self.c3_rect.x += 2
            self.c4_rect.x += 1

    # reglage de mouvement de cursseur
    def cursorMoving(self):
        self.cur_rect.center = pygame.mouse.get_pos()
        self.screen.blit(self.cur, pygame.mouse.get_pos())

    # reglage de mouvement de pointer:
    def pointerMoving(self):
        # Pointer movements:
        if 55 < pygame.mouse.get_pos()[0] < 678 and self.playing:
            # for e in self.Columns.keys():
            #     if 42<= pygame.mouse.get_pos()[0]-e <=42:
            #         self.Pointer_rect.x=e
            #     # else:
            #     #     self.Pointer_rect.center=(pygame.mouse.get_pos()[0],20)
            if 84 < pygame.mouse.get_pos()[0] < 148:
                self.Pointer_rect.center = (122, self.Pointer_rect.center[1])
            elif 170 < pygame.mouse.get_pos()[0] < 234:
                self.Pointer_rect.center = (206, self.Pointer_rect.center[1])
            elif 254 < pygame.mouse.get_pos()[0] < 318:
                self.Pointer_rect.center = (290, self.Pointer_rect.center[1])
            elif 340 < pygame.mouse.get_pos()[0] < 404:
                self.Pointer_rect.center = (374, self.Pointer_rect.center[1])
            elif 426 < pygame.mouse.get_pos()[0] < 490:
                self.Pointer_rect.center = (458, self.Pointer_rect.center[1])
            elif 512 < pygame.mouse.get_pos()[0] < 576:
                self.Pointer_rect.center = (542, self.Pointer_rect.center[1])
            elif 598 < pygame.mouse.get_pos()[0] < 662:
                self.Pointer_rect.center = (626, self.Pointer_rect.center[1])

    # reglege de Start Screen
    def Starting(self):

        self.screen.blit(self.bg1, (0, 0))
        self.screen.blit(self.Powred_By, self.Powred_By_rect)
        if self.Start_Trans_rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.Start_Clear, self.Start_Clear_rect)
        else:
            self.screen.blit(self.Start_Trans, self.Start_Trans_rect)
        self.screen.blit(self.GameBunner, self.GameBunner_rect)
        self.screen.blit(self.Dedicace, self.Dedicace_rect)

    def checkPositions(self,p):
        for e in p.Pions:
            if e.rect.center[1]<e.goal:
                return False
        return True

    # reglage de Playing Mode:
    def Playing(self):
        # affichage de Background et ses elements
        self.screen.blit(self.bg1, (0, 0))
        self.screen.blit(self.TurnOf, self.TurnOf_rect)

        # affichage de log De Pion de chaque joueur dans sa position:
        self.crrentPlayer.playerIcon_rect.center = (self.TurnOf_rect.center[0], self.TurnOf_rect.center[1] + 25)
        self.screen.blit(self.crrentPlayer.playerIcon, self.crrentPlayer.playerIcon_rect)

        # affichage de pointeur des positions
        self.screen.blit(self.Pointer, self.Pointer_rect)

        # afficher tous les pions joués
        self.p1.Pions.draw(self.screen)
        self.p2.Pions.draw(self.screen)
        for pion1 in self.p1.Pions:
            pion1.move()
        for pion2 in self.p2.Pions:
            pion2.move()

        #affichage de la table de jeu:
        self.screen.blit(self.GameTable, self.GameTable_rect)

        # Pointer movements:
        self.pointerMoving()

        #indiquer s'il y'a un gagnant:
        self.findWinner()



    #chercher s'il y'a un gagnant ou une égalité
    def findWinner(self):
        if self.game.checkWinner(self.p1.playerId) and self.checkPositions(self.p1):
            self.Endgame()
            self.Winning(self.p1)

        elif self.game.checkWinner(self.p2.playerId) and self.checkPositions(self.p2):
            self.Endgame()
            self.Winning(self.p2)

        elif self.game.pions <= 0 :
            self.Endgame()
            self.Egality()
    #reglage de l'écran dans le cas ou il y'a un gagnant:
    def Winning(self,Player):
        self.screen.blit(self.TheWinnerIs,self.TheWinnerIs_rect)
        self.screen.blit(Player.playerIcon,self.Player_rect)
    #reglage de l'écran dans le cas de l'égalité
    def Egality(self):
        self.screen.blit(self.Equal,self.Equal_rect)
    #réglage de l'écran dans la fin de jeu
    def Endgame(self):
        self.playing=False
        self.screen.blit(self.EndScreen,(0,0))
        if self.No_rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.NoClear,self.No_rect)
        else:
            self.screen.blit(self.NoTrans,self.No_rect)
        if self.Yes_rect.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.YesClear,self.Yes_rect)
        else:
            self.screen.blit(self.YesTrans,self.Yes_rect)


    # Principal Function
    def play(self):

        play = True
        while play:
            Load=True
            self.Loading()
            if self.c4_rect.x >= self.screen.get_width():
                Load=False
            if not Load:

                if self.start:
                    self.Starting()
                else:
                    self.Playing()
                self.cursorMoving()
            # mise a jour de l'écran
            pygame.display.flip()

            # traquer les différents évènements:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    play = False
                    pygame.quit()
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    # verifier si le boutton START est appuié pour commencer le jeu:
                    if self.Start_Clear_rect.collidepoint(e.pos) and self.start:
                        self.start = False
                    # le cas dans lequel le jeu n'a pas encore terminé
                    elif self.playing:
                    #choisir les différentes endroits pour lancer les pions
                        if self.GameTable_rect.collidepoint(e.pos) :
                            c=self.game.putPion(self.crrentPlayer.playerId, self.codingColumns[self.Pointer_rect.center[0]])
                            if c>-1:
                                print(c)
                                print(self.decodingLigns[c])
                                #lancement de pion de joueur courrant:
                                self.crrentPlayer.LacherPion(self.Pointer_rect.center,self.decodingLigns[c])

                                if self.game.pions%2==0:
                                    self.crrentPlayer=self.p1
                                elif self.game.pions%2==1:
                                    self.crrentPlayer=self.p2
                    #dans le cas ou le jeu est terminé:
                    else:
                        if self.Yes_rect.collidepoint(e.pos):
                            s=gameView()
                            s.Play_again()
                        elif self.No_rect.collidepoint(e.pos):
                            play=False
                            pygame.quit()

    #methode pour rejouer
    def Play_again(self):
        play = True
        while play:

            self.Playing()
            self.cursorMoving()
            # mise a jour de l'écran
            pygame.display.flip()

            # traquer les différents évènements:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    play = False
                    pygame.quit()
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    # le cas dans lequel le jeu n'a pas encore terminé
                    if self.playing:
                    #choisir les différentes endroits pour lancer les pions
                        if self.GameTable_rect.collidepoint(e.pos) :
                            c=self.game.putPion(self.crrentPlayer.playerId, self.codingColumns[self.Pointer_rect.center[0]])
                            if c>-1:
                                print(c)
                                print(self.decodingLigns[c])
                                #lancement de pion de joueur courrant:
                                self.crrentPlayer.LacherPion(self.Pointer_rect.center,self.decodingLigns[c])

                                if self.game.pions%2==0:
                                    self.crrentPlayer=self.p1
                                elif self.game.pions%2==1:
                                    self.crrentPlayer=self.p2
                    #dans le cas ou le jeu est terminé:
                    else:
                        if self.Yes_rect.collidepoint(e.pos):
                            s=gameView()
                            s.Play_again()
                        elif self.No_rect.collidepoint(e.pos):
                            play=False
                            pygame.quit()

if __name__ == '__main__':
    g = gameView()
    g.play()

import pygame
#import du composant
from playerone import Playerone
#création de la classe représentant le jeu
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #genere le joueur
        self.playerone=Playerone()
        #touche appuyée, le dictionnaire associe une une touche à
        self.touche_appuyee={}

import pygame
import os
class Player(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__()
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))
    self.image = pygame.image.load(os.path.join(sourceFileDir, "graphics", "player.png")).convert_alpha()
    self.rect = self.image.get_rect(midbottom = pos)
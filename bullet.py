import pygame 
import colors
import constants 
import random 

class Bullet(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/missile1.png")
    self.image.set_colorkey(colors.WHITE)
    self.rect = self.image.get_rect()

    self.size = self.image.get_size()
        # create a 2x bigger image than self.image
    self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.5), int(self.size[1]*0.5)))
  
  def update(self):
    self.rect.y -= 10

    if self.rect.y < 0:
      self.kill()
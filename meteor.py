import pygame 
import colors
import constants 
import random 

class Meteor(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/meteor1.png")
    self.image.set_colorkey(colors.WHITE)
    self.rect = self.image.get_rect()

    self.size = self.image.get_size()
        # create a 2x bigger image than self.image
    self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.25), int(self.size[1]*0.25)))
  
  def update(self):
    self.rect.y += random.randint(1,10)

    if self.rect.y > constants.DEFAULT_SCREEN_SIZE[1]*2:
      self.rect.y = -200
      self.rect.x = random.randint(0,constants.DEFAULT_SCREEN_SIZE[0])
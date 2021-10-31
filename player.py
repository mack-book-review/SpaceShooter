import pygame 
import colors

class Player(pygame.sprite.Sprite):
  """
  This class represents the player spaceship; it derives from the "Sprite" cass in pygame
  """

  def __init__(self,img_path):

    #Call the parent class (Sprite) constructor
    super().__init__()

    self.health = 20
    self.is_colliding = False
    self.img_path = img_path
  
    self.image = pygame.image.load(img_path)

    self.image.set_colorkey(colors.WHITE)

    #Store a reference to the 'rect' object, which holds information about player position and size
    self.rect = self.image.get_rect()
    self.size = self.image.get_size()
    self.width = self.size[0]
    self.height = self.size[1]


  
  def draw(self,screen):
    self.image.blit(screen,[self.rect.x,self.rect.y])

  def get_size(self):
    return [self.rect.width,self.rect.height]

  def get_position(self):
    return [self.rect.x,self.rect.y]
  
  def set_position(self,x,y):
    self.rect.x = x 
    self.rect.y = y

import pygame 
import colors
import constants 
import random 
import math 

class Enemy(pygame.sprite.Sprite):
  RAND_ALIENS = ["alien_beige","alien_blue","alien_green","alien_pink","alien_yellow"]

  EXPLOSION_TEXTURES = [
    pygame.image.load("assets/explosionTextures/regularExplosion00.png"),
    pygame.image.load("assets/explosionTextures/regularExplosion01.png"),
    pygame.image.load("assets/explosionTextures/regularExplosion02.png"),pygame.image.load("assets/explosionTextures/regularExplosion03.png"),
    pygame.image.load("assets/explosionTextures/regularExplosion04.png"),pygame.image.load("assets/explosionTextures/regularExplosion05.png"),pygame.image.load("assets/explosionTextures/regularExplosion06.png"),    
    pygame.image.load("assets/explosionTextures/regularExplosion07.png"),
     pygame.image.load("assets/explosionTextures/regularExplosion08.png")    
    ]

  def __init__(self,screen):
    super().__init__()

    self.screen = screen 

    rand_num = random.randrange(0,len(Enemy.RAND_ALIENS))
    rand_alien = Enemy.RAND_ALIENS[rand_num]
    img_path = "assets/" + rand_alien + ".png"
    self.moving_right = True
    self.image = pygame.image.load(img_path)
    self.image.set_colorkey(colors.WHITE)
    self.rect = self.image.get_rect()

    self.size = self.image.get_size()
        # create a 2x bigger image than self.image
    self.image = pygame.transform.scale(self.image, (int(self.size[0]*0.5), int(self.size[1]*0.5)))

    self.explosion_timer = 0 
    self.explosion_interval = 5000
    self.current_explosion_texture = 0

   
  def runExplosionAnimation(self,finishCallback):
    print("Running explosion animation")
    # if self.current_explosion_texture >= len(Enemy.EXPLOSION_TEXTURES):
    #   print("Finished running animation")
    #   return
      
    while self.current_explosion_texture < len(Enemy.EXPLOSION_TEXTURES):

      ticks = pygame.time.get_ticks()

      self.explosion_timer += math.floor(ticks/1000)

      if self.explosion_timer > self.explosion_interval:
        self.screen.blit(Enemy.EXPLOSION_TEXTURES[self.current_explosion_texture],[self.rect.x,self.rect.y])
        self.current_explosion_texture += 1
        self.explosionTimer = 0
    
    finishCallback()
  
  def kill(self):
    print("Enemy is being killed")
    self.runExplosionAnimation(super().kill)
  
  
  def update(self):
    if self.moving_right:
      self.rect.x += random.randint(1,10)
      if self.rect.x > constants.DEFAULT_SCREEN_SIZE[0]:
        self.moving_right = False
    else:
      self.rect.x -= random.randint(1,10)
      if self.rect.x < 0:
        self.moving_right = True
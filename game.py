import pygame
import player
import colors 
import constants
import random
from meteor import Meteor
from bullet import Bullet
from enemy import Enemy
import math 

class Game(object):
 

  def __init__(self):
    pygame.init() 
    self.caption_text = ""
    self.score = 0
    self.clock = pygame.time.Clock()
    self.playerDebounceTimer = 0
    self.playerDebounceInterval = 3000

    self.enemySpawnTimer = 0 
    self.enemySpawnInterval = 5000

    self.screen = pygame.display.set_mode(constants.DEFAULT_SCREEN_SIZE)

    self.all_sprites_list = pygame.sprite.Group()
    self.meteor_list = pygame.sprite.Group()
    self.bullet_list = pygame.sprite.Group()
    self.enemy_list = pygame.sprite.Group()
    
    self.player = player.Player("assets/spaceship.png")

    self.all_sprites_list.add(self.player)
    
    #spawn meteors
    self.spawnMeteors(3)

    #spawn enemies
    self.spawnEnemies(2)

  

    player_width,player_height = self.player.get_size()

    self.player.set_position(constants.DEFAULT_SCREEN_SIZE[0]*0.5,constants.DEFAULT_SCREEN_SIZE[1]*0.8)

    self.load_background_image("assets/starry_sky.jpg")

  def load_background_image(self,img_path):
    self.bg_image = pygame.image.load(img_path)

  def get_mouse_pos(self):
    return pygame.mouse.get_pos()
  
  def update_background(self):
    self.screen.blit(self.bg_image,[0,0])
  
  def spawnMeteors(self,numberMeteors):
    for i in range(numberMeteors):
      m1 = Meteor()
      m1.rect.x = random.randint(0,constants.DEFAULT_SCREEN_SIZE[0]*0.90)
      self.meteor_list.add(m1)
      self.all_sprites_list.add(m1)

  def spawnEnemies(self,numberEnemies):
    if len(self.enemy_list) > 10: 
      return 

    for i in range(numberEnemies):
      a1 = Enemy(self.screen)
      a1.rect.x = random.randint(0,constants.DEFAULT_SCREEN_SIZE[0]*0.90)
      a1.rect.y = random.randint(0,200)
      self.enemy_list.add(a1)
      self.all_sprites_list.add(a1)
  
  
      
            


  def run_game(self):
    done = False 

    #Main game loop 
    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            self.player.rect.x -= 20
          elif event.key == pygame.K_RIGHT: 
            self.player.rect.x += 20
          elif event.key == pygame.K_SPACE:
            bullet = Bullet()
            self.bullet_list.add(bullet)
            self.all_sprites_list.add(bullet)
            bullet.rect.x = self.player.rect.x + self.player.width*0.5
            bullet.rect.y = self.player.rect.y

      #clear the screen 
      self.update_background()

      #Get ticks
      ticks = pygame.time.get_ticks()

      self.playerDebounceTimer += math.floor(ticks/1000)
      

      if self.playerDebounceTimer > self.playerDebounceInterval:
        if self.player.is_colliding:
          self.player.is_colliding = False
        self.playerDebounceTimer = 0
      
      self.enemySpawnTimer += math.floor(ticks/1000)

      if self.enemySpawnTimer > self.enemySpawnInterval:
        self.spawnEnemies(random.randint(1,5))
        self.enemySpawnTimer = 0

      #draw the player
      self.all_sprites_list.draw(self.screen)
      self.meteor_list.update()
      self.bullet_list.update()
      self.enemy_list.update()

      #check collisions
      
      

      if not self.player.is_colliding:
  
        player_hit = pygame.sprite.spritecollideany(self.player,self.meteor_list,pygame.sprite.collide_rect_ratio(0.5))
        if player_hit:
          self.player.is_colliding = True
          self.player.health -= 1
          self.player.playerDebounceTimer = 0
        
   
      sprite_dict = pygame.sprite.groupcollide(self.enemy_list,self.bullet_list,True,True,pygame.sprite.collide_rect_ratio(0.15))

      for enemy in sprite_dict.keys():
        self.score += 1
     
      
      self.caption_text = "Score: " + str(self.score) + " "
      self.caption_text += "| Player Health: " + str(self.player.health) 

      pygame.display.set_caption(self.caption_text)
      #update the screen
      pygame.display.flip()

      #set the frame rate
      self.clock.tick(60)
    
    pygame.quit()
    


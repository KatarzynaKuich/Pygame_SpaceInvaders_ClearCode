import pygame, sys
from player import Player

#class
class Game:
  def __init__(self):
    player_sprite = Player((screen_width/2,screen_hight))
    self.player = pygame.sprite.GroupSingle(player_sprite)
    
  def run(self):
    self.player.update()
    self.player.draw(screen)
    
#++++++++

#start

if __name__==('__main__'):#checks if this file is run
  
  pygame.init()
  #settings----------------
  screen_width = 600
  screen_hight = 600
  screen = pygame.display.set_mode((screen_width,screen_hight))
  clock=pygame.time.Clock()
  game=Game() #odwolanie do klasy
  #-------------------------
  #-init-----------------------
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    screen.fill((30,30,30)) #black?
    pygame.display.flip() #update screen
    clock.tick(60)
    game.run() #our instance of class Game
  #-------------------------
  
  
  for row_index,row in enumerate(layout):
    for col_index,cell in enumerate(row):
      x = col_index* tile_size
      y = row_index* tile_size
  
      if cell == 'X':
        tile = Tile((x,y),tile_size)
        self.tiles.add(tile)
      

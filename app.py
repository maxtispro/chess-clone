import pygame
from pygame.sprite import Group
from src.piece import Color
from src.board import Board

def run_chess():

  # Initialize window
  pygame.init()
  screen = pygame.display.set_mode((600, 600))
  clock = pygame.time.Clock()
  running = True

  # Initialize Chess Board
  group = Group()
  Board(Color.WHITE, 600, group)

  while running:
    for event in pygame.event.get():
      if event.type ==  pygame.QUIT:
        running = False
    
    screen.fill('beige')
    group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

  pygame.quit()


if __name__ == '__main__':
  run_chess()
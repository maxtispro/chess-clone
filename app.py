from pprint import pprint
import pygame
from src.board import Board

def run_chess():

  # Initialize window
  pygame.init()
  screen = pygame.display.set_mode((600, 700))
  clock = pygame.time.Clock()
  running = True

  # Initialize Chess Board
  board = Board()
  pprint(board._pieces)

  while running:
    for event in pygame.event.get():
      if event.type ==  pygame.QUIT:
        running = False
    
    screen.fill('beige')
    pygame.display.flip()
    clock.tick(60)

  pygame.quit()


if __name__ == '__main__':
  run_chess()
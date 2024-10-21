from typing import override
import pygame
from enum import StrEnum, auto

class Color(StrEnum):
  WHITE = auto()
  BLACK = auto()
  
class Rank(StrEnum):
  KING   = auto()
  QUEEN  = auto()
  ROOK   = auto()
  BISHOP = auto()
  KNIGHT = auto()
  PAWN   = auto()

class Piece(pygame.sprite.Sprite):

  @override
  def __init__(self, rank: str, color: str, scale: float = 1, *groups):
    super().__init__(*groups)
    assert rank in Rank, f'invalid piece type {rank}'
    assert color in Color, f'invalid color {color}'
    self._type = rank
    self._color = color
    img = pygame.image.load(f'assets/{self.type}_{self.color}.png').convert_alpha()
    self.image = pygame.transform.scale_by(img, scale)
    self.rect = self.image.get_rect()
  
  @property
  def type(self):
    return self._type
  
  @property
  def color(self):
    return self._color

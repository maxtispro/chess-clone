from typing import override
from pygame import Rect
from src.notation import Position, code_2_pos, pos_2_code
from enum import StrEnum, auto
import pygame.image as image
from pygame.sprite import Sprite

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

class Piece(Sprite):

  @override
  def __init__(self, piece_type: str, color: str, *groups):
    super().__init__(*groups)
    assert piece_type in Rank, f'invalid piece type {piece_type}'
    assert color in Color, f'invalid color {color}'
    self._type = piece_type
    self._color = color
    self.image = image.load(f'assets/{self.type}_{self.color}.png').convert_alpha()
    self.rect = self.image.get_rect()
  
  @property
  def type(self):
    return self._type
  
  @property
  def color(self):
    return self._color

from typing import override
import pygame
from src.piece import *

class Board(pygame.sprite.Sprite):

  @override
  def __init__(self, first: str, width = 1104, *groups):
    super().__init__(*groups)
    assert first in Color, 'invalid board starting color'
    second = Color.BLACK if first == Color.WHITE else Color.WHITE
    self.scale = width / 1104
    self.sqaure_size = 128 * self.scale
    self.border_size = 40 * self.scale
    self.size = self.sqaure_size * 8 + self.border_size * 2
    img = pygame.image.load(f'assets/board_{first}.png').convert()
    self.image = pygame.transform.scale(img, (width, width))
    self.rect = self.image.get_rect()
    self.rect.x = 0
    self.rect.y = 0

    self._grid: dict[str, Piece] = {}

    # First pieces
    self.place(Rank.ROOK,   first, 'a1')
    self.place(Rank.KNIGHT, first, 'b1')
    self.place(Rank.BISHOP, first, 'c1')
    self.place(Rank.QUEEN,  first, 'd1' if first == Color.WHITE else 'e1')
    self.place(Rank.KING,   first, 'e1' if first == Color.WHITE else 'd1')
    self.place(Rank.BISHOP, first, 'f1')
    self.place(Rank.KNIGHT, first, 'g1')
    self.place(Rank.ROOK,   first, 'h1')
    self.place(Rank.PAWN,   first, 'a2')
    self.place(Rank.PAWN,   first, 'b2')
    self.place(Rank.PAWN,   first, 'c2')
    self.place(Rank.PAWN,   first, 'd2')
    self.place(Rank.PAWN,   first, 'e2')
    self.place(Rank.PAWN,   first, 'f2')
    self.place(Rank.PAWN,   first, 'g2')
    self.place(Rank.PAWN,   first, 'h2')

    # Second pieces
    self.place(Rank.ROOK,   second, 'a8')
    self.place(Rank.KNIGHT, second, 'b8')
    self.place(Rank.BISHOP, second, 'c8')
    self.place(Rank.QUEEN,  second, 'd8' if second == Color.BLACK else 'e8')
    self.place(Rank.KING,   second, 'e8' if second == Color.BLACK else 'd8')
    self.place(Rank.BISHOP, second, 'f8')
    self.place(Rank.KNIGHT, second, 'g8')
    self.place(Rank.ROOK,   second, 'h8')
    self.place(Rank.PAWN,   second, 'a7')
    self.place(Rank.PAWN,   second, 'b7')
    self.place(Rank.PAWN,   second, 'c7')
    self.place(Rank.PAWN,   second, 'd7')
    self.place(Rank.PAWN,   second, 'e7')
    self.place(Rank.PAWN,   second, 'f7')
    self.place(Rank.PAWN,   second, 'g7')
    self.place(Rank.PAWN,   second, 'h7')
  
  def _validate_pos(self, pos: str) -> str:
    pos = pos.lower()
    assert len(pos) == 2 and ord('a') <= ord(pos[0]) <= ord('h') and ord('1') <= ord(pos[1]) <= ord('8')
    return pos
  
  def _coords_on_board(self, pos: str) -> tuple[int, int]:
    pos = self._validate_pos(pos)
    x = (ord(pos[0]) - ord('a')) * self.sqaure_size + self.border_size
    y = self.size - (ord(pos[1]) - ord('0')) * self.sqaure_size - self.border_size
    return (x, y)
  
  def place(self, rank: str, color: str, pos: str):
    pos = self._validate_pos(pos)
    piece = Piece(rank, color, self.scale, *self.groups())
    coords = self._coords_on_board(pos)
    piece.rect.x = coords[0] + (self.sqaure_size - piece.rect.width)/2
    piece.rect.y = coords[1] + (self.sqaure_size-piece.rect.height)/2
    self._grid[pos] = piece
  
  def get(self, pos: str) -> Piece:
    pos = self._validate_pos(pos)
    return self._grid[pos]
  
  def move(self, piece: Piece, pos: str):
    pos = self._validate_pos(pos)
    coords = self._coords_on_board(pos)
    piece.rect.x = coords[0] + (self.sqaure_size - piece.rect.width)/2
    piece.rect.y = coords[1] + (self.sqaure_size-piece.rect.height)/2
  
  def capture(self, pos: str):
    pos = self._validate_pos(pos)
    self._grid[pos] = None
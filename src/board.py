from typing import override
import pygame
from src.piece import *

class Board(pygame.sprite.Sprite):

  @override
  def __init__(self, first: str, width = 1104, *groups):
    super().__init__(*groups)
    assert first in Color, 'invalid board starting color'
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

    # White pieces
    self.place(Rank.ROOK,   Color.WHITE, 'a1')
    self.place(Rank.KNIGHT, Color.WHITE, 'b1')
    self.place(Rank.BISHOP, Color.WHITE, 'c1')
    self.place(Rank.QUEEN,  Color.WHITE, 'd1')
    self.place(Rank.KING,   Color.WHITE, 'e1')
    self.place(Rank.BISHOP, Color.WHITE, 'f1')
    self.place(Rank.KNIGHT, Color.WHITE, 'g1')
    self.place(Rank.ROOK,   Color.WHITE, 'h1')
    self.place(Rank.PAWN,   Color.WHITE, 'a2')
    self.place(Rank.PAWN,   Color.WHITE, 'b2')
    self.place(Rank.PAWN,   Color.WHITE, 'c2')
    self.place(Rank.PAWN,   Color.WHITE, 'd2')
    self.place(Rank.PAWN,   Color.WHITE, 'e2')
    self.place(Rank.PAWN,   Color.WHITE, 'f2')
    self.place(Rank.PAWN,   Color.WHITE, 'g2')
    self.place(Rank.PAWN,   Color.WHITE, 'h2')

    # Black pieces
    self.place(Rank.ROOK,   Color.BLACK, 'a8')
    self.place(Rank.KNIGHT, Color.BLACK, 'b8')
    self.place(Rank.BISHOP, Color.BLACK, 'c8')
    self.place(Rank.QUEEN,  Color.BLACK, 'd8')
    self.place(Rank.KING,   Color.BLACK, 'e8')
    self.place(Rank.BISHOP, Color.BLACK, 'f8')
    self.place(Rank.KNIGHT, Color.BLACK, 'g8')
    self.place(Rank.ROOK,   Color.BLACK, 'h8')
    self.place(Rank.PAWN,   Color.BLACK, 'a7')
    self.place(Rank.PAWN,   Color.BLACK, 'b7')
    self.place(Rank.PAWN,   Color.BLACK, 'c7')
    self.place(Rank.PAWN,   Color.BLACK, 'd7')
    self.place(Rank.PAWN,   Color.BLACK, 'e7')
    self.place(Rank.PAWN,   Color.BLACK, 'f7')
    self.place(Rank.PAWN,   Color.BLACK, 'g7')
    self.place(Rank.PAWN,   Color.BLACK, 'h7')
  
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
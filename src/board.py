from typing import override
import pygame
from src.notation import code_2_pos
from src.piece import *
import pygame.image as image
from pygame.sprite import Sprite

class Board(pygame.sprite.Sprite):

  @override
  def __init__(self, first: str, width = 1104, *groups):
    super().__init__(*groups)
    assert first in Color, 'invalid board starting color'
    self.scale = width / 1104
    self.sqaure_size = 128 * self.scale
    self.border_size = 40 * self.scale
    self.size = self.sqaure_size * 8 + self.border_size * 2
    img = image.load(f'assets/board_{first}.png').convert()
    self.image = pygame.transform.scale(img, (width, width))
    self.rect = self.image.get_rect()
    self.rect.x = 0
    self.rect.y = 0

    self._pieces: list[tuple[Piece, str]] = [

      # White pieces
      (Piece(Rank.ROOK,   Color.WHITE, *groups), 'a1'),
      (Piece(Rank.KNIGHT, Color.WHITE, *groups), 'b1'),
      (Piece(Rank.BISHOP, Color.WHITE, *groups), 'c1'),
      (Piece(Rank.QUEEN,  Color.WHITE, *groups), 'd1'),
      (Piece(Rank.KING,   Color.WHITE, *groups), 'e1'),
      (Piece(Rank.BISHOP, Color.WHITE, *groups), 'f1'),
      (Piece(Rank.KNIGHT, Color.WHITE, *groups), 'g1'),
      (Piece(Rank.ROOK,   Color.WHITE, *groups), 'h1'),
      (Piece(Rank.PAWN,   Color.WHITE, *groups), 'a2'),
      (Piece(Rank.PAWN,   Color.WHITE, *groups), 'b2'),
      (Piece(Rank.PAWN,   Color.WHITE, *groups), 'c2'),
      (Piece(Rank.PAWN,   Color.WHITE, *groups), 'd2'),
      (Piece(Rank.PAWN,   Color.WHITE, *groups), 'e2'),
      (Piece(Rank.PAWN,   Color.WHITE, *groups), 'f2'),
      (Piece(Rank.PAWN,   Color.WHITE, *groups), 'g2'),
      (Piece(Rank.PAWN,   Color.WHITE, *groups), 'h2'),

      # Black pieces
      (Piece(Rank.ROOK,   Color.BLACK, *groups), 'a8'),
      (Piece(Rank.KNIGHT, Color.BLACK, *groups), 'b8'),
      (Piece(Rank.BISHOP, Color.BLACK, *groups), 'c8'),
      (Piece(Rank.QUEEN,  Color.BLACK, *groups), 'd8'),
      (Piece(Rank.KING,   Color.BLACK, *groups), 'e8'),
      (Piece(Rank.BISHOP, Color.BLACK, *groups), 'f8'),
      (Piece(Rank.KNIGHT, Color.BLACK, *groups), 'g8'),
      (Piece(Rank.ROOK,   Color.BLACK, *groups), 'h8'),
      (Piece(Rank.PAWN,   Color.BLACK, *groups), 'a7'),
      (Piece(Rank.PAWN,   Color.BLACK, *groups), 'b7'),
      (Piece(Rank.PAWN,   Color.BLACK, *groups), 'c7'),
      (Piece(Rank.PAWN,   Color.BLACK, *groups), 'd7'),
      (Piece(Rank.PAWN,   Color.BLACK, *groups), 'e7'),
      (Piece(Rank.PAWN,   Color.BLACK, *groups), 'f7'),
      (Piece(Rank.PAWN,   Color.BLACK, *groups), 'g7'),
      (Piece(Rank.PAWN,   Color.BLACK, *groups), 'h7'),
    ]

    for piece, pos in self._pieces:
      piece.image = pygame.transform.scale_by(piece.image, self.scale)
      piece.rect = piece.image.get_rect()
      self.move_piece(piece, pos)
  
  def move_piece(self, piece: Piece, pos: str):
    pos = pos.lower()
    assert len(pos) == 2 and ord('a') <= ord(pos[0]) <= ord('h') and ord('1') <= ord(pos[1]) <= ord('8')
    piece.rect.x = (ord(pos[0]) - ord('a')) * self.sqaure_size + self.border_size + (self.sqaure_size - piece.rect.width)/2
    piece.rect.y = self.size - (ord(pos[1]) - ord('0')) * self.sqaure_size - self.border_size + (self.sqaure_size-piece.rect.height)/2
  
  @override
  def add(self, *groups):
    super().add(*groups)
    for piece, _ in self._pieces:
      piece.add(*groups)
  
  @override
  def remove(self, *groups) -> None:
    super().remove(*groups)
    for piece, _ in self._pieces:
      piece.remove(*groups)
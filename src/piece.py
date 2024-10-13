from src.notation import Position, pos_2_code
from enum import Enum
from typing import override


Color = Enum('Color', ['WHITE', 'BLACK'])


class Piece:
  def __init__(self, color: int, position: Position):
    assert(color == Color.WHITE or color == Color.BLACK)
    self._color = color
    self._position = (0, 0)
    self.position = position
    self._update_valid_pos()

  def is_pos_on_board(self, pos: Position):
    if len(pos) == 2 and 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
      return True
    return False
  
  @property
  def position(self):
    return self._position
  
  @position.setter
  def position(self, pos: Position):
    if self.is_pos_on_board(pos):
      self._position = pos
    else:
      print(f'Trying to set invalid position: {pos}')
  
  @property
  def color(self):
    return self._color
  
  def _update_valid_pos(self):
    '''Override this method in child classes'''
    self.valid_positions: list[Position] = []
  
  def move(self, pos: Position):
    if pos in self.valid_positions:
      self.position = pos
  
  def __repr__(self) -> str:
    return '{ color: ' + ('white' if self.color == Color.WHITE else 'black')\
      + ', position: ' + pos_2_code(self.position) + ' }'


class King(Piece):
  @override
  def _update_valid_pos(self):
    self.valid_positions = [(i, j) for j in range(self.position[0]-1, self.position[0]+2)
                 for i in range(self.position[1]-1, self.position[1]+2) if self.is_pos_on_board((i, j))]
  
  @override
  def __repr__(self) -> str:
    old = super().__repr__()
    return old[:2] + 'King, ' + old[2:]


class Queen(King):
  @override
  def _update_valid_pos(self):
    super()._update_valid_pos()
    for i in range(2, 8):
      x = i + self.position[0]
      y = i + self.position[1]
      if self.is_pos_on_board((x, y)):
        self.valid_positions.append((x, y))
  
  @override
  def __repr__(self) -> str:
    old = super().__repr__()
    return old[:2] + 'Queen, ' + old[8:]


class Bishop(Piece):
  @override
  def _update_valid_pos(self):
    return super()._update_valid_pos()

  @override
  def __repr__(self) -> str:
    old = super().__repr__()
    return old[:2] + 'Bishop, ' + old[2:]


class Knight(Piece):
  @override
  def _update_valid_pos(self):
    return super()._update_valid_pos()
  
  @override
  def __repr__(self) -> str:
    old = super().__repr__()
    return old[:2] + 'Knight, ' + old[2:]


class Rook(Piece):
  @override
  def _update_valid_pos(self):
    return super()._update_valid_pos()
  
  @override
  def __repr__(self) -> str:
    old = super().__repr__()
    return old[:2] + 'Rook, ' + old[2:]


class Pawn(Piece):
  @override
  def _update_valid_pos(self):
    return super()._update_valid_pos()
  
  @override
  def __repr__(self) -> str:
    old = super().__repr__()
    return old[:2] + 'Pawn, ' + old[2:]
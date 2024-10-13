from src.notation import code_2_pos
from src.piece import *

class Board:
  def __init__(self):
    self._pieces: list[Piece] = [

      # White pieces
      King  (Color.WHITE, code_2_pos('e1')),
      Queen (Color.WHITE, code_2_pos('d1')),
      Bishop(Color.WHITE, code_2_pos('c1')),
      Bishop(Color.WHITE, code_2_pos('f1')),
      Knight(Color.WHITE, code_2_pos('b1')),
      Knight(Color.WHITE, code_2_pos('g1')),
      Rook  (Color.WHITE, code_2_pos('a1')),
      Rook  (Color.WHITE, code_2_pos('h1')),
      Pawn  (Color.WHITE, code_2_pos('a2')),
      Pawn  (Color.WHITE, code_2_pos('b2')),
      Pawn  (Color.WHITE, code_2_pos('c2')),
      Pawn  (Color.WHITE, code_2_pos('d2')),
      Pawn  (Color.WHITE, code_2_pos('e2')),
      Pawn  (Color.WHITE, code_2_pos('f2')),
      Pawn  (Color.WHITE, code_2_pos('g2')),
      Pawn  (Color.WHITE, code_2_pos('h2')),

      # Black pieces
      King  (Color.BLACK, code_2_pos('e8')),
      Queen (Color.BLACK, code_2_pos('d8')),
      Bishop(Color.BLACK, code_2_pos('c8')),
      Bishop(Color.BLACK, code_2_pos('f8')),
      Knight(Color.BLACK, code_2_pos('b8')),
      Knight(Color.BLACK, code_2_pos('g8')),
      Rook  (Color.BLACK, code_2_pos('a8')),
      Rook  (Color.BLACK, code_2_pos('h8')),
      Pawn  (Color.BLACK, code_2_pos('a7')),
      Pawn  (Color.BLACK, code_2_pos('b7')),
      Pawn  (Color.BLACK, code_2_pos('c7')),
      Pawn  (Color.BLACK, code_2_pos('d7')),
      Pawn  (Color.BLACK, code_2_pos('e7')),
      Pawn  (Color.BLACK, code_2_pos('f7')),
      Pawn  (Color.BLACK, code_2_pos('g7')),
      Pawn  (Color.BLACK, code_2_pos('h7')),
    ]
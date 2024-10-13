Position = tuple[int, int]

def code_2_pos(code: str) -> Position:
  assert(len(code) == 2)
  code = code.lower()
  x = ord(code[0]) - 97
  y = ord(code[1]) - 49
  assert(0 <= x < 8 and 0 <= y < 8)
  return (x, y)

def pos_2_code(pos: Position) -> str:
  assert(0 <= pos[0] < 8 and 0 <= pos[1] < 8)
  return chr(pos[0] + 97) + chr(pos[1] + 49)

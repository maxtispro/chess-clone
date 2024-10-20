from PIL import Image, ImageDraw, ImageFont

WHITE_FILE = 'assets/board_white.png'
BLACK_FILE = 'assets/board_black.png'

BROWN = (160, 133, 91)
CREAM = (241, 214, 171)

SQUARE_SIZE = 128
BORDER_SIZE = 40
BOARD_SIZE = SQUARE_SIZE * 8 + BORDER_SIZE * 2


if __name__ == '__main__':
  font = ImageFont.truetype('assets/Acme-Regular.ttf', 36)
  white_img = Image.new('RGB', (BOARD_SIZE, BOARD_SIZE), CREAM)
  white_draw = ImageDraw.Draw(white_img)
  for i in range(64):
    x = (i % 8) * SQUARE_SIZE + BORDER_SIZE
    y = (i // 8) * SQUARE_SIZE + BORDER_SIZE
    white_draw.rectangle([x, y, x + SQUARE_SIZE, y + SQUARE_SIZE], BROWN if (i + i//8) % 2 == 1 else CREAM)
  black_img = white_img.copy()
  black_draw = ImageDraw.Draw(black_img)
  for i in range(8):
    j = i * SQUARE_SIZE + BORDER_SIZE + SQUARE_SIZE/2
    white_draw.text((BORDER_SIZE/2, j), f'{8-i}', BROWN, font, anchor='mm')
    white_draw.text((BOARD_SIZE - BORDER_SIZE/2, j), f'{8-i}', BROWN, font, anchor='mm')
    white_draw.text((j, BORDER_SIZE/2), f'{chr(i + 65)}', BROWN, font, anchor='mm')
    white_draw.text((j, BOARD_SIZE - BORDER_SIZE/2), f'{chr(i + 65)}', BROWN, font, anchor='mm')
    black_draw.text((BORDER_SIZE/2, j), f'{i+1}', BROWN, font, anchor='mm')
    black_draw.text((BOARD_SIZE - BORDER_SIZE/2, j), f'{i+1}', BROWN, font, anchor='mm')
    black_draw.text((j, BORDER_SIZE/2), f'{chr(7-i + 65)}', BROWN, font, anchor='mm')
    black_draw.text((j, BOARD_SIZE - BORDER_SIZE/2), f'{chr(7-i + 65)}', BROWN, font, anchor='mm')
  white_img.save(WHITE_FILE)
  black_img.save(BLACK_FILE)
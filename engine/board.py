from pygame import Rect, draw, Surface, Font, font
from ..utils.utilities import getFontPath

OFFSET = 15 # for the board's border

def _isWhite(x, y) -> bool:
    return (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1)

# function to draw each individual squares
def _drawSquare(col, board, square, squareSize, color):
    square.left = (col * squareSize) + OFFSET
    draw.rect(board, color, square)

# function to draw the board, aside the ranks and files
def _drawBoard(squareSize, board, colors: dict, fonts: Font):
    square = Rect(OFFSET, OFFSET, squareSize, squareSize)

    for row in range(8):
        if row >= 1: square.bottom = ( (row + 1) * squareSize ) + OFFSET # go to next row
    
        for col in range(8):
            if _isWhite(row, col):
                _drawSquare(col, board, square, squareSize, colors['white'])
            else:
                _drawSquare(col, board, square, squareSize, colors['black'])
                
            _drawRanks(row, board, squareSize, fonts, colors['font'])
            _drawFiles(board, squareSize, fonts, colors['font'])
    
# function to draw ranks (1, 2, 3, 4, 5, 6, 7, 8)
def _drawRanks(row, board : Surface, squareSize, font : Font, color):
    boardSize = board.get_width()
    xPos = boardSize - (OFFSET - 5)
    yPos = OFFSET + ((row + .4) * squareSize) 
    text = str(8 - row)

    rank = font.render(text, False, color)
    rankPos = rank.get_rect(x = xPos, y = yPos)
    board.blit(rank, rankPos)

# function to draw ranks (a, b, c, d, e, f, g, h, i)
def _drawFiles(board : Surface, squareSize, font : Font, color):
    boardSize = board.get_height()
    text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    for col in range(8):
        xPos = OFFSET + ((col + .5) * squareSize)
        yPos = boardSize - (OFFSET)

        file = font.render(text[col], True, color)
        filePos = file.get_rect(x = xPos, y = yPos)
        board.blit(file, filePos)

# the function to be called in the game
def boardSurface(squareSize = 30) -> Surface:
    colors = {
        "background" : (38, 37, 34),
        "black" : (0, 0, 0),
        "white": (255, 255, 255),
        "font" : (255, 255, 255)
    }
    
    boardSize = ( squareSize * 8 ) + (OFFSET * 2)
    board = Surface((boardSize, boardSize)).convert()
    board.fill(colors["background"])

    fontPath = getFontPath("AGENCYR.ttf")
    fonts = font.Font(fontPath, 13)
    
    _drawBoard(squareSize, board, colors, fonts)
        
    return board
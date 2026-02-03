from pygame import Rect, draw, Surface, Font, font

OFFSET = 15 # for the board's border

# function to draw each individual squares
def _drawSquare(col, board, square, squareSize, color):
    square.left = (col * squareSize) + OFFSET
    draw.rect(board, color, square)

# function to draw the board, aside the ranks and files
def _drawBoard(row, squareSize, board, colors: dict):
    square = Rect(OFFSET, OFFSET, squareSize, squareSize)

    if row >= 1: square.bottom = ( (row + 1) * squareSize ) + OFFSET # go to next row
    
    for col in range(8):
        if(row == 0 or row % 2 == 0) and col % 2 == 0:
            _drawSquare(col, board, square, squareSize, colors['white'])
        elif(row == 1 or row % 2 == 1) and col % 2 == 1:
            _drawSquare(col, board, square, squareSize, colors['white'])

        if(row == 0 or row % 2 == 0) and col % 2 == 1:
            _drawSquare(col, board, square, squareSize, colors['black'])
        elif(row == 1 or row % 2 == 1) and col % 2 == 0:
            _drawSquare(col, board, square, squareSize, colors['black'])
    
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

    fonts = font.Font("assets/AGENCYR.ttf", 13)
    
    for row in range(8):
        _drawBoard(row, squareSize, board, colors)
        _drawRanks(row, board, squareSize, fonts, colors['font'])
        _drawFiles(board, squareSize, fonts, colors['font'])
        
    return board
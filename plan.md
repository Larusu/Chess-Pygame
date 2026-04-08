# chess-pygame-plan

## Plan:
### `pieces/`
- This is where I'll put all the move logics for piece class
- The white and black is not here
- **Abstract Base Class (ABC)** - Have an interface methods for all the pieces `moves`, `available_moves`, `available_takes`
- Special piece:
	- Pawn: `promotion`, `en_passant`
	- King: `castling`

### `engine/`
- Turn management (whose turn is it?)
- Move validation (is this move legal _right now_?)
- Special rule enforcement (check, checkmate, stalemate)
- Board state (where is every piece?)
#### `board.py`
- this should handle the data structures
- We will FEN / Forsyth-Edwards Notations
1. Piece Placement
	- lowercase for black : prnbqk
	- UPPERCASE for white : PRNBQK
	- empty squares are denoted by numbers 1-8
	- Starting piece looks like : =="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"==
2. Active Color
	- who moves next
	- always in lowercase : w if white turn or b for black
	- exampls : =="8/8/8/4p1K1/2k1P3/8/8/8 b"== (black's turn)
3. Castling Rights
	- can castle and what side
	- Uppercase for white first, means available to castle
	- then lowercase for black
	- k: kingside castle, q: queenside castle. -: neither can castle
	- example: =="4k2r/6r1/8/8/8/8/3R4/R3K3 w Qk"== 
		- *white can castle queen side, while black can castle kingside*
	- example: =="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq"==
		- *both can castle on kingside and queenside*
4. Possible En Passant targets
	- if pawn moves 2 squares is possible en passant capture
	- if can en passant capture: use algebraic notation (e4, f4, c5, f5)
	- if cannot: the symbol used is `-`
	- example: =="rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3"==
5. Half-move Clock
	- how many moves player has made since the last pawn advance or piece capture
	- this is for the **50-move draw rule**
	- if counter reach 100 (means both players reached 50 moves), the game ends in a draw
	- example: =="8/5k2/3p4/1p1Pp2p/pP2Pp1P/P4P1K/8/8 b - - 99"==
		- *The fifth field of this string tells us that this game ends in a draw on the next move.*
6. Full-move Number
	- last field is to count the move of both player
	- it is ONLY INCREMENTED if black moves
	- example: =="5k2/ppp5/4P3/3R3p/6P1/1K2Nr2/PP3P2/8 b - - 1 32"==
#### `rules.py`
- This is where all the rule happens
- `checkmate`, `stalemate`, `is_in_check`

### `gui/` 
- The graphical interface that will show the player
- The game loop
- Event handling: mouse click and drag-and-drop
#### `board_view.py`
- Draw the board and pieces 
- reads the FEN Notation and show it to the graphical interface
#### `config.py`
-  all the configurations for the game
- `BOARD_SIZE`, `SQUARE_SIZE`, `BOARD_COLORS`, `BACKGROUND_COLOR`

## Pieces Movement

### Pawn - P
Equation: (x, y ± 1 || 2)
- If white: (x, y + 1) or (x, y + 2)
- If black: (x, y - 1) or (x, y - 2)
Condition: (1 <= x <= 8,  1 <= y <= 8)
### Rook - R
![[how-rook-move.png]]
Equation: (x, y ± n) and (x ± n, y)
- Top:    (x, y + n)
- Right:  (x + n, y)
- Bottom: (x, y - n)
- Left:   (x - n, y)
Condition: (1 <= x <= 8,  1 <= y <= 8)
### Bishop - B
![[how-bishop-move.png]]
Equation: (x ± n, y ± n)
- Top-right: (x + n, y + n)
- Top-left:  (x - n, y + n)
- Bot-right: (x + n, y - n)
- Bot-left:  (x - n, y - n)
Condition: (1 <= x <= 8,  1 <= y <= 8)
### Knight - N
![[how-knight-move.png]]
Equation: (x ± 2, y ± 1), (x ± 1, y ± 2)
- Top-right:  (x + 1, y + 2)
- Top-left:   (x - 1, y + 2)
- Right-up:   (x + 2, y + 1)
- Right-down: (x + 2, y - 1)
- Bot-right:  (x + 1, y - 2)
- Bot-left:   (x - 1, y - 2)
- Left-up:    (x - 2, y + 1)
- Left-down:  (x - 2, y - 1)
Condition: (1 <= x <= 8,  1 <= y <= 8)
### Queen - Q
Same as Rook and Bishop

## File Structure

```
chess/
├── assets/              # all the images and fonts for the game
├── config/              # configurations
├── engine/              # core logic (no gui)
│   ├── __init__.py
│   ├── board.py         # handles data structure of the board
│   ├── game_state.py    # game state, turn management
│   └── rules.py         # check, checkmate, stalemate logic
├── gui/
│   ├── __init__.py
│   ├── board_view.py    # board drawing and pieces
│   └── game.py          # game loop, event handling
├── pieces/
│   ├── __init__.py
│   ├── piece.py         # abstract base class
│   ├── pawn.py
│   ├── rook.py
│   ├── knight.py
│   ├── bishop.py
│   ├── queen.py
│   └── king.py
├── utils/
│   ├── __init__.py
│   └── utilities.py
└── __main__.py
```
****
## Phase 1 — Foundation & Cleanup
- [x] Rename all functions/variables to snake_case
- [x] Restructure folders (create pieces/ folder)
- [x] Create abstract Piece base class with shared interface
- [x] Separate board drawing from board state
- [x] Create config for game constants (BOARD_SIZE, SQUARE_SIZE, colors, etc.)
Finished at 4/7/2026;02:38

## Phase 2 — Piece Rendering
- [x] Load and display all piece images on the board
- [x] Map board squares to pixel coordinates
- [x] Place all pieces in their starting positions
Finished at 4/9/2026;02:45
## Phase 3 — Mouse Input & Selection
- [ ] Detect which square the user clicks
- [ ] Highlight the selected piece
- [ ] Show available moves for the selected piece

## Phase 4 — Movement
- [ ] Implement basic move logic per piece
- [ ] Move a piece from one square to another
- [ ] Implement capture logic
- [ ] Implement turn system (white → black → white)

## Phase 5 — Special Rules
- [ ] Pawn: en passant, promotion
- [ ] King & Rook: castling
- [ ] Check detection
- [ ] Checkmate & stalemate detection

## Phase 6 — Polish
- [ ] Move history / notation
- [ ] UI improvements
- [ ] Sound effects (optional)

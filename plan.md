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
- Where are the pieces?
#### `rules.py`
- This is where all the rule happens
- `checkmate`, `stalemate`, `is_in_check`

### `gui/` 
- Draw the board and pieces 
- The game loop
- Event handling: mouse click and drag-and-drop
#### `config.py`
-  all the configurations for the game
- `BOARD_SIZE`, `SQUARE_SIZE`, `BOARD_COLORS`, `BACKGROUND_COLOR`

## Pieces Movement

### Pawn
Equation: (x, y ± 1 || 2)
- If white: (x, y + 1) or (x, y + 2)
- If black: (x, y - 1) or (x, y - 2)
Condition: (1 <= x <= 8,  1 <= y <= 8)
### Rook
![[how-rook-move.png]]
Equation: (x, y ± n) and (x ± n, y)
- Top:    (x, y + n)
- Right:  (x + n, y)
- Bottom: (x, y - n)
- Left:   (x - n, y)
Condition: (1 <= x <= 8,  1 <= y <= 8)
### Bishop
![[how-bishop-move.png]]
Equation: (x ± n, y ± n)
- Top-right: (x + n, y + n)
- Top-left:  (x - n, y + n)
- Bot-right: (x + n, y - n)
- Bot-left:  (x - n, y - n)
Condition: (1 <= x <= 8,  1 <= y <= 8)
### Knight
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
### Queen
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
- [ ] Load and display all piece images on the board
- [ ] Map board squares to pixel coordinates
- [ ] Place all pieces in their starting positions

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

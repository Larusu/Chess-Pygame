# =========================
# Board Dimensions
# =========================

SQUARE_SIZE = 60
OFFSET = 15

BOARD_SIZE = (SQUARE_SIZE * 8) + (OFFSET * 2)

# =========================
# Screen Settings
# =========================

BACKGROUND_COLOR = (49, 46, 43)

# =========================
# Board Colors
# =========================

BOARD_COLORS = {
    "background": (49, 46, 43),
    "black": (118,150,86),
    "white": (238,238,210),
    "selected": (255,255,0,80),  # for left click
    "annotation": (255,0,0,100), # for right click
    "circles": (192,192,192,80), # for the possibles moves
    "font": (255, 255, 255),
}

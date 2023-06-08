print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP21, board.GP22, board.GP4, board.GP2, board.GP1) # Cols
keyboard.row_pins = (board.GP0, board.GP5, board.GP11, board.GP16, board.GP15) # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())

# cleaner non-keys
_______ = KC.TRNS
FN      = KC.MO(1)

# Keymap
keyboard.keymap = [
    [ # base layer
        KC.F14,   KC.NLCK, KC.PSLS,  KC.PAST,  KC.PMNS,
        KC.F15,   KC.N7,   KC.N8,    KC.N9,    KC.PPLS,
        KC.F16,   KC.N4,   KC.N5,    KC.N6,    _______,
        KC.F17,   KC.N1,   KC.N2,    KC.N3,    KC.PENT,
        FN,   KC.N0,   _______,  KC.PDOT,  _______,
    ],
    [ # fn layer
        KC.A,     _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,
    ],
    [ # extra blank layer
        _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,
    ] nb
]

if __name__ == '__main__':
    keyboard.go()

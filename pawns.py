class Pawn:
    def __init__(self, pos, player, active):
        self.pos = pos
        self.player = player
        self.active = active

pawns = [
    Pawn((455, 460), 1, False),
    Pawn((455, 350), 1, False),
    Pawn((350, 350), 1, False),
    Pawn((350, 460), 1, False),
    Pawn((200, 210), 2, False),
    Pawn((200, 100), 2, False),
    Pawn((95, 100), 2, False),
    Pawn((95, 210), 2, False),
    Pawn((200, 460), 3, False),
    Pawn((200, 350), 3, False),
    Pawn((95, 350), 3, False),
    Pawn((95, 460), 3, False),
    Pawn((455, 210), 4, False),
    Pawn((455, 100), 4, False),
    Pawn((350, 100), 4, False),
    Pawn((350, 210), 4, False),
]


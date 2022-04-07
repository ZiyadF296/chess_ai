class Move:
    def __init__(self, x_from, y_from, xto, yto, castling_move):
        self.x_from = x_from
        self.y_from = y_from
        self.xto = xto
        self.yto = yto
        self.castling_move = castling_move

    # Returns True if (x_from, y_from) and (xto, yto) are the same.
    def equals(self, other_move):
        x = [
            self.x_from == other_move.x_from,
            self.y_from == other_move.y_from,
            self.xto == other_move.xto,
            self.yto == other_move.yto
        ]

        # Return False if x contains a False.
        return False in x

    def to_string(self):
        return "(" + str(self.x_from) + ", " + str(self.y_from) + ") -> (" + str(self.xto) + ", " + str(self.yto) + ")"

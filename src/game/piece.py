
class Color:
    WHITE = 0x1
    BLACK = 0x2
    TEAMS = 0x3

    def __new__(self, args):
        if args.lower() in 'white':
            return self.WHITE
        elif args.lower() in 'black':
            return self.BLACK
        return self.TEAMS

    @classmethod
    def set(self, bits, color):
        return (bits | self.TEAMS) ^ self.TEAMS | color

    @classmethod
    def get(self, bits):
        return bits & self.TEAMS



class Piece:
    PAWN = 0x4
    KNIGHT = 0x8
    BISHOP = 0x10
    ROOK = 0x20
    QUEEN = 0x40
    KING = 0x80
    PIECES = 0xfc

    def __new__(self, args):
        args = args.lower()
        if args in 'pawn':
            return self.PAWN
        if args in ('n', 'knight'):
            return self.KNIGHT
        if args in 'bishop':
            return self.BISHOP
        if args in 'rook':
            return self.ROOK
        if args in 'queen':
            return self.QUEEN
        if args in 'king':
            return self.KING
        return self.PIECES

    @classmethod
    def set(self, bits, piece):
        return (bits | self.PIECES) ^ self.TEAMS | piece

    @classmethod
    def get(self, bits):
        return bits & self.PIECES


class Type:
    def __init__(self, args):
        return Piece(args) | Color('wb'[args.lower()==args])

    @classmethod
    def set(self, bits, type):
        return Color.set(bits, type) | Piece.set(bits, type)

    @classmethod
    def get(self, bits):
        return bits & (Color.TEAMS | Piece.PIECES)

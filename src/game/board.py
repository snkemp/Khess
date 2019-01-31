
from src.game.squares import Cell
from src.game.notation import Notation

class Board:

    def __init__(self):
        self.reset()


    def __getitem__(self, sq):
        return Cell.first(self._board & sq)

    def __setitem__(self, sq, bits):
        self._board |= sq
        self._board ^= sq
        self._board |= bits


    def reset(self, fen='rnbqknbr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKNBR w - 1 1'):
        self._notation = Notation(fen)

        self._board,
        self._turn,
        self._castle,
        self._enpassant,
        self._halfmove,
        self._fullmove = self.notation.fen_values

    def move(self, move):

        args = self._notation.move(move)



    def __repr__(self):

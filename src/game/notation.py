
from itertools import zip_longest

import re


from src.game.errors import IllegalNotation, IllegalFEN, IllegalPGN

class Notation:

    def __init__(self, fen, moves=[], **tags):
        if not re.match(
            '[pnbrqk1-8]{1,8}(/[pnbrqk1-8]{1,8}){7} [wb] [KQkq-]{,4} (-|[a-h][1-8]) \d+ \d+',
            fen):
            raise IllegalFEN(fen)

        self.fen = fen
        self.moves = moves
        self.tags = tags

    def fromPGN(self, pgn):

        if not re.match(
            '(?m:\s|(\[.*?\])|\{.*?\}|;.*?\n|\d+\. [PNBRQKa-h1-8xX\+\#\?\!]+ [PNBRQKa-h1-8xX\+\#\?\!]+)*',
            pgn):
            raise IllegalPGN(pgn)

        tags = {}
        for arg in re.findall('[.*?]', pgn):
            k, v = re.split('\s+', arg[1:-1])
            tags[k] = v[1:-1]


        annotations = re.findall('{.*?}|;.*\n', pgn)
        tags['Annotations'] = annotations




    @property
    def fen_values(self):
        board, turn, castle, ep, hm, fm = self.fen.split(' ')

        _turn = Color(turn)
        _castle = Castle(castle)
        _ep = Square(ep)
        _hm = int(hm)
        _fm = int(fm)

        _board = 0x0
        board = ''.join([ str(r) for r in map(reversed, board.split('/')) ])
        for p in board:
            if p in '12345678':
                board = Cell.shift(board, int(p))
            else:
                board = Cell.shift(board, 1)
                board |= Type(p)


        return _board, _turn, _castle, _ep, _hm, _fm


    @property
    def pgn_values(self):

        _desc = '\n'.join([ '[%s "%s"]' % (str(k).capitalize(), str(v)) for k,v in self.tags.items()  ])

        _moves = ''
        moves = zip_longest(*(iter(self.moves)*2), fillvalue='')

        for i, (w, b) in moves:
            _moves += '%d. %s %s ' % (i, w, b)

        return _desc + '\n\n' + _moves


    def move(self, move):

        valid = re.compile('(?P<piece>[PNBRQK]?)(?P<ocol>[a-h]?)(?P<orow>[1-8]?)(?P<cap>[xX]?)(?P<sq>[a-h][1-8])(?P<args>.*)')

        match = valid.match(move)
        if match:
            self.moves.append(move)
            return match.groupdict()
        else:
            raise IllegalMoveNotation(move)

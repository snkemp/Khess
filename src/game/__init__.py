
from src.game.board import Board
from src.game.notation import Notation

from src.engine import khess_engine


class Player:


    def __init__(self, name='Player'):
        self.name = name

    def move(self, board):
        print(board)
        return input(': ')


class Engine(Player):

    def __init__(self, *args):
        super().__init__(self, *args)
        self.machine = khess_engine()

    def move(self, board):
        print(board)
        print(': ', end='')
        move = self.machine.evaluate(board)
        print(move)
        return move


class Game:

    def __init__(self):
        self.board = board
        self.first_move = 1
        self.curr_move = 1

        p1 = input('What is your name player1 (leave empty for engine)? ')
        p2 = input('What is your name player2 (leave empty for engine)? ')
        self.players = (
            (Player(p1) if p1 else Engine('engine1')),
            (Player(p2) if p2 else Engine('engine2'))
        )

    def __iter__(self):
        self.first_move ^= 1
        self.curr_move = self.first_move
        self.board.reset()
        return self

    def __next__(self):
        move = self.players[self.curr_move].move(self.board)

        try:
            self.board(move)

        except KhessError as e:
            print(e)

        else:
            self.curr_move ^= 1

        return self.board


    def __repr__(self):
        return repr(self.board)

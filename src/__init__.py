
import os
from argparse import ArgumentParser

from src.chess import chess
import src.engine

class Player:

    def __init__(self):
        self.score = 0

    def won(self):
        self.score += 1

    def query(self, board):
        return input('\n>> ')




class Engine(Player):
    def query(self, board):
        move = engine.query(board)
        print(move)
        return move



class Game:

    def __init__(self):
        self.board = chess.Board()
        self._players = [ Player(), Engine() ]


    @property
    def players(self):
        while True:
            yield from self._players

    def reset(self):
        print(self.board)
        self.board.reset()
        self._players = self._players[::-1]

    def __iter__(self):
        players = self.players
        for p in players:

            try:
                yield self.board
                move = p.query(self.board)
                self.board.push_san(move)

                if self.board.is_game_over():
                    if self.board.is_checkmate():
                        p.won()
                    break
            except KeyboardInterrupt:
                return
            except:
                next(players)

        arg = input('\nWould you like to play another? ')
        if arg in 'no':
            raise StopIteration
        else:
            self.reset()
            yield from iter(self)


class Train:

    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass



class Session:

    def __init__(self):
        pass

    def __iter__(self):
        while True:
            try:

                func, *args = input('\nWhat would you like to do? ').split(' ')
                if not func:
                    os.system('clear')

                yield from getattr(self, func)(*args)

            except EOFError: # CTRL+D
                print('Quiting\n')
                self.quit()

            except KeyboardInterrupt:
                print('Stopped everything...\n')

            except AttributeError:
                print('Nothing here ..\n')


    def new(self):
        game = Game()
        for g in game:
            yield g


    def train(self):
        train = Train()
        for t in train:
            yield t


    def quit(self):
        raise StopIteration



def main():

    session = Session()
    for action in session:
        print('\n\n')
        print(action)



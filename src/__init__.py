
import os, sys, code

from src.game import Game


class Session:

    def __init__(self):
        self.game = None

    def __iter__(self):
        return self

    def __next__(self):

        try:
            args = input('>> ').strip()
            return getattr(self, args)()

        except AttributeError:
            print('$ No functionality for %s' % args)

        except EOFError:
            print('$ force quitting')
            raise StopIteration

        except KeyboardInterrupt:
            print('$ stopping processes')


    def newgame(self):
        if not self.game:
            self.game = Game()

        for board in self.game:
            print(board)

    def train(self):
        pass


    def sudo(self):
        code.interact(local=globals())

    def clear(self):
        os.system('clear')

    def quit(self):
        raise StopIteration


    def start(self):
        print('\t-- Khess --')

    def end(self):
        print('-'*80)



def main():

    session = Session()
    session.start()

    for _ in session:
        pass

    session.end()

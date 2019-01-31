

class Cell:
    BASE = 0xff
    RANK = 0x40
    FILE = 0x8

    @classmethod
    def shift(self, bits, f, r):
        f += self.RANK // self.FILE * r
        return bits << (f * self.FILE)

    @classmethod
    def drop(self, bits, f, r):
        f += self.RANK // self.FILE * r
        return bits >> (f * self.FILE)


    @classmethod
    def every(self, bits):
        return sum([ self.shift(bits, i) for i in range(64) ])

    @classmethod
    def first(self, bits):
        while not (bits & self.BASE):
            bits = self.drop(1)
        return bits


class Rank:
    def __new__(self, rank):
        return Cell.shift( sum([ Cell.shift(Cell.BASE, i) for i in range(8) ]), 0, rank )

    @classmethod
    def move(self, bits, rank):
        return Cell.shift(bits, 0, rank)

    @classmethod
    def find(self, bits):
        _rank = Rank(0)
        i = 0
        while not (bits & _rank):
            bits = Cell.drop(0, 1)
            i += 1

        return i


class File:
    def __new__(self, file):
        return Cell.shift( sum([ Cell.shift(Cell.BASE, 0, i) for i in range(8) ]), file )

    @classmethod
    def move(self, bits, file):
        return Cell.shift(bits, file)

    @classmethod
    def find(self, bits):
        _file = File(0)
        i = 0
        while not (bits & _file):
            bits = Cell.drop(1)
            i += 1

        return i


class Square(Rank, File):
    def __new__(self, file, rank=-1):
        if rank < 0:
            rank = file // 8
            file = file %  8

        return Rank(rank) & File(file)

    @classmethod
    def move(self, bits, file, rank=0):
        if rank < 0:
            rank = file // 8
            file = file % 8

        return Cell.shift(bits, file, rank)


    @classmethod
    def find(self, bits):
        rank = Rank.find(bits)
        file = File.find(bits)
        return 8*rank + file


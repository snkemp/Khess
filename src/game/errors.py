class KhessError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '%s: illegal syntax at \'%s\'' % (self.__class__.__name__, str(self.value))


class IllegalNotationError(KhessError):
    pass

class IllegalFEN(IllegalNotationError):
    pass

class IllegalPGN(IllegalNotationError):
    pass

class IllegalNotation(IllegalNotationError):
    pass



class IllegalMovementError(KhessError):
    pass

class IllegalPiece(IllegalMovementError):
    pass

class IllegalCaptureError(IllegalMovementError):
    pass

class IllegalMove(IllegalMovementError):
    pass

class IllegalCastle(IllegalMovementError):
    pass


from .Piece import Piece


class Knight(Piece):
    def __init__(self, team, type):
        super().__init__(team, type)

    def validMove(self):
        pass

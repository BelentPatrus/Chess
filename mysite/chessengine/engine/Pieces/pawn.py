from .piece import Piece


class Pawn(Piece):

    def __init__(self, team, type):
        super().__init__(team, type)

    def validMove(self):
        return False

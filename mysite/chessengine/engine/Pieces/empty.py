from .Piece import Piece


class Empty(Piece):
    def __init__(self, team, type):
        super().__init__(team, type)

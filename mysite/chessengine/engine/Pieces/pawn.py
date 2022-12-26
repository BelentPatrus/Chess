from .piece import Piece
from .empty import Empty


class Pawn(Piece):

    def __init__(self, team, type, moves):
        super().__init__(team, type, moves)

    def validMove(self, board, position):
        """
            args: The state of the board (2d array), the move that wants to be made (dictionary with field 'next' with move values).
            return: True or False on validity
        """
        row, col = position[0], position[1]
        if self.team == 'white':
            # moving forward and moving twice on start
            if isinstance(board[row-1][col], Empty):
                self.moves.append((row-1,col))
                if row == 6 and isinstance(board[row-2][col], Empty):
                    self.moves.append((row-2, col))
            # Take logic
            if not isinstance(board[row-1][col+1], Empty):
                self.moves.append((row-1, col+1))
            if not isinstance(board[row-1][col-1], Empty):
                self.moves.append((row-1, col-1))
        elif self.team == 'black':
            if isinstance(board[row+1][col], Empty):
                self.moves.append((row+1, col))
                if row == 1 and isinstance(board[row+2][col], Empty):
                    self.moves.append((row+2, col))
            # Take logic
            if not isinstance(board[row+1][col-1], Empty):
                self.moves.append((row+1, col-1))
            if not isinstance(board[row+1][col+1], Empty):
                self.moves.append((row-1, col+1))
        return set(position) in self.moves
        

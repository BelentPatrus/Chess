from django.db import models
# Create your models here.


class GameStateModel(models.Model):
    gameOver = models.BooleanField(default=False)
    playerTurn = models.SlugField(default="WHITE")
    totalMoves = models.PositiveSmallIntegerField(default=0)


class ChessboardModel(models.Model):
    chessboard = models.JSONField()
    date = models.DateTimeField(auto_now=True)
    playerTurn = models.TextField(max_length=15)
    gameState = models.ForeignKey(GameStateModel, on_delete=models.CASCADE)


class ChessBoardMove(models.Model):
    selectedPiece = models.JSONField()
    moveLocation = models.JSONField()
    result = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)
    gameState = models.ForeignKey(GameStateModel, on_delete=models.CASCADE)

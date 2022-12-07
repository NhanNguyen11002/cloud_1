from django.db import models


# Background Classes for Enums
class OutCome(models.IntegerChoices):
    XWin = 1,
    OWin = 2,
    Draw = -1
    ND = 0 # Means -> Not Determined

class PlayerChoice(models.IntegerChoices):
    X = 0
    O = 1

# ==== Real Models for storing data
class Game(models.Model):
    # need to set
    game_id = models.CharField(max_length=15, unique=True)
    tiles = models.PositiveIntegerField()
    # automatically set
    outcome = models.IntegerField(choices=OutCome.choices, default=OutCome.ND)
    turn = models.IntegerField(choices=PlayerChoice.choices, default=PlayerChoice.O)
    start_DT = models.DateTimeField(auto_now=True)

class Move(models.Model):
    # need to set
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.IntegerField(choices=PlayerChoice.choices)
    move = models.PositiveIntegerField()
    # automatically set
    time = models.TimeField(auto_now=True)

"""Storing Data about cureent state of the game
to determine the valid moves
keep a move log"""
class GameState():
    def __init__(self):
        self.board=[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"] ]
        self.whitetomove=True
        self.movelog=[]
    def makemove(self, move):
        self.board[move.startrow ][move.startcol]="--"
        self.board[move.endrow ][move.endcol]=move.piecemoved
        self.movelog.append(move)
        self.whitetomove = not self.whitetomove


class Move:
    # Map key to value
    rankstorow = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    r2r = {v: k for k, v in rankstorow.items()}

    filestocols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    c2f = {v: k for k, v in filestocols.items()}

    def __init__(self, startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]  # Corrected: use endsq for the ending row
        self.endcol = endsq[1]  # Corrected: use endsq for the ending column
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]  # Corrected: use endrow and endcol

    def chessnota(self):
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self, r, c):
        return self.c2f[c] + self.r2r[r]

        







































class Player():
    """Players Class"""
    def __init__(self,player_no):
        self.no = player_no
        self.points = 0
        self.history = []
        self.lastTurn = 0
        self.skip = False
        self.win = False
        self.rank = None
        self.next = None
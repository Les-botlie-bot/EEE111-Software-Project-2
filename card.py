class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.compute_value(rank)

    def compute_value(self, rank):
        if rank in ['J', 'Q', 'K']:
            return 10
        elif rank == 'A':
            return 11 #for now
        else: 
            return int(rank)
    def __str__(self):
        return f"{self.rank}{self.suit}"

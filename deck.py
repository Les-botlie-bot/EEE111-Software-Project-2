import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()

    def create_deck(self):
        allcards = []
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for rank in ranks:
                allcards.append(Card(rank, suit))
        return allcards

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self): #remove and return
        if len(self.cards) == 0:
            self.cards = self.create_deck()
            self.shuffle()
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)
        
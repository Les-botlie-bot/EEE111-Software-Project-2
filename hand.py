from card import Card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 #track aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'A':
            self.aces += 1
        self.ace_adjust()
    def ace_adjust(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    
    def is_blackjack(self):
        return self.value == 21 and len(self.cards) ==2
    
    def is_bust(self):
        return self.value > 21
    
    def __str__(self):
        cards_str = ', '.join(str(card) for card in self.cards)
        return f"{cards_str} (value: {self.value})"


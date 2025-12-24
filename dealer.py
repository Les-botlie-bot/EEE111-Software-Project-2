from hand import Hand

class Dealer:
    def __init__(self):
        self.hand = Hand()
    
    def play_turn(self, deck):
        print("Dealer's Turn!")
        print(f"Dealer's hand: {self.hand}")

        while self.hand.value < 17:
            new_card = deck.deal()
            self.hand.add_card(new_card)
            print(f"Dealer draws: {new_card}, Total: {self.hand.value}")

        if self.hand.value > 21:
            print(f"Dealer busts with {self.hand.value}")
        else:
            print(f"Dealer stands with {self.hand.value}\n")
    
    def reset_hand(self):
        self.hand = Hand()
    def __str__(self):
        return f"Dealer's Hand: {self.hand}"


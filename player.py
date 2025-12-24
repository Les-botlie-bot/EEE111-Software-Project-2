from hand import Hand

class Player:
    def __init__(self, name, balance = 100): #default to 100 for now
        self.name = name
        self.balance = balance
        self.bet = 0
        self.hand = Hand()

    def place_bet(self):
        while True:
            try:
                print(f"\n{self.name}'s current balance: {self.balance}$")
                bet_amount = int(input(f" enter your bet amount, {self.name}: $"))

                if bet_amount <= 0:
                    print("Bet must be greater than 0!")
                elif bet_amount > self.balance:
                    print("You must bet within your balance capacity!")
                else:
                    self.bet = bet_amount
                    self.balance -= bet_amount
                    print(f"Bet accepted: ${self.bet}\n")
                    break
            except ValueError:
                print(" Invalid input! Enter a whole number!")
            
    def hit(self, deck): #draw a card -> player hand
        newcard = deck.deal()
        self.hand.add_card(newcard)
        print(f"{self.name} drew a: {newcard}")
    def stand(self):
        print(f"{self.name} stands with value: {self.hand.value}")

    def reset_hand(self):
        self.hand = Hand()

    def __str__(self):
        return f"{self.name} | BALANCE: ${self.balance} | Hand: {self.hand}"   



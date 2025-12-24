from deck import Deck
from player import Player
from dealer import Dealer
import os

def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')

class BlackjackGame:

    def __init__(self):
        self.players = []
        self.dealer = Dealer()
        self.deck = None
        self.round_number = 1

    def display_table(self, hide_dealer = True):
        width = 50
        border_top = "┌" + "─" * (width - 2) + "┐"
        border_bottom = "└" + "─" * (width - 2) + "┘"
        border_side = '|'
#dealer
        print(border_top)
        print(border_side + "DEALER".center(width - 2) + border_side)
        print(border_side + " " * (width - 2) + border_side)

        if hide_dealer:
            dealer_cards = f"{self.dealer.hand.cards[0]}  [HIDDEN]"
            dealer_total = "???"
        else:
            dealer_cards = ' '.join(str(c) for c in self.dealer.hand.cards)
            dealer_total = str(self.dealer.hand.value)
        
        print(border_side + f"  Cards  : {dealer_cards}".ljust(width - 2) + border_side)
        print(border_side + f"  Total  : {dealer_total}".ljust(width - 2) + border_side)
        print(border_bottom)
        print("\n")
           
#platyer
        for player in self.players:
            print(border_top)
            print(border_side + f"Player: {player.name}".ljust(width - 2) + border_side)
            print(border_side + " ".ljust(width - 2) + border_side)

            balancestr = f"Balance :  ${player.balance}"
            bet_str = f"Bet :  ${player.bet}"
            print(
                border_side + 
                f" {balancestr}".ljust(30) +
                f" {bet_str}".ljust(width - 32) + 
                border_side
            )

            cards = " ".join(str(c) for c in player.hand.cards)
            print(border_side + f"  Cards  :  {cards}".ljust(width - 2) + border_side)
            print(border_side + f"  Total  :  {player.hand.value}".ljust(width - 2) + border_side)
            print(border_bottom)
            print()

        

    def start(self):
        print("\n==== WELCOME TO BLACKJACK ====\n")
        self.setup_players()

        while True:
            clear_screen()
            print(f"\n==== ROUND {self.round_number} ====")
            self.deck = Deck() #reshuffle
            self.place_bets()
            self.initial_deal()
            self.run_player_turns()
            self.run_dealer_turn()
            self.resolve_round()
            self.eliminate_broke_players()

            if len(self.players) == 0:
                print("\n All players are out of money! GAME OVER! House wins as always XD")
                break
            if not self.ask_continue():
                print("\n Thanks for playing, see you soon ;)")
                break

            self.round_number += 1
    
    def setup_players(self):
        while True:
            try:
                count = int(input("Enter number of players [1 - 7]:  "))
                if count < 1 or count > 7:
                    print("only 1 to 7 players can play at a time")
                else:
                    break
            except ValueError:
                print("invalid input, please enter a whole number.")

        for i in range(count):
            name = input(f"Enter name for player {i + 1}: ").strip()
            if name == "":
                name = f"Player {i+1}"
            self.players.append(Player(name))
        print(f"\n {len(self.players)} player(s) ready!\n")

    def place_bets(self):
        for player in self.players:
            player.place_bet()
    
    def initial_deal(self):
        for player in self.players:
            player.reset_hand()
            player.hand.add_card(self.deck.deal())
            player.hand.add_card(self.deck.deal())

        self.dealer.reset_hand()
        self.dealer.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())

        print("\n --- Initial Hands ---")
        for player in self.players:
            print(f"{player.name}: {player.hand}")
        
        print(f"Dealer's Card: {self.dealer.hand.cards[0]} and [hidden]")
    
    def run_player_turns(self):
        for player in self.players:
            while True:
                clear_screen()
                self.display_table(hide_dealer= True)
                print(f"\n==== {player.name}'s Turn ====")
        
                if player.hand.is_blackjack():
                    print("BLACKJACK!")
                    input("Press Enter to continue...")
                    break
                if player.hand.is_bust():
                    print("BUST!")
                    input("Press Enter to continue...")
                    break
                choice = input("Do you want to (1)Hit or (2)stand?  ").strip()
                if choice == '1':
                    player.hit(self.deck)
                elif choice == '2':
                    player.stand()
                    input("Press Enter to continue...")
                    break
                else:
                    print("Invalid choice, Please enter 1 or 2")
    
    def run_dealer_turn(self):
        clear_screen()
        print("\n---- Dealer's Hand Reveal ----")
        self.display_table(hide_dealer= False)
        self.dealer.play_turn(self.deck)
        input("Press Enter to continue...")
    
    def resolve_round(self):
        clear_screen()
        dealer_total = self.dealer.hand.value
        print("\n---- ROUND RESULTS! ----")

        for player in self.players:
            player_total = player.hand.value
            print(f"{player.name}'s final hand: {player.hand}")

            if player.hand.is_bust():
                print(f"{player.name} Busts! And loses ${player.bet}")

            elif self.dealer.hand.is_blackjack() and not player.hand.is_blackjack():
                print(f" Dealer has a BLACKJACK!! {player.name} loses ${player.bet}")

            elif player.hand.is_blackjack() and not self.dealer.hand.is_blackjack():
                winning = int(player.bet * 2.5)
                print(f"BLACKJACK! {player.name} wins ${winning}")
                player.balance += winning
            elif self.dealer.hand.is_bust():
                print(f"Dealer Busts! {player.name} wins ${player.bet * 2}")
                player.balance += player.bet * 2
            
            elif player_total > dealer_total:
                print(f"{player.name} wins ${player.bet * 2}!")
                player.balance += player.bet * 2
            elif player_total == dealer_total:
                print(f"{player.name} ties, bet returned")
                player.balance += player.bet

            else:
                print(f"Dealer wins against {player.name}. lost ${player.bet}")
        
        print("--- $Balances$ ---")
        for player in self.players:
            print(f"{player.name}: {player.balance}")
        input("\nPress Enter to continue...")
    
    def eliminate_broke_players(self):
        self.players = [p for p in self.players if p.balance > 0]
    
    def ask_continue(self):
        remaining_players = []
        for player in self.players:
            while True:
                choice = input(f"{player.name}, would you like to continue playing? [Y or N]").strip().lower()
                if choice == 'y':
                    remaining_players.append(player)
                    break
                elif choice == 'n':
                    print(f"{player.name} has left the table")
                    break
                else:
                    print("please enter Y or N")
        self.players = remaining_players
        return len(self.players) > 0

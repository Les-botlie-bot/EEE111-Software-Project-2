# ♠️ BLACKJACK (Software Project 2)

### 🃏 What is Blackjack?

**Blackjack** is a Python-based implementation of the classic casino card game   
This project was developed as part of my **EEE 111** course, following strict modular design and OOP principles.  
It includes features such as multi-player gameplay, betting logic, and a fully automated dealer system — all through a clean **command-line interface (CLI)**.

---

## ⚙️ **Features and Technology**

### 🧠 Technology
The game was developed using **Python 3.11** and the **Visual Studio Code** IDE.  
It uses standard Python libraries only (no external dependencies) and runs directly in the terminal.

### 🎮 Features
- Up to **7 human players** can compete simultaneously against **one dealer**.  
- A **betting system** where each player wagers each round.  
- A **dealer** following official Blackjack rules (hits until 17 or higher).  
- Dynamic **command-line display** showing cards, totals, and balances.  
- **Detection of Blackjack, bust, and ties** for accurate scoring.  
- **Automatic elimination** of broke players.  
- **Error handling and input validation** for player count, bets, and choices.  
- Built using an **object-oriented structure** (Card, Deck, Hand, Player, Dealer, Game).  

---

## 🧩 **Program Architecture**

| File | Description |
|------|--------------|
| `main.py` | Entry point – runs the game. |
| `card.py` | Defines the `Card` class (rank, suit, and value). |
| `deck.py` | Builds and manages the deck of 52 cards. |
| `hand.py` | Tracks cards and total values for players and dealer. |
| `player.py` | Manages player data (balance, bets, actions). |
| `dealer.py` | Handles the dealer’s automated gameplay. |
| `game.py` | Main controller – handles rounds, turns, and results. |

---

## 🧠 **How to Run** 

1. Clone or download the repository:
   ```bash
   git clone https://github.com/Les-botlie-bot/EEE111-Software-Project-2.git
2. Download all the files in the repository or the folder submitted in UVLE

3. Extract the Zipped file if necessary, make sure that all of the python files are in the same folder / directory

4. run the python main.py file on VS code and follow the on-screen game instructions


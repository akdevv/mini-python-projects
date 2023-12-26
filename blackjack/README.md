# Blackjack

## Overview
This Python project is an implementation of the classic Blackjack card game. It provides a console-based interface for playing Blackjack against a computer dealer.

## How to Use
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/akdevv/mini-python-projects.git
    cd mini-python-projects
    cd blackjack
    ```
2. **Run _main.py_:**
    ```bash
    python main.py
    ```

## Examples
```
Do you want to play a game of Blackjack? Type 'y' or 'n': y

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

        Your cards: [10, 6], current score: 16
        Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: y
        Your cards: [10, 6, 10], current score: 26
        Computer's first card: 6
        Your final hand: [10, 6, 10], final score: 26
        Computer's final hand: [6, 9, 9], final score: 24
You went over. You lose 😤
Do you want to play a game of Blackjack? Type 'y' or 'n': y

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

        Your cards: [5, 5], current score: 10
        Computer's first card: 2
Type 'y' to get another card, type 'n' to pass: y
        Your cards: [5, 5, 4], current score: 14
        Computer's first card: 2
Type 'y' to get another card, type 'n' to pass: n
        Your final hand: [5, 5, 4], final score: 14
        Computer's final hand: [2, 5, 5, 10], final score: 22
Opponent went over. You win 😁
Do you want to play a game of Blackjack? Type 'y' or 'n': n
```
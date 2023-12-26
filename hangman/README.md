# Hangman Game

## Overview
Hangman Game is word guessing game in terminal made with Python. The project incorporates fundamental programming concepts, including random word selection, user input validation, and interactive gameplay.

## How to Use
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/akdevv/mini-python-projects.git
    cd mini-python-projects
    cd hangman
    ```
2. **Run _main.py_:**
    ```bash
    python main.py
    ```

## Examples
```
 _                                          
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
Guess a letter: a
a _ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: c
You guessed c, that's not in the word. You lose a life.
a _ _ _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess a letter: k
a _ k _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess a letter: o 
You guessed o, that's not in the word. You lose a life.
a _ k _ _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: w
a _ k _ w

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: s
a s k _ w

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: e
a s k e w
You win.

  +---+
  |   |
  O   |
  |   |
      |
      |
=========
```
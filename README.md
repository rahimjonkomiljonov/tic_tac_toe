Tic Tac Toe (Text-Based)
A simple, text-based Tic Tac Toe game implemented in Python, playable in the command line. Supports both two-player mode and single-player mode against an AI opponent.
Features

3x3 Tic Tac Toe board with clear text-based display.
Two-player mode: Players alternate as 'X' and 'O'.
Single-player mode: Play as 'X' against an AI opponent ('O') that makes random moves.
Input validation to ensure only valid moves are accepted.
Automatic detection of wins and draws.
Option to play again after each game.
User-friendly prompts and error messages.

Requirements

Python 3.x
No external dependencies (uses the standard random module).

Setup

Save the game code in a file named tic_tac_toe.py.
Open a terminal or command prompt.
Navigate to the directory containing tic_tac_toe.py.
Run the game with the command:python tic_tac_toe.py



Gameplay Instructions

Start the Game:

Run the script, and you'll see a welcome message.
Choose a game mode by entering:
1 for single-player (you vs AI).
2 for two-player (human vs human).




Playing the Game:

The board is displayed as a 3x3 grid with numbers 1-9 representing empty cells: 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 


Two-Player Mode:
Players take turns as 'X' and 'O'.
Enter a number (1-9) to place your mark in the corresponding cell.


Single-Player Mode:
You play as 'X', entering a number (1-9) for your move.
The AI plays as 'O', automatically selecting a random empty cell.


Invalid moves (e.g., choosing an occupied cell or entering a non-number) prompt an error message and a retry.


Game End:

The game announces a win (e.g., "Player X wins!" or "AI wins!") or a draw.
Choose to play again by entering yes or exit with no.



Example Gameplay (Single-Player)
Welcome to Tic Tac Toe!
Players take turns to place 'X' or 'O' by selecting a number 1-9.
In single-player mode, you are 'X' and the AI is 'O'.
Select game mode (1 for single-player vs AI, 2 for two-player): 1

 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 

Player X, enter a number (1-9): 5

 1 | 2 | 3 
---+---+---
 4 | X | 6 
---+---+---
 7 | 8 | 9 

AI chooses position 1

 X | 2 | 3 
---+---+---
 4 | X | 6 
---+---+---
 7 | 8 | 9 

Player X, enter a number (1-9): 3
...
Player X wins!
Do you want to play again? (yes/no): no
Thanks for playing!

Additional Notes

The AI opponent uses a simple random move strategy, making it suitable for casual play.
The code is modular and can be extended (e.g., to implement a smarter AI using Minimax or support larger boards).
Contributions or suggestions are welcome! Feel free to fork the project or submit feedback.


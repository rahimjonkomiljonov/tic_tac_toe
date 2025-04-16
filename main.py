# Tic Tac Toe game with two-player and single-player (vs AI) modes in Python
import random


def initialize_board():
    # Create a board with numbers 1-9 as placeholders for empty cells
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def display_board(board):
    # Print the 3x3 Tic Tac Toe board with borders
    print('\n')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('\n')


def is_valid_move(board, move):
    # Check if the move is valid (1-9 and cell is empty)
    try:
        move = int(move)
        if 1 <= move <= 9 and board[move - 1] not in ['X', 'O']:
            return True
        return False
    except ValueError:
        return False


def make_move(board, move, player):
    # Place the player's mark ('X' or 'O') on the board
    board[int(move) - 1] = player


def check_win(board, player):
    # Check all winning combinations for the player
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def check_draw(board):
    # Check if the game is a draw (no empty cells left)
    return all(cell in ['X', 'O'] for cell in board)


def get_ai_move(board):
    # AI selects a random empty cell
    empty_cells = [str(i + 1) for i in range(9) if board[i] not in ['X', 'O']]
    move = random.choice(empty_cells)
    return move


def select_game_mode():
    # Prompt user to select game mode
    while True:
        mode = input("Select game mode (1 for single-player vs AI, 2 for two-player): ")
        if mode in ['1', '2']:
            return mode
        print("Invalid input! Please enter 1 or 2.")


def play_game():
    while True:
        # Select game mode
        game_mode = select_game_mode()
        single_player = (game_mode == '1')

        # Initialize game state
        board = initialize_board()
        current_player = 'X'

        while True:
            # Display the board
            display_board(board)

            # Handle move based on player and game mode
            if single_player and current_player == 'O':
                # AI's turn
                move = get_ai_move(board)
                print(f"AI chooses position {move}")
            else:
                # Human player's turn
                move = input(f"Player {current_player}, enter a number (1-9): ")

                # Validate the move
                if not is_valid_move(board, move):
                    print("Invalid move! Please choose an empty cell (1-9).")
                    continue

            # Make the move
            make_move(board, move, current_player)

            # Check for a win
            if check_win(board, current_player):
                display_board(board)
                if single_player and current_player == 'O':
                    print("AI wins!")
                else:
                    print(f"Player {current_player} wins!")
                break

            # Check for a draw
            if check_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


# Start the game
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    print("Players take turns to place 'X' or 'O' by selecting a number 1-9.")
    print("In single-player mode, you are 'X' and the AI is 'O'.")
    play_game()
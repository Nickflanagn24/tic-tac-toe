import sys
import random
import os

class TicTacToe:
    def __init__(self):
        # Initialize the game board as a 3x3 grid of empty spaces
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        # Players: "X" and "O"
        self.players = ["X", "O"]
        
        # Start with player 0 ("X") as the current player
        self.current_player = 0
        
        # Default player names
        self.player_names = ["Player 1", "Player 2"]
        
        # Default game mode ("human" vs "computer")
        self.mode = "human"
        
        # Difficulty setting for computer mode ("Easy" or "Hard")
        self.difficulty = ""

    def clear_screen(self):
        # Clear the terminal screen for a clean view
        os.system("cls" if os.name == "nt" else "clear")

    def print_banner(self):
        # Display the ASCII art banner for the game
        print("//////////////////////////////////////////////////////")
        print("// _____ _        _____             _____           //")
        print("///__   (_) ___  /__   \\__ _  ___  /__   \\___   ___ //")
        print("//  / /\\/ |/ __|   / /\\/ _ |/ __|   / /\\/ _ \\ / _ \\//")
        print("// / /  | | (__   / / | (_| | (__   / / | (_) |  __///")
        print("// \\/   |_|\\___|  \\/   \\__,_|\\___|  \\/   \\___/ \\___|//")  
        print("//////////////////////////////////////////////////////")
        print("\n")

    def print_welcome(self):
        # Show the welcome screen with instructions
        self.print_banner()
        print("=================================")
        print("       Welcome to Tic Tac Toe    ")
        print("=================================")
        print("Game Instructions:")
        print("- Two players take turns marking a square on the board.")
        print("- The first to align 3 of their marks in a row, column, or diagonal wins!")
        print("- Choose the difficulty level (Easy or Hard) for Human vs Computer mode.")
        print("- If the board fills up without a winner, it's a tie.")
        print()

    def print_board(self):
        # Print the current state of the board using emojis for each cell
        # "X" = ✖️, "O" = ⭕, empty = ⬜
        for row in self.board:
            print(" | ".join(
                f"{'✖️' if cell == 'X' else '⭕' if cell == 'O' else '⬜'}" 
                for cell in row
            ))
            print("-" * 11)

    def reset_board(self):
        # Reset the board to an empty state and reset the current player
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 0

    def play_turn(self):
        # Play a single turn. If it's the computer's turn, let the AI pick a move,
        # otherwise prompt a human player for input.
        if self.mode == "computer" and self.current_player == 1:
            self.computer_move()
        else:
            row, col = self.get_human_move()
            # Check if the chosen cell is empty
            if self.board[row][col] != " ":
                print("Invalid move! That cell is already taken.")
                return False
            self.board[row][col] = self.players[self.current_player]
        return True

    def get_human_move(self):
        # Prompt the human player for a valid move (row and column)
        # Keep asking until a valid input is provided
        while True:
            try:
                move = input("Enter your move (row and column as '1 3'): ").strip()
                move = "".join(move.split())  # Remove all spaces
                row, col = int(move[0]), int(move[1])
                if row in range(1, 4) and col in range(1, 4):
                    return row - 1, col - 1
                else:
                    print("Please enter numbers between 1 and 3.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter two numbers in the format '1 3'.")

    def computer_move(self):
        # Make a move for the computer.
        # In Easy mode, pick a random empty cell.
        # In Hard mode, use the minimax algorithm to choose the best move.
        if self.difficulty == "Easy":
            empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]
            move = random.choice(empty_cells)
        else:  # Hard mode
            move = self.minimax_move()
        self.board[move[0]][move[1]] = self.players[self.current_player]

    def minimax_move(self):
        # Use the minimax algorithm to find the best possible move for the AI.
        best_score = float("-inf")
        best_move = None
        # Check each empty cell, simulate placing the "O" there, and evaluate with minimax
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == " ":
                    self.board[r][c] = self.players[1]  # Place "O"
                    score = self.minimax(False)
                    self.board[r][c] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (r, c)
        return best_move

    def minimax(self, is_maximizing):
        # The minimax algorithm attempts to choose the optimal move for the AI:
        # - If `is_maximizing` is True, we are choosing moves for the AI ("O").
        # - If False, we are simulating the opponent ("X").
        
        # Check if there's a winner
        winner = self.check_winner("X") or self.check_winner("O")
        if winner:
            # If "O" (AI) wins, return 1. If "X" (human) wins, return -1.
            return 1 if winner == "O" else -1
        # If board is full, it's a tie, return 0
        if self.is_full():
            return 0

        if is_maximizing:
            # AI's turn: try to maximize the score
            best_score = float("-inf")
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == " ":
                        self.board[r][c] = "O"
                        score = self.minimax(False)
                        self.board[r][c] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            # Opponent's turn: try to minimize the score
            best_score = float("inf")
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == " ":
                        self.board[r][c] = "X"
                        score = self.minimax(True)
                        self.board[r][c] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        # Check all rows for a win
        for row in self.board:
            if all(cell == player for cell in row):
                return player
        # Check all columns for a win
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return player
        # Check diagonals for a win
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return player
        return None

    def is_full(self):
        # Check if the board is completely filled with no empty spaces
        return all(self.board[r][c] != " " for r in range(3) for c in range(3))

    def play_game(self):
        # Orchestrate the game
        self.reset_board()
        self.clear_screen()
        print(f"{self.player_names[0]} is X and {self.player_names[1]} is O.")
        while True:
            self.clear_screen()
            self.print_board()
            print(f"{self.player_names[self.current_player]}'s turn ({self.players[self.current_player]}).")
            if not self.play_turn():
                continue
            if self.check_winner(self.players[self.current_player]):
                self.clear_screen()
                self.print_board()
                print(f"Congratulations, {self.player_names[self.current_player]}! You win!")
                break
            if self.is_full():
                self.clear_screen()
                self.print_board()
                print("It's a tie!")
                break
            self.current_player = 1 - self.current_player

    def setup_game(self):
        # Setup the game mode and difficulty (if playing against the computer).
        print("\nSelect game mode:")
        print("1. Human vs Human")
        print("2. Human vs Computer")
        mode_choice = input("Enter your choice: ")
        while mode_choice not in ["1", "2"]:
            print("Invalid choice. Please select either 1 (Human vs Human) or 2 (Human vs Computer).")
            mode_choice = input("Enter your choice: ")

        if mode_choice == "2":
            self.mode = "computer"
            self.player_names[0] = input("Enter name for Player 1: ").strip() or "Player 1"
            self.player_names[1] = "Computer"
            print("Select difficulty:")
            print("1. Easy")
            print("2. Hard")
            difficulty_choice = input("Enter your choice: ")
            while difficulty_choice not in ["1", "2"]:
                print("Invalid choice. Please select either 1 (Easy) or 2 (Hard).")
                difficulty_choice = input("Enter your choice: ")
            self.difficulty = "Easy" if difficulty_choice == "1" else "Hard"
        else:
            self.mode = "human"
            self.player_names[0] = input("Enter name for Player 1: ").strip() or "Player 1"
            self.player_names[1] = input("Enter name for Player 2: ").strip() or "Player 2"

    def welcome_screen(self):
        # Display the welcome screen and ask the user to see instructions or start the game
        self.print_welcome()
        print("1. See instructions")
        print("2. Start game")
        choice = input("Enter your choice: ")
        while choice not in ["1", "2"]:
            print("Invalid choice. Please select 1 (See instructions) or 2 (Start game).")
            choice = input("Enter your choice: ")

        if choice == "1":
            # Print instructions if chosen
            print("""
Tic Tac Toe Instructions:
- Players take turns marking a square on a 3x3 grid.
- The first to align 3 of their marks in a row, column, or diagonal wins!
- If the board fills up without a winner, it's a tie.
            """)
        self.setup_game()
        self.play_game()

if __name__ == "__main__":
    # Create an instance of the game and show the welcome screen
    game = TicTacToe()
    game.welcome_screen()

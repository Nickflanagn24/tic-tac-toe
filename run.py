import sys
import random
import os


class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.current_player = 0
        self.player_names = ["Player 1", "Player 2"]
        self.mode = "human"
        self.difficulty = ""

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.print_banner()

    def print_banner(self):
        print("//////////////////////////////////////////////////////")
        print("// _____ _        _____             _____           //")
        print("///__   (_) ___  /__   \\__ _  ___  /__   \\___   ___ //")
        print("//  / /\\/ |/ __|   / /\\/ _ |/ __|   / /\\/ _ \\ / _ \\//")
        print("// / /  | | (__   / / | (_| | (__   / / | (_) |  __///")
        print("// \\/   |_|\\___|  \\/   \\__,_|\\___|  \\/   \\___/ \\___|//")
        print("//////////////////////////////////////////////////////")
        print("\n")

    def print_welcome(self):
        self.print_banner()
        print("=================================")
        print("       Welcome to Tic Tac Toe    ")
        print("=================================")
        print("Game Instructions:")
        print("- Two players take turns marking a square on the board.")
        print("- The first to align 3 of their marks in a row, \
column, or diagonal wins!")
        print("- Choose the difficulty level (Easy or Hard) \
for Human vs Computer mode.")
        print("- If the board fills up without a winner, it's a tie.")
        print()

    def print_board(self):
        for row in self.board:
            print(" | ".join(
                f"{'✖️' if cell == 'X' else '⭕' if cell == 'O' else '⬜'}"
                for cell in row
            ))
            print("-" * 11)

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 0

    def play_turn(self):
        if self.mode == "computer" and self.current_player == 1:
            self.computer_move()
        else:
            row, col = self.get_human_move()
            if self.board[row][col] != " ":
                print("Invalid move! That cell is already taken.")
                return False
            self.board[row][col] = self.players[self.current_player]
        return True

    def get_human_move(self):
        while True:
            try:
                move = input(
                    "Enter your move (row and column as '1 3'): ").strip()
                if move.lower() == "exit":
                    print(
                        f"Goodbye, {self.player_names[self.current_player]}!")
                    sys.exit()
                move = "".join(move.split())
                row, col = int(move[0]), int(move[1])
                if row in range(1, 4) and col in range(1, 4):
                    return row - 1, col - 1
                else:
                    print("Please enter numbers between 1 and 3.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter \
two numbers in the format '1 3'.")

    def computer_move(self):
        if self.difficulty == "Easy":
            empty_cells = [(r, c) for r in range(3)
                           for c in range(3) if self.board[r][c] == " "]
            move = random.choice(empty_cells)
        else:
            move = self.minimax_move()
        self.board[move[0]][move[1]] = self.players[self.current_player]

    def minimax_move(self):
        best_score = float("-inf")
        best_move = None
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == " ":
                    self.board[r][c] = self.players[1]
                    score = self.minimax(False)
                    self.board[r][c] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (r, c)
        return best_move

    def minimax(self, is_maximizing):
        winner = self.check_winner("X") or self.check_winner("O")
        if winner:
            return 1 if winner == "O" else -1
        if self.is_full():
            return 0

        if is_maximizing:
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
        for row in self.board:
            if all(cell == player for cell in row):
                return player
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return player
        if all(self.board[i][i] == player for i in range(3)) or all(
                self.board[i][2 - i] == player for i in range(3)):
            return player
        return None

    def is_full(self):
        return all(self.board[r][c] != " " for r in range(3) for c in range(3))

    def end_game(self):
        print("\nWhat would you like to do next?")
        print("1. Return to the start screen")
        print("2. Play again")
        print("3. Exit")
        choice = input("Enter your choice: ")
        while choice not in ["1", "2", "3"]:
            print("Invalid choice. Please select 1, 2, or 3.")
            choice = input("Enter your choice: ")

        if choice == "1":
            self.welcome_screen()
        elif choice == "2":
            self.play_game()
        elif choice == "3":
            if self.mode == "human":
                print(
                    f"Thank you for playing, {
                        self.player_names[0]} and {
                        self.player_names[1]}!")
            else:
                print(f"Thank you for playing, {self.player_names[0]}!")
            sys.exit()

    def play_game(self):
        self.reset_board()
        self.clear_screen()
        print(f"{self.player_names[0]} is X and {self.player_names[1]} is O.")
        while True:
            self.clear_screen()
            print(
                f"{self.player_names[self.current_player]}'s \
turn ({self.players[self.current_player]}):")
            self.print_board()
            if not self.play_turn():
                continue
            if self.check_winner(self.players[self.current_player]):
                self.clear_screen()
                self.print_board()
                print(
                    f"Congratulations, {self.player_names[self.current_player]}! You win!")
                self.end_game()
                break
            if self.is_full():
                self.clear_screen()
                self.print_board()
                print("It's a tie!")
                self.end_game()
                break
            self.current_player = 1 - self.current_player

    def setup_game(self):
        print("\nSelect game mode:")
        print("1. Human vs Human")
        print("2. Human vs Computer")
        mode_choice = input("Enter your choice: ")
        while mode_choice not in ["1", "2"]:
            print(
                "Invalid choice. Please select either 1 (Human vs Human) or 2 (Human vs Computer).")
            mode_choice = input("Enter your choice: ")

        if mode_choice == "2":
            self.mode = "computer"
            self.player_names[0] = input(
                "Enter name for Player 1: ").strip() or "Player 1"
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
            self.player_names[0] = input(
                "Enter name for Player 1: ").strip() or "Player 1"
            self.player_names[1] = input(
                "Enter name for Player 2: ").strip() or "Player 2"

    def welcome_screen(self):
        self.print_welcome()
        print("1. See instructions")
        print("2. Start game")
        choice = input("Enter your choice: ")
        while choice not in ["1", "2"]:
            print("Invalid choice. Please select 1 (See instructions) or 2 (Start game).")
            choice = input("Enter your choice: ")

        if choice == "1":
            print("""
Tic Tac Toe Instructions:
- Players take turns marking a square on a 3x3 grid.
- The first to align 3 of their marks in a row, column, or diagonal wins!
- If the board fills up without a winner, it's a tie.
            """)
        self.setup_game()
        self.play_game()


if __name__ == "__main__":
    game = TicTacToe()
    game.welcome_screen()

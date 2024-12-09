import random

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.current_player = 0
        self.player_names = ["Player 1", "Player 2"]
        self.mode = "human"
        self.difficulty = ""

    def print_banner(self):
        """Display the game's banner."""
        print("//////////////////////////////////////////////////////")
        print("// _____ _        _____             _____           //")
        print("///__   (_) ___  /__   \\__ _  ___  /__   \\___   ___ //")
        print("//  / /\\/ |/ __|   / /\\/ _` |/ __|   / /\\/ _ \\ / _ \\//")
        print("// / /  | | (__   / / | (_| | (__   / / | (_) |  __///")
        print("// \\/   |_|\\___|  \\/   \\__,_|\\___|  \\/   \\___/ \\___|//")  
        print("//////////////////////////////////////////////////////")
        print("\n")

    def print_welcome(self):
        """Display the welcome message and instructions."""
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
        """Print the game board with emojis for better visual appeal."""
        print("\n")
        for row in self.board:
            print(" | ".join(f"{'❌' if cell == 'X' else '⭕' if cell == 'O' else '⬜'}" for cell in row))
            print("-" * 11)
        print("\n")

    def reset_board(self):
        """Reset the game board to an empty state."""
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
            move = input("Enter your move (row and column as '1 3'): ")
            row, col = map(int, move.split())
            if row in range(1, 4) and col in range(1, 4):
                return row - 1, col - 1
            else:
                print("Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space.")

    def computer_move(self):
        """Make a move for the computer based on difficulty."""
        if self.difficulty == "Easy":
            empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]
            move = random.choice(empty_cells)
        else:  # Hard difficulty
            move = self.minimax_move()
        self.board[move[0]][move[1]] = self.players[self.current_player]

    def minimax_move(self):
        """Minimax algorithm for the computer to make an optimal move in Hard mode."""
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
        """Recursively evaluate the board using the Minimax algorithm."""
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
    if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
        return player
    return None

def is_full(self):
    return all(self.board[r][c] != " " for r in range(3) for c in range(3))

def computer_move(self):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]
    move = random.choice(empty_cells)
    self.board[move[0]][move[1]] = self.players[self.current_player]



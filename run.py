class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.current_player = 0
        self.player_names = ["Player 1", "Player 2"]
        self.mode = "human"
        self.difficulty = ""

def print_board(self):
    for row in self.board:
        print(" | ".join(f"{'❌' if cell == 'X' else '⭕' if cell == 'O' else '⬜'}" for cell in row))
        print("-" * 11)

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

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


class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.current_player = 0
        self.player_names = ["Player 1", "Player 2"]
        self.mode = "human"
        self.difficulty = ""


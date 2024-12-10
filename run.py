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
        """Play a single turn for the current player."""
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
        """Get the move from a human player."""
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
        """Check if the given player has won the game."""
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
        """Check if the board is full."""
        return all(self.board[r][c] != " " for r in range(3) for c in range(3))

    def play_game(self):
        """Play the full game."""
        self.reset_board()
        print(f"\n{self.player_names[0]} is X and {self.player_names[1]} is O.")
        while True:
            self.print_board()
            print(f"{self.player_names[self.current_player]}'s turn ({self.players[self.current_player]}).")
            if not self.play_turn():
                continue
            if self.check_winner(self.players[self.current_player]):
                self.print_board()
                if self.mode == "computer" and self.current_player == 1:
                    print(f"Sorry, {self.player_names[0]}! You lost. Better luck next time!")
                    print("""
       :::        ::::::::   ::::::::  :::::::::: :::::::::
     :+:       :+:    :+: :+:    :+: :+:        :+:    :+:
    +:+       +:+    +:+ +:+        +:+        +:+    +:+ 
   +#+       +#+    +:+ +#++:++#++ +#++:++#   +#++:++#:   
  +#+       +#+    +#+        +#+ +#+        +#+    +#+   
 #+#       #+#    #+# #+#    #+# #+#        #+#    #+#    
########## ########   ########  ########## ###    ###     
                    """)
                else:
                    print(f"Congratulations, {self.player_names[self.current_player]}! You win!")
                    print("""
:::       ::: ::::::::::: ::::    ::: ::::    ::: :::::::::: :::::::::
:+:       :+:     :+:     :+:+:   :+: :+:+:   :+: :+:        :+:    :+:
+:+       +:+     +:+     :+:+:+  +:+ :+:+:+  +:+ +:+        +:+    +:+ 
+#+  +:+  +#+     +#+     +#+ +:+ +#+ +#+ +:+ +#+ +#++:++#   +#++:++#:   
+#+ +#+#+ +#+     +#+     +#+  +#+#+# +#+  +#+#+# +#+        +#+    +#+   
#+# #+#+#      #+#     #+#   #+#+# #+#   #+#+# #+#        #+#    #+#    
###   ###   ########### ###    #### ###    #### ########## ###    ###     
                    """)
                self.end_game()
                break
            if self.is_full():
                self.print_board()
                print("It's a tie!")
                print("""
::::::::::: ::::::::::: ::::::::::
     :+:         :+:     :+:        
    +:+         +:+     +:+         
   +#+         +#+     +#++:++#     
  +#+         +#+     +#+           
 #+#         #+#     #+#            
###     ########### ##########      
                """)
                self.end_game()
                break
            self.current_player = 1 - self.current_player

    def end_game(self):
        """Offer options after the game finishes."""
        print("\nWhat would you like to do next?")
        print("1. Return to the start screen")
        print("2. Play again")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.welcome_screen()
        elif choice == "2":
            self.play_game()
        elif choice == "3":
            print(f"Thank you for playing, {self.player_names[0]} and {self.player_names[1]}!")
            exit()
        else:
            print("Invalid choice! Exiting...")
            exit()

    def setup_game(self):
        """Setup the game mode and difficulty."""
        print("\nSelect game mode:")
        print("1. Human vs Human")
        print("2. Human vs Computer")
        mode_choice = input("Enter your choice: ")
        if mode_choice == "2":
            self.mode = "computer"
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
            self.player_names[1] = input("Enter name for Player 2: ")
        self.player_names[0] = input("Enter name for Player 1: ")

    def welcome_screen(self):
        """Display the welcome screen and get user input to start the game."""
        self.print_welcome()
        print("1. See instructions")
        print("2. Start game")
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


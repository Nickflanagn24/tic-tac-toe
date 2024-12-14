# Tic Tac Toe - Command-Line Application

![Flowchart](overview-placeholder.png)

## Overview
Tic Tac Toe is a classic two-player game implemented as a command-line application. This project was designed to demonstrate programming fundamentals, object-oriented programming (OOP), and clean code practices while creating an engaging and functional application. The project caters to both human players and includes an option to play against a computer opponent with adjustable difficulty.

---

## 1. Logic and Code Efficiency (1.1, 2.1)

### Code Efficiency
The application's logic is broken into small, reusable methods and functions, adhering to the principles of DRY (Don’t Repeat Yourself). The core gameplay loop ensures smooth transitions between player turns, validations for moves, and the game's end conditions.

### Granular Functions
Key functions include:
- **`print_board`**: Displays the game board with emojis for visual clarity.
- **`play_turn`**: Handles individual player or computer moves.
- **`check_winner`**: Determines if there’s a winner based on the current board state.
- **`computer_move`**: Implements AI logic for computer moves (easy or hard).
- **`minimax`**: A recursive algorithm for determining the optimal move in hard difficulty.

This modular structure ensures consistency in logic flow and simplifies testing and debugging.

---

## 2. Programming Fundamentals and OOP (3.1, 3.2)

### Programming Constructs
The project demonstrates:
- Control structures like loops and conditionals for board navigation and move validation.
- Recursive functions for the Minimax algorithm.
- Data structures like lists for representing the game board.

### Object-Oriented Programming
The application is encapsulated within the **`TicTacToe`** class. Key features:
- Encapsulation of game data (e.g., board, players).
- Methods for gameplay and utility, enhancing code reusability.
- Clear relationships between game elements.

This OOP approach ensures scalability and future extensibility, such as integrating a graphical interface or additional game modes.

---

## 3. Easy and Hard Modes

### **Easy Mode**
In Easy Mode, the computer makes random moves by selecting from the available spaces on the board. This approach doesn't consider winning strategies or blocking the opponent, making the computer predictable and easier to beat.

#### **Logic**:
- Identify all empty cells on the board.
- Randomly choose one of these cells for the computer's move.

#### **Implementation**:
- The computer uses Python's `random.choice()` function to pick a move.
- The randomness ensures the computer's moves are not repetitive but also not strategic.

#### **Why Easy?**
- This mode doesn’t use any tactical logic, so it’s ideal for beginners or players who want a casual, relaxed game.

---

### **Hard Mode**
Hard Mode significantly increases the difficulty by implementing the **Minimax algorithm**, a decision-making algorithm often used in game theory and AI to find the optimal move. The computer now plays strategically to win or block the player from winning.

#### **How the Hard Mode Works:**
1. **Logic**:
   - The Minimax algorithm recursively evaluates all possible moves and their outcomes.
   - Assigns a score to each possible game state:
     - **+1**: If the computer wins.
     - **0**: If the game ends in a tie.
     - **-1**: If the player wins.
   - The computer selects the move that maximizes its chances of winning (or minimizes the player's chances of winning).

2. **Strategies Implemented**:
   I researched winning strategies for Tic Tac Toe online and implemented the Minimax algorithm to make the computer unbeatable in Hard mode. These strategies were adapted to suit the project and provide both a fun and challenging experience for players. These were the strategies that I found - 

   - **Win if possible**: The computer checks if there’s a move that leads directly to a win and prioritizes it.
   - **Block opponent’s win**: If the player is about to win, the computer blocks their move.
   - **Play for a tie**: In cases where neither side can win, the computer prioritizes moves that ensure a tie.
   - **Optimize long-term outcomes**: The Minimax algorithm ensures that the computer considers future moves, making it impossible to trick or outsmart in most cases.

---

### **Comparison Between Easy and Hard Modes**

| **Feature**             | **Easy Mode**            | **Hard Mode**           |
|--------------------------|--------------------------|--------------------------|
| **Move Selection**       | Random                  | Optimal (Minimax)        |
| **Win Prioritization**   | No                      | Yes                      |
| **Blocking Player’s Win**| No                      | Yes                      |
| **Long-Term Planning**   | No                      | Yes                      |
| **Difficulty Level**     | Beginner-Friendly       | Challenging              |

---

## 4. Planning and Design (4.1)

The project’s logic was planned and visualized using flowcharts and diagrams. These include:
- A flowchart for the game loop, detailing player turns, move validation, and game-end conditions.
- A decision tree outlining the computer's moves based on difficulty.
- Below you can see the flowchart that was made in the planning stage to plan out the functions.
![Flowchart](assets/images/flowchart.webp)

---

## 5. Validation and Testing (5.1, 5.2)

### Validation Fixes
Common validation issues addressed:
- Preventing players from selecting already occupied cells.
- Ensuring valid input (e.g., numbers between 1 and 3 for row and column).
- Fixing edge cases where Minimax logic caused errors.

### Manual Testing
The application was tested manually, including:
- Simulating all possible win conditions (rows, columns, diagonals).
- Testing tie conditions.
- Switching between game modes and difficulties.

PEP 8 validation was used to ensure compliance with Python’s coding standards.

**Placeholder Screenshot:**
![Testing Results](testing-results-placeholder.png)

---

## 6. Code Attribution (6.1)

All code was written from scratch except for references to:
- The Minimax algorithm, which was adapted from open-source resources and modified for this project.

These external sources were clearly separated and cited in the code comments.

---

## 7. Deployment Procedure (9.1)

### Steps to Deploy the Project to Heroku

1. **Push the Code to GitHub**:
   - Commit and push all changes to your GitHub repository:
     ```bash
     git add .
     git commit -m "Prepare for Heroku deployment"
     git push 
     ```
   
   **Placeholder Screenshot:**
   ![GitHub Repository](github-repository-placeholder.png)

2. **Create a Heroku App**:
   - Log in to your Heroku account and create a new app from the Heroku dashboard.
   - Choose a unique name for your app and select the appropriate region.
   
   **Placeholder Screenshot:**
   ![Heroku Dashboard](heroku-dashboard-placeholder.png)

3. **Deploy the App**:
   - Connect your Heroku app to your GitHub repository via the **Deployment Method** section.
   - Enable automatic or manual deployment from the desired branch (e.g., `main`).
   
   **Placeholder Screenshot:**
   ![Heroku Deployment](heroku-deployment-placeholder.png)

4. **Run the Application**:
   - After deployment, click **Open App** in the Heroku dashboard to run the application.
   
   **Placeholder Screenshot:**
   ![Running Application](running-application-placeholder.png)

5. **Live Link**:
   The live version of the application can be accessed at:  
   [**Tic Tac Toe on Heroku**](https://your-app-name.herokuapp.com)

---

## Conclusion
The Tic Tac Toe project showcases programming fundamentals, OOP principles, and a clean, modular code structure. Its simple yet effective design makes it both an educational tool and an entertaining application.

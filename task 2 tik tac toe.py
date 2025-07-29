# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def print_board():
    print()
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print()

# Function to check if a player has won
def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (draw)
def check_draw():
    return ' ' not in board

# Main game function
def play_game():
    current_player = 'X'
    
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'")
    print_board()

    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue
        
        board[move] = current_player
        print_board()

        if check_win(current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif check_draw():
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play_game()

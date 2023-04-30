# TICTACTOE GAME
#creating a board function for tictactoe
import random
def display_board(board): 
     print(" "+" "+" | "+" "+" | ")
     print(" "+ board[1] +" | "+ board[2] +" | "+ board[3])
     print(" "+" "+" | "+" "+" | ")
     print("-----------")
     print(" "+" "+" | "+" "+" | ")
     print(" "+ board[4] +" | "+ board[5] +" | " + board[6])
     print(" "+" "+" | "+" "+" | ")
     print("-----------")
     print(" "+" "+" | "+" "+" | ")
     print(" "+ board[7] +" | "+ board[8] +" | "+ board[9])
     print(" "+" "+" | "+" "+" | ")
    

# creating a function to set the user marker as "X" or "O"
def player_input():
    user_input=''
    while not (user_input== 'X' or user_input=='O'):
     user_input= input("Player 1: Do you want to be 'O' or 'X') ? ").upper()
    if user_input=='X':
       return('X','O')
    else:
       return ('O','X')

# creating a function that takes in the board list object, a marker and desired position
def place_marker(board,marker,position):
   board[position] = marker
   

# creating a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
   if (board[1]==board[2]==board[3]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark)or(board[4]==board[5]==board[6]==mark)or(board[7]==board[8]==board[9]==mark):
      return True

# creating a function that uses the random module to randomly decide which player goes first.You may want to lookup random.randint() Return a string of which player went first.

def choose_first():
   if random.randint(0,1)==0:
      return "Player 2"
   else:
      return "Player 1"
   
# creating a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board,position):
   return board[position]==' '
         

# Creaing a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1,10):
       if space_check(board,i):
          return False
   
    return True

# creating a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    next_position = 0
    
    while next_position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, next_position):
        next_position = int(input('Choose your next position: (1-9)'))
        
    return next_position

 
def replay():
       return input("Do you want to play again? Enter yes or no: ").lower().startswith('y')  


print("Welcome to Tic Tac Toe!")

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
    



   
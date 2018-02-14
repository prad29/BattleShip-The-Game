from random import randint

board = []   #creating an empty list

for x in range(0, 5):
  board.append(["O"]* 5)    #adding O's to evry row 5 times

def print_board(board):
  for row in board:
    print (" ".join(row))   #removing list methods so that the board list looks like an actual 5x5 squareboard, rather than a list

print_board(board)          #prints out the 5x5 squareboard onto the console

def random_row(board):
  return randint(0, len(board) - 1)       #getting a random number between including 0 and excluding 5, 
                                          #which will serve as our row index using the randint() function

def random_col(board):
  return randint(0, len(board[0]) - 1)             #getting a random number between including 0 and excluding 5, 
                                                   #which will serve as our column index using the randint() function

ship_row = random_row(board)
ship_col = random_col(board)



for turn in range(4):                              #prints "Turn" and "Turn number" onto the console and asks the user for his/her guess
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:               #If guesses right, console prints Congrats and breaks out the program
    print ("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or \                                   # This condition checks whether the user repeats his/her guess
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print ("You missed my battleship!")                            #When the user guesses wrong, the O on the board is replaced by an "X"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print ("Game Over")                                          #prints "Game Over" to the console at the end of 4 turns
    print_board(board)

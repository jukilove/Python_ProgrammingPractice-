import time;
import os;

print('Hi, welcome to my tic tac toe game I made in python! Hope you enjoy!')

def checkwin(player):
	# loop through the rows and columns
	for c in range(0,3):
		# check for horizontal line win
		if board[c][0] == player and board[c][1] == player and board[c][2] == player:
			print ("**************\n\n%s wins\n\n**************" % player)
			playerwin = True
			return playerwin
		# check for vertical line win
		elif board[0][c] == player and board[1][c] == player and board[2][c] == player:
			print ("**************\n\n%s wins\n\n**************" % player)
			playerwin = True
			return playerwin
		# check for a diagonal win [left to right]
		elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
			print ("**************\n\n%s wins\n\n**************" % player)
			playerwin = True
			return playerwin
		# check for diagonal win [right to left]
		elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
			print ("**************\n\n%s wins\n\n**************" % player)
			playerwin = True
			return playerwin
	else:
		playerwin = False
		return playerwin
		
# code for the players turn
def playerturn(player):
	print ("%s's turn" % player)
	turn = 1
	while(turn):
		try:
			print ("Select column [1-3]: ",)
			col = int(input()) - 1
			print ("Select row [1-3]: ",)
			row = int(input()) - 1
			if board[row][col] == 'X' or board[row][col] == 'O':
				print ("Already taken! Sorry.")
			else:
				board[row][col] = player
				turn = 0
			os.system('cls')
			print('Hi, welcome to my tic tac toe game I made in python! Hope you enjoy!')
		except IndexError:
			print ("Oops! That was too big or to small, sorry. Try again...")
		except ValueError:
			print ("Oops! That was an invalid number, sorry. Try again...")

# print an empty board
def printboard():
	print (board[0])
	print (board[1])
	print (board[2])

# initialise an empty board
board = [['-','-','-'],['-','-','-'],['-','-','-']]
player1 = 'X'
player2 = 'O'
win = False
turns = 0
printboard()

# game loop
# print empty board to start program
while(win == False):
	playerturn(player1)
	turns +=1
	printboard()
	if checkwin(player1) == True: break
	if turns == 9:
		print ("This game has come to a tie, bad luck!")
		break

	playerturn(player2)
	turns += 1
	printboard()
	checkwin(player2)
	if checkwin(player2) == True: break

time.sleep(10)

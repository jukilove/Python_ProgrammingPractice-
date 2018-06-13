#Using Data Structures to Model Real-World Things.
#A Tic-Tac-Toe Board
#To move, the Tic-Tac-Toe Board space are called:
#top-L | top-M | top-R
#------+-------+------
#mid-L | mid-M | mid-R
#------+-------+------
#low-L | low-M | low-R

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
           
def printTTTBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def introTTTBoard():
    print('Welcome to Python Tic-Tac-Toe Board.\nHere are some few instructions to the game.')
    print('- The board is display as')
    printTTTBoard(theBoard)
    print('- There are nine space that can each contain an X, an O, or a blank.')
    print('- To move on which space, use these keys word: \n' +
          'top-L | top-M | top-R \n' + '------+-------+------\n' +
          'mid-L | mid-M | mid-R \n' + '------+-------+------\n' +
          'low-L | low-M | low-R \n' + '######################################')
    
introTTTBoard()

userTurn = 'X'

for i in range(9):
    printTTTBoard(theBoard)
    print('Turn for ' + userTurn + '. Move on which space?')
    move = input()
    theBoard[move] = userTurn
    if userTurn == 'X':
        print('```````````````````````````````````````````````')
        print('- To move on which space, use these keys word: \n' +
          'top-L | top-M | top-R \n' + '------+-------+------\n' +
          'mid-L | mid-M | mid-R \n' + '------+-------+------\n' +
          'low-L | low-M | low-R \n' + '```````````````````````````````````````````````')
        userTurn = 'O'
    else:
        print('```````````````````````````````````````````````')
        print('- To move on which space, use these keys word: \n' +
          'top-L | top-M | top-R \n' + '------+-------+------\n' +
          'mid-L | mid-M | mid-R \n' + '------+-------+------\n' +
          'low-L | low-M | low-R \n' + '```````````````````````````````````````````````')
        userTurn = 'X'
        
printTTTBoard(theBoard)

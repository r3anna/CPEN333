# student name: Reanna Wong
# student number: 98717846

"""

Hi! This is my first time coding in python, my apologies in advance if my work is not the best. I'm learning!(:

"""

# A command-line 2048 game

import random

board: list[list] = []  # a 2-D list to keep the current status of the game board

def init() -> None:  # Use as is
    """ 
        initializes the board variable
        and prints a welcome message
    """
    # initialize the board cells with ''
    for _ in range(4):     
        rowList = []
        for _ in range(4):
            rowList.append('')
        board.append(rowList)
    # add two starting 2's at random cells
    twoRandomNumbers = random.sample(range(16), 2)   # randomly choose two numbers between 0 and 15   
    # correspond each of the two random numbers to the corresponding cell
    twoRandomCells = ((twoRandomNumbers[0]//4,twoRandomNumbers[0]%4),
                      (twoRandomNumbers[1]//4,twoRandomNumbers[1]%4))
    #for cell in twoRandomCells:  # put a 2 on each of the two chosen random cells
     #   board[cell[0]][cell[1]] = 2
    
    
    ## FOR TEST PURPOSES ##
   
    # board[0][0] = 2
    # board[0][1] = 2
    # board[0][2] = 2
    # board[0][3] = 2
    board[1][0] = 2  
    board[1][1] = 2  
    board[1][2] = 2  
    board[1][3] = 2
    board[2][0] = 4
    board[2][1] = 4
    board[2][2] = 4
    board[2][3] = 4
    board[3][0] = 4
    board[3][1] = 4
    board[3][2] = 4
    board[3][3] = 4
    



    print(); print("Welcome! Let's play the 2048 game."); print()


def displayGame() -> None:  # Use as is
    """ displays the current board on the console """
    print("+-----+-----+-----+-----+")
    for row in range(4): 
        for column in range(4):
            cell = board[row][column] 
            print(f"|{str(cell).center(5)}", end="")
        print("|")
        print("+-----+-----+-----+-----+")


def promptGamerForTheNextMove() -> str: # Use as is
    """
        prompts the gamer until a valid next move or Q (to quit) is selected
        (valid move direction: one of 'W', 'A', 'S' or 'D')
        returns the user input
    """
    print("Enter one of WASD (move direction) or Q (to quit)")
    while True:  # prompt until a valid input is entered
        move = input('> ').upper()
        if move in ('W', 'A', 'S', 'D', 'Q'): # a valid move direction or 'Q'
            break
        print('Enter one of "W", "A", "S", "D", or "Q"') # otherwise inform the user about valid input
    return move

def addANewTwoToBoard() -> None:
    """ 
        adds a new 2 at an available randomly-selected cell of the board
    """
    pass #to implement


def isFull() -> bool:
    """ 
        returns True if no empty cell is left, False otherwise 
    """
    pass #to implement


def getCurrentScore() -> int:
    """ 
        calculates and returns the current score
        the score is the sum of all the numbers currently on the board
    """
    pass #to implement





def updateTheBoardBasedOnTheUserMove(move: str) -> None:
    """
        updates the board variable based on the move argument by sliding and merging
        the move argument is either 'W', 'A', 'S', or 'D'
        directions: W for up; A for left; S for down, and D for right
    """
    #my starting point
    Merge(move)
        
        #moving left or up, i want to make sure that all the tiles from left to right, top to bottom get shifted first
    if (move == "W" or move == "A"):
         for row in range(4): 
            for col in range(4): 
                if str(board[row][col]).isnumeric():
                   
                    Shift(move, row, col) 
                    

        # moving down or right, i want to make sure all tiles from right to left, bottom to topget shifted first  
    if (move == "S" or move == "D"):
        for row in range(3, -1, -1):
            for col in range(3, -1, -1):
                if str(board[row][col]).isnumeric():
                   
                    Shift(move, row, col)

            
 
    

    pass #to implement

#up to two new functions allowed to be added (if needed)
#as usual, they must be documented well
#they have to be placed below this line

"""

figure out how to merge a tile if there are multiple blank spaces

"""

def Merge(move: str) -> None:
    match move:
        case "W":

            #board[row][column] will be compared to the 'NextTile'
            for column in range(0, 4, 1):
                for row in range(0, 4, 1):

                    #if it is empty go to the next row!
                    if (board[row][column] == ''):
                        #continue skips the code below and goes back to the for row loop
                        continue

                    NextTile = row + 1

                    while NextTile < 4:
                
                        #if the next tile below is the same add them together and end the while loop
                        if (board[row][column] == board[NextTile][column]):
                            board[row][column] *= 2
                            board[NextTile][column] = ''
                            break
                        
                        #move to the next tile to check
                        NextTile+=1
        case "D":

            #board[row][column] will be compared to the 'NextTile'
            for column in range(0, 4, 1):
                for row in range(0, 4, 1):

                    #if it is empty go to the next row!
                    if (board[row][column] == ''):
                        #continue skips the code below and goes back to the for row loop
                        continue

                    NextTile = row + 1

                    while NextTile < 4:
                
                        #if the next tile below is the same add them together and end the while loop
                        if (board[row][column] == board[NextTile][column]):
                            board[row][column] *= 2
                            board[NextTile][column] = ''
                            break
                        
                        #move to the next tile to check
                        NextTile+=1




                        
                            
                        
                            

                        

                
                        
                    

                    
                
    # match move:
    #     case "W":
    #         if (board[row+1][column] == board[row][column]):
    #             board[row][column] *= 2
    #             board[row+1][column] = ''
    #     case "A":
    #         if board[row][column+1] == board[row][column]:
    #             board[row][column] *= 2
    #             board[row][column+1] = ''
    #     case "S":
    #         if board[row-1][column] == board[row][column]:
    #             board[row][column] *= 2
    #             board[row-1][column] = ''

    #     case "D":
    #         if board[row][column-1] == board[row][column]:
    #             board[row][column] *= 2
    #             board[row][column-1] = ''

def Shift(move: str, row: int, column: int) -> None: 
    # find out if box is empty
    OGnum = board[row][column]
    match move:
            case "W":
                #row only changes shift up
                for i in range (row-1,-1,-1):
                    

                    # checks if the tile above has nothing, and if there is nothing it shifts up
                    if board[i][column] == '':
                        board[i][column] = OGnum
                        board[i+1][column] = ''
                        
            
            case "A":
                #column only changes shift left
                for i in range (column-1,-1,-1):
                    if board[row][i] == '':
                        board[row][i] = OGnum
                        board[row][i+1] = ''
                    

            case "S":
                #row only changes shift down
                for i in range (row+1,4,1):
                    if board[i][column] == '':
                        board[i][column] = OGnum
                        board[i-1][column] = ''
                   

            case "D":
                #column only changes shift right
                for i in range (column+1,4,1):
                    if board[row][i] == '':
                        board[row][i] = OGnum
                        board[row][i-1] = ''
                                   
            case default:
             print ("ERROR: Invalid Input, Try Again.")

   


if __name__ == "__main__":  # Use as is  
    init()
    displayGame()
    while True:  # Super-loop for the game
        print(f"Score: {getCurrentScore()}")
        userInput = promptGamerForTheNextMove()
        if(userInput == 'Q'):
            print("Exiting the game. Thanks for playing!")
            break
        updateTheBoardBasedOnTheUserMove(userInput)
        addANewTwoToBoard()
        displayGame()

        if isFull(): #game is over once all cells are taken
            print("Game is Over. Check out your score.")
            print("Thanks for playing!")
            break
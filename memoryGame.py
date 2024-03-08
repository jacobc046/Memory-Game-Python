import random

def createBoard(): #create the board of random numbers
    numList = []
    while len(numList) != 16: #while the list does not have 16 numbers...
        randNum = random.randint(1,8) #create random number 1-8

        #if there is less than 2 of the number already in the list...
        if numList.count(randNum) < 2: 
            numList.append(randNum) #add the random number to the list

    global board #declare board as global variable
    board = []
    for i in range(16): #run 16 times...
        #declare row list as empty every 4 iterations starting at i = 0 
        if i % 4 == 0: 
            row = []
        #add the number in the random number list at index i to the row
        row.append(numList[i]) 

        if i in range(3,16,4): #if is 3, 7, 11, 15....
            board.append(row) #add the row list to the board list
    
    #defines the completed board. Board is updated as user finds matches
    global completedBoard 
    completedBoard = [["*","*","*","*"],
                      ["*","*","*","*"],
                      ["*","*","*","*"],
                      ["*","*","*","*"]]

    
def cardLocation(): #get user input for the location of both cards
    position1List,position2List = [-1,-1],[-1,-1] #define lists of each card's positions

    while True: #always enter loop...
        #get user input for first position
        position1 = input("Enter the row (1-4) and column (1-4) of the first number: ").split()
        position1List = checkCard(position1) #check card 1 position is valid

        #display card face up on board to user
        print("\nShowing first card on board")
        showBoard(position1List)
        
        #get user input for position 2
        position2 = input("Enter the row (1-4) and column (1-4) of the second number: ").split()
        position2List = checkCard(position2) #check if card 2 position is valid

        #if the user enters the same position for both cards...
        if position2List == position1List: 
            print("You entered the same location for each card. Please try again.\n")
            continue #skip the rest of the loop and get user input again

        #display both cards face up on board
        print("\nShowing both cards on board")
        showBoard(position1List,position2List)
        break #stop the loop from repeating

    return position1List, position2List


def checkCard(position): #check if card position is valid
    #define row and column from position list input
    row,column = int(position[0])-1,int(position[1])-1 

    #while the row or column index is not 0-4...
    while row not in range(4) or column not in range(4):
        #display error statement to user and get user input again
        print("Invalid input, try again.\n")
        position = input("Enter the row (1-4) and column (1-4) of the first number: ").split()
    
        #redefine row and column based on new user input
        row = int(position[0])-1
        column = int(position[1])-1

    #while card has already been displayed face up FROM PREVOUS TURNS ONLY...
    while board[row][column] == completedBoard[row][column]:
        #display error message to user and get input again
        print("Card already face up, please enter another selection.\n")
        position = input("Enter the row (1-4) and column (1-4) of the first number: ").split()
        
        #redefine row and column based on new input
        row = int(position[0])-1
        column = int(position[1])-1
        
        #check again to make sure the card index is not out of range
        while row not in range(4) or column not in range(4):
            print("Invalid input, try again.")
            position = input("Enter the row (1-4) and column (1-4) of the first number: ").split()
        
            row = int(position[0])-1
            column = int(position[1])-1

    return [row,column]


def showBoard(position1List,position2List = [-1,-1]): #display board to user
    #create row and column variables for each card based on list input
    card1Row = position1List[0]
    card1Column = position1List[1]
    card2Row = position2List[0]
    card2Column = position2List[1]

    #for each item in the array...
    for row in range(4):
        for column in range(4):
            #if completed board at item index is not a face down card (show all face-up cards from previous turns)...
            if completedBoard[row][column] != "*":
                print(board[row][column],end = " ") #display face-up card
            #if the loop index == card 1 index or loop index == card 2 index (display all cards in current turn to user)...
            elif [row, column] == [card1Row, card1Column] or [row,column] == [card2Row,card2Column]:
                print(board[row][column],end = " ") #display card face-up
            else: #if the loop index does not match the index of the user-entered cards nor matches a card already revealed...
                print("*",end = " ") #display a face-down card
        print() #create a new line


def playGame(): #run game
    runGame = True
    pos1List = [-1,-1]
    pos2List = [-1,-1]

    while runGame:
        #show board to user
        print("Showing current board")
        showBoard(pos1List,pos2List)

        #get positions of cards
        positions = cardLocation()

        #from position list, define row and column variables for both cards
        c1Row = positions[0][0]
        c1Column = positions[0][1]
        c2Row = positions[1][0]
        c2Column = positions[1][1]

        #if both the cards at user-entered index are the same (cards match)...
        if board[c1Row][c1Column] == board[c2Row][c2Column]:
            #display turn result
            print("Nice match!") 

            #replace the face-down cards of the completed board with the matched cards
            completedBoard[c1Row][c1Column] = board[c1Row][c1Column]
            completedBoard[c2Row][c2Column] = board[c2Row][c2Column]
        else: #not a match
            print("Pairs do not match, try again!")
        print() #create new line

        #if the board is completely filled in (all matches have been found)...
        if completedBoard == board: 
            runGame = False #stop the game

            #display win status to user
            print("Congratulations, you found all the pairs!")
            print("Thanks for playing.")
        

def main(): #run function to create the board then run the game
    createBoard()
    playGame()

main() #run main code
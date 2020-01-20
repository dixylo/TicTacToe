# Assignment 2: Tic-Tac-Toe
# Author: Lin, Xiaofeng
# ID: 1487467


# This function prints the board.
def printBoard(moves):
    print("       1   2   3\n     +---+---+---+\n   1 |",
            moves[0], "|", moves[1], "|", moves[2], "|\n     +---+---+---+\n   2 |",
            moves[3], "|", moves[4], "|", moves[5], "|\n     +---+---+---+\n   3 |",
            moves[6], "|", moves[7], "|", moves[8], "|\n     +---+---+---+")

# This function determines which player wins.
def checkWin(moves, player):
    if moves[0] == player and moves[1] == player and moves[2] == player:
        winner = player
    elif moves[3] == player and moves[4] == player and moves[5] == player:
        winner = player
    elif moves[6] == player and moves[7] == player and moves[8] == player:
        winner = player
    elif moves[0] == player and moves[3] == player and moves[6] == player:
        winner = player
    elif moves[1] == player and moves[4] == player and moves[7] == player:
        winner = player
    elif moves[2] == player and moves[5] == player and moves[8] == player:
        winner = player
    elif moves[0] == player and moves[4] == player and moves[8] == player:
        winner = player
    elif moves[2] == player and moves[4] == player and moves[6] == player:
        winner = player
    else:
        winner = ""
    return winner

# This block initialises the game.
moves = [" "] * 9 # List that contains the status of each position of the board.
marks = "OX"
print("Welcome to Tic Tac Toe! Below is the board with each row and column numbered.")
printBoard(moves)
print("Enter the row and column numbers of the position where you'd like to place your mark.\nFor example, enter 23 if you want to place your mark in Row 2, Column 3.")
validCoordinates = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]

playMore = "y"
while playMore.lower() == "y":
    moves = [" "] * 9 # List that contains the status of each position of the board.
    # This block asks for the number of players, which determines if the game is between two humans or between a human and a computer.
    numPlayer = input("How many players are playing the game? ")
    while numPlayer not in "12":
        numPlayer = input("This game needs one or two players. Please input '1' or '2': ")
    
    # This block runs a game between two humans.
    if numPlayer == "2":
        print("Please decide who is X. X always moves first.")
        i = 1
        while i <= 9:
            player = marks[i % 2]
            # This block asks for the coordinates of a move and prevents an invalid input.
            validMove = False    
            while not validMove:
                # This block prevents an input that is not a pair of coordinates.
                newMove = input("\n\nNow it's " + player + "'s turn: ")
                while newMove not in validCoordinates:
                    newMove = input("Please enter a valid coordinate consisting of only Digits 1, 2 and 3, like 23 or 33. ")
                    
                row = int(newMove[0])
                col = int(newMove[1])
                # This block gets the coordinates and converts them into the index of List moves by the mapping formula "3*row+col-4".
                # It also gives a warning if the move is invalid.
                if moves[3 * row + col - 4] == " ":
                    moves[3 * row + col - 4] = player
                    validMove = True
                else:
                    print("You CANNOT place a mark in an occupied position! Please re-enter.")
                
            printBoard(moves)
            # This block determines the winner.
            if i >= 5:
                winner = checkWin(moves, player)
                if winner != "":
                    print("\n\nPlayer", winner, "Wins!")
                    break
            # This block announces it is a tie if no one wins or loses.  
            if i == 9:
                print("\n\nDRAW!")
                
            i += 1
    
    # This block runs a game between a human and a dumbbot.
    else:
        import random
        print("Now you are going to play against a dumbbot.")
        level = input("Please choose a difficulty level. Enter 'E' for Easy or 'H' for Hard. ")
        while level.upper() not in "EH":
            level = input("Only 'E' or 'H' is allowed, case insensitive. Please re-enter: ")
        level = level.upper()
        human = input("Would you like to play X or O? (X always moves first.): ")
        while human.upper() not in "XO":
            human = input("Only 'X' or 'O' is allowed, case insensitive. Please re-enter: ")
        human = human.upper()
        
        leftPos = [i for i in range(9)] # List that contains the index of unoccupied positions.
        i = 1
        while i <= 9:
            player = marks[i % 2]
            opponent = marks[(i + 1) % 2]
            # This block allows a human to make a move.
            if player == human:    
                # This block asks for the coordinates of a move and prevents an invalid input.
                validMove = False    
                while not validMove:
                    # This block prevents an input that is not a pair of coordinates.
                    newMove = input("\n\nNow it's your turn: ")
                    while newMove not in validCoordinates:
                        newMove = input("Please enter a valid coordinate consisting of only Digits 1, 2 and 3, like 23 or 33. ") 
        
                    row = int(newMove[0])
                    col = int(newMove[1])
                    moveIndex = 3 * row + col - 4
                    # This block gets the coordinates and converts them into the index of List moves by the mapping formula "3*row+col-4".
                    # It also gives a warning if the move is invalid.
                    if moves[moveIndex] == " ":
                        moves[moveIndex] = player
                        leftPos.remove(moveIndex)
                        validMove = True
                    else:
                        print("You CANNOT place a mark in an occupied position! Please re-enter.")
            # This block instructs the computer to make a move.
            else:
                # This block instructs the computer to make a random move if the difficulty level is easy or when it is too early for anyone to win.
                if level == "E" or i < 4:
                    botMove = leftPos[random.randint(0, len(leftPos)-1)]
                    if human == "X":
                        moves[botMove] = "O"
                    else:
                        moves[botMove] = "X"
                    leftPos.remove(botMove)
                # This block instructs the computer to make a reasonable move if the difficulty level is hard and when it is possible for either side to win.
                else:
                    won = False
                    blockedOppo = False
                    # This block is used for the bot to find the right move to win the game.
                    for element in leftPos:
                        mockMoves = list(moves)
                        mockMoves[element] = player 
                        if checkWin(mockMoves, player) != "":
                            moves[element] = player
                            leftPos.remove(element)
                            won = True
                            break
                    # This block is used for the bot to find the right move to prevent the human from winning the game.
                    if not won:
                        for element in leftPos:
                            mockMoves = list(moves)
                            mockMoves[element] = opponent 
                            if checkWin(mockMoves, opponent) != "":
                                moves[element] = player
                                leftPos.remove(element)
                                blockedOppo = True
                                break
                    # This block instructs the bot to make a random move if neither side is winning.
                    if not won and not blockedOppo:
                        botMove = leftPos[random.randint(0, len(leftPos)-1)]
                        if human == "X":
                            moves[botMove] = "O"
                        else:
                            moves[botMove] = "X"
                        leftPos.remove(botMove)
                            
                print("\n\nDumbbot has made a move.")
                
            printBoard(moves)
            # This block determines the winner.
            if i >= 5:
                winner = checkWin(moves, player)
                if winner != "":
                    if human == winner:
                        print("\n\nYou Win! You are smarter than a dumbbot!")
                    else:
                        print("\n\nYou Lose! Humans are proud of you!")
                    break
            # This block announces it is a tie if no one wins or loses.  
            if i == 9:
                print("\n\nGood Job! You are as smart as a dumbbot!")
                
            i += 1
    
    playMore = input("\n\nWanna play again? (y/n): ")
    while playMore not in "ynYN":
        playMore = input("Please enter only 'y' for yes or 'n' for no, case insensitive. ")
    

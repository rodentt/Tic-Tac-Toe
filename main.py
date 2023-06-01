from classes.game import Game
from classes.menu import Menu
from exceptions.invalidMoveError import InvalidMoveError

# starts game
startGame = True
while startGame:

    # creates a game and menu
    game = Game()
    gameMenu = Menu()
    continueGame = True

    # welcomes user with instructions and prompt
    gameMenu.welcomeUser()
    
    # starts the tic-tac-toe game
    while continueGame:

        # gets the position to place the next piece
        position = gameMenu.getMove()

        # tries to place piece
        try:
            # moves piece, displays board and ends game if necessary
            gameCondition = game.takeTurn(position)
            boardStr = game.getBoard()
            gameMenu.displayBoard(boardStr)
            continueGame = gameMenu.displayOutcome(gameCondition)
        
        # tells user why move was invalid and tries to prompt user for move again
        except InvalidMoveError:
            gameMenu.displayMoveError(InvalidMoveError.getMessage())
            continue
    
    # after ending the game offer a new game
    # if accepted, a new game starts
    startGame = gameMenu.offerNewGame()



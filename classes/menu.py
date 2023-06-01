from classes.board import Board

class Menu:
    """
    Game menu which displays prompts and gets user input.

    Methods:
        welcomeUser(): Welcomes user and gives game instructions. 
        getMove(): Gets move from user.
        displayBoard(str): Prints given tic-tac-toe board.
        displayMoveError(str): Prints given move error message.
        displayOutcome(str): Displays the game outcome if it's ended.
        offerNewGame(): Prints a prompt offering a new game to user and gets response.
    """    
    
    def __init__(self):
        self._referenceBoard = Board()
        for i in range(1, 10):
            self._referenceBoard.replacePiece(str(i), i)
            
    def welcomeUser(self):
        """ Welcomes user and gives game instructions. """        
        print("Welcome to console line tic-tac-toe!")
        print("When you place a piece, use the following board as a reference for piece positions:")
        print(self._referenceBoard)
        
    def getMove(self):
        """ 
        Gets move from user. 

        Returns:
            int: a position to place a piece on the board
        """  
        validInput = False
        position = None
        while not validInput:
            try:
                position = input("Enter position for your piece: ")
                position = int(position)
                break
            except:
                print("Given position is not an integer")
                continue
        
        return position

    def displayBoard(self, board):
        """
        Prints given tic-tac-toe board.

        Args:
            board (str): string representation of board to print
        """
        print(board)

    def displayMoveError(self, message):
        """
        Prints given move error message.

        Args:
            message (str): move error message
        """
        print(message)

    def displayOutcome(self, gameCondition):
        """
        Determines whether the game has ended 
        and displays a corresponding message if so.
        
        Args:
            gameCondition (str): the current game condition (win, draw, continue)
        
        Returns:
            (bool): whether the game has ended or not
        """
        pass

    def offerNewGame(self):
        """
        Prints a prompt offering a new game to user and gets response.

        Returns:
            (bool): whether a new game should start
        """
        pass
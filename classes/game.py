from classes.board import Board
from enum import Enum
from exceptions.invalidMoveError import InvalidMoveError

class TurnColor(Enum):
    """An enumeration of the two turn colors."""    
    WHITE = 1
    BLACK = 2

    def __str__(self):   
        return self.name.lower()

class GameOutcome(Enum):
    """An enumeration of the current game outcome."""
    WHITEWINS = 1
    BLACKWINS = 2
    DRAW = 3
    CONTINUE = 4

    def __str__(self):   
        return self.name.lower()

class Game:
    """
    This class represents a game of tic-tac-toe

    Methods:
        takeTurn(int): Adds a piece to the board at the given position
        getTurn(): Retrieves turn color
        getBoard(): Retrieves board
        getNumPieces(): Retrieves number of pieces on board
    """    

    def __init__(self):
        """
        The constructor for the Game class.
        Initializes a board and initial turn color.
        """        
        self._gameBoard = Board()
        self._turn = TurnColor.WHITE
        self._numPieces = 0
    
    def _toggleTurn(self):
        """
        Toggles turn color (from white to black and vice-versa)
        """
        if self._turn == TurnColor.WHITE:
            self._turn = TurnColor.BLACK 
        else:
            self._turn = TurnColor.WHITE
    
    def getTurn(self):
        """
        Returns current turn color 

        Returns:
            str: string representation of current turn
        """        
        return str(self._turn)
    
    def getBoard(self):
        """
        Returns board string representation

        Returns:
            str: string representation of current board
        """
        return str(self._gameBoard)
    
    def getNumPieces(self):
        """
        Returns number of pieces on board

        Returns: 
            int: number of pieces on board
        """
        return self._numPieces
    
    def _continueGame(self):
        """
        Checks whether the game should continue or not.

        Returns:
            str: string representation of game condition (win, draw, to continue)
        """

        def checkForWin():
            """
            Checks if white or black won the tic-tac-toe game

            Returns:
                enum: Returns a game outcome specifying a winner if applicable 
            """

            # helper function that determines if white or black won in case of a victory
            getWinner = lambda piece: GameOutcome.WHITEWINS if piece == "O" else GameOutcome.BLACKWINS

            # checks for win along rows and columns
            rowPositions = [1, 2, 3]
            colPositions = [1, 4, 7]
            for i in range(0, 3):
                if (self._gameBoard).checkPositions(rowPositions):
                    return getWinner((self._gameBoard)[rowPositions[0]])
                elif (self._gameBoard).checkPositions(colPositions):
                    return getWinner((self._gameBoard)[colPositions[0]])
                
                # changes the row/col to check next
                rowPositions = [x + 3 for x in rowPositions]
                colPositions = [x + 1 for x in colPositions]
            
            # checks for win along diagonals
            if (self._gameBoard).checkPositions([1, 5, 9]):
                return getWinner((self._gameBoard)[1])
            elif (self._gameBoard).checkPositions([3, 5, 7]):
                return getWinner((self._gameBoard)[3])
            else:
                return GameOutcome.CONTINUE
 
        # check for a win along all possible diagonals, columns and rows
        gameCondition = checkForWin()

        # if there's been no win after all pieces are placed, there's a draw
        if self._numPieces == 9:
            gameCondition = GameOutcome.DRAW
        
        return str(gameCondition)

    def takeTurn(self, position):
        """
        Adds a piece at the given position, if possible, 
        and checks if the game has ended or should continue.

        Exceptions:
            InvalidMoveError: raised if the given move is invalid

        Args:
            position (int): denotes the position on the board to add a piece

        Returns:
            str: string represntation of game condition (to continue or end game)
        """

        # tries to add piece to board 
        (self._gameBoard).addPiece(self.getTurn(), position)
        self._numPieces += 1

        # changes turn
        self._toggleTurn()

        # returns the game condition
        return self._continueGame()
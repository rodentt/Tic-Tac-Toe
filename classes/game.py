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
    """    

    def __init__(self):
        """
        The constructor for the Game class.
        Initializes a board and initial turn color.
        """        
        self._gameBoard = Board(self)
        self._turn = TurnColor.WHITE
    
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
    
    def _continueGame(self):
        """
        Checks whether the game should continue or not.

        Returns:
            str: string representation of game condition (win, draw, to continue)
        """
        pass

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

        # changes turn
        self._toggleTurn()

        # returns the game condition
        return self._continueGame()
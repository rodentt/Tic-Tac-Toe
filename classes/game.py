from classes.board import Board
from enum import Enum

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
        add_piece(int): Adds a piece to the board at the given position
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
    
    def _continueGame(self):
        """
        Checks whether the game should continue or not.

        Returns:
            str: string representation of game condition (win, draw, to continue)
        """
        pass

    def addPiece(self, position):
        """
        Adds a piece to the board at the given positions

        Args:
            position (int): denotes the position on the board to add a piece

        Returns:
            str: string represntation of game condition (to continue or end game)
        """
        pass

    
        
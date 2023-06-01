from exceptions.invalidMoveError import InvalidMoveError

class Board:
    """
    This class represents a game board for tic-tac-toe

    Methods:
        addPiece(str, int): Adds a piece to the board at the given position
    """
    def __init__(self):
        """
        Constructor for the Board class
        """
        self._board = [None] * 9

    def __str__(self):
        """
        Prints the board and pieces
        """
        pass

    def addPiece(self, color, position):
        """
        Adds a piece to the board at the given positions

        Exceptions:
            InvalidMoveError: raised if the given position already has a 
            piece on it or is invalid

        Args:
            color (str): denotes the color of the piece to add
            position (int): denotes the position on the board to add a piece
        """
        
        # checks if given position is in range
        if position > 9 or position < 1:
            raise InvalidMoveError("Given position is not in range (1 - 9)")
        
        # checks that the position on the board is open
        if self._board[position - 1] != None:
            raise InvalidMoveError("Position already has a piece on it")
        
        # place a piece on the board
        piece = "X" if color == "black" else "O" 
        self._board[position - 1] = piece


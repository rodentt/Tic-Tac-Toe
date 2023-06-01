from exceptions.invalidMoveError import InvalidMoveError

class Board:
    """
    This class represents a game board for tic-tac-toe

    Methods:
        addPiece(str, int): Adds a piece to the board at the given position
        replacePiece(str, int): Adds a piece at the given position, replacing any if necessary.
    """
    def __init__(self):
        """
        Constructor for the Board class
        """
        self._board = [" "] * 9

    def __str__(self):
        """
        Converts the board to a string representation
        """
        boardStr = []
        rowDivider = "+-----+-----+-----+"
        currPosition = 1

        def getRow():
            """Generates a tic-tac-toe row's string representation."""

            # adds row character by character to string list
            # either adds column divider, space or piece on board
            nonlocal currPosition
            rowStr = []
            for i in range(0, 19):
                match i % 6:
                    case 0:
                        rowStr.append("|")
                    case 3:
                        rowStr.append(self._board[currPosition - 1])
                        currPosition += 1
                    case _:
                        rowStr.append(" ")
            
            # joins list and creates row representation
            return "".join(rowStr)

        # generates the 7 tic-tac-toe board as a string
        # either places the row divider or actual row with X, Os in a list
        for i in range(0, 7):
            if i % 2 == 0:
                boardStr.append(rowDivider)
            else:
                boardStr.append(getRow())
        
        # joins row list and creates board representation
        return "\n".join(boardStr)
    
    def replacePiece(self, piece, position):
        """
        Adds a piece at the given position, replacing any if necessary.

        Args:
            piece (str): piece to place
            position (int): position to place piece
        """
        self._board[position - 1] = piece

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
        if self._board[position - 1] != " ":
            raise InvalidMoveError("Position already has a piece on it")
        
        # place a piece on the board
        piece = "X" if color == "black" else "O" 
        self._board[position - 1] = piece


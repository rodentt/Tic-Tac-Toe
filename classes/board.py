from exceptions.invalidMoveError import InvalidMoveError

class Board:
    """
    This class represents a game board for tic-tac-toe

    Methods:
        addPiece(str, int): Adds a piece to the board at the given position.
        replacePiece(str, int): Adds a piece at the given position, replacing any if necessary.
        checkPositions(list): Checks if the given positions have the same piece, excluding blank spots.
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
    
    def __getitem__(self, index):
        """
        Retrieves piece at the given position.

        Pre:
            Given index is valid (between 1 - 9)

        Args:
            index (int): position of piece to retrieve

        Returns:
            str: piece at given position
        """
        return (self._board)[index - 1]
    
    def checkPositions(self, positions):
        """
        Checks if the given positions have the same piece, excluding blank spots.

        Pre:
            given positions list must contain at least one element, all integers between 1 - 9

        Args:
            positions (list): list of the positions to check

        Returns:
            bool: True if the pieces at the positions match, false otherwise
        """

        # gets first piece to compare all others with
        piece = self._board[positions[0] - 1]

        # iterates over all the pieces referenced in the positions list
        # compares them with the initial piece to check if they all match up
        for i in positions:
            current_piece = self._board[i - 1]
            if current_piece == " " or current_piece != piece:
                return False
        
        return True

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


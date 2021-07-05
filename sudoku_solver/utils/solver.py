

class Solver:
    def __init__(self):
        self.board = [[0 for i in range(9)] for j in range(9)]

    # OBS!
    # This function never reaches a return statement if the last
    # number is already set
    def solve(self, row=0, col=0):
        """Recursive function that solves any sudoku puzzle using recursion

        Args:
            row (int, optional): Starting row. Defaults to 0.
            col (int, optional): Starting column. Defaults to 0.

        Returns:
            func: The solve function, since it uses recursison
        """
        next_row, next_col = self.next_coord(row, col)
        if self.board[row][col] == 0:
            for number in range(1, 10):  # Loop through all possible numbers
                if self.is_valid(row, col, number):
                    self.board[row][col] = number
                    if next_row == -1 and next_col == -1:
                        return True
                    if not self.solve(next_row, next_col):
                        self.board[row][col] = 0
                    else:
                        return True
        elif not(next_row == -1 and next_col == -1):
            return self.solve(next_row, next_col)

    def solve2(self, row=0, col=0):


        # When the end is reached
        if row>=9:
            return True

        next_row, next_col = self.next_coord(row, col)

        # A value needs to be set
        if self.board[row][col] == 0:
            for number in range(1, 10): # Loop through all possible numbers
                if self.is_valid(row, col, number):
                    self.board[row][col] = number
                    if self.solve2(next_row, next_col):
                        return True
                self.board[row][col] = 0
            return False

        return self.solve2(next_row, next_col)


    def next_coord(self, row, col):
        """Returns the next coordinate to check

        Args:
            row (int): The last checked row
            col (int): The last checked column

        Returns:
            int, int: The next row and col to check
        """
        next_row = row
        next_col = col + 1

        if next_col >= 9:
            next_col = 0
            next_row += 1

        return next_row, next_col

    def is_valid(self, row, col, number):
        """Check whether a number is valid in it's current spot

        Args:
            row (int): The row to check
            col (int): The column to check
            n (int): The number to check

        Returns:
            boolean: Whether the number is valid in the coordinate
        """
        return not (self.in_square(self.get_square(row, col), number) or
                    self.in_row(row, number) or
                    self.in_col(col, number))

    def get_square(self, row, col):
        """Get the square belonging to the row and column

        Args:
            row (int): Row of square
            col (int): Column of square

        Returns:
            int: The square number
        """
        return (row // 3) * 3 + col // 3

    def in_square(self, square, number):
        """Check if square contains number

        Args:
            square (int): The square number
            number (int): The number

        Returns:
            boolean: Whether the square container the number
        """
        starting_row = square // 3 * 3
        starting_col = square % 3 * 3

        for row in range(starting_row, starting_row + 3):
            for col in range(starting_col, starting_col + 3):
                if self.board[row][col] == number:
                    return True

        return False

    def in_row(self, row, number):
        """Check if row contains number

        Args:
            row (int): The row number
            number (int): The number

        Returns:
            boolean: Whether the row contains the number
        """
        return number in self.board[row]

    def in_col(self, col, number):
        """Check if column contains number

        Args:
            col (int): The column number
            number (int): The number

        Returns:
            boolean: Whether the column contains the number
        """
        for row in self.board:
            if row[col] == number:
                return True

        return False

    def print_board(self):
        print("####")
        for row in self.board:
            print(row)
        print("####")

    def get_board(self):
        return self.board

    def clear(self):
        self.board = [[0 for i in range(9)] for j in range(9)]


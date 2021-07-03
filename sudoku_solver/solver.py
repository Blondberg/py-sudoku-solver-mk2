import pygame
from input_box import InputBox
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN
)


board_1 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

board_2 = [
    [0, 0, 0, 2, 6, 0, 0, 0, 1],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 4, 5, 0, 0],
    [0, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 0, 3, 0, 0, 0, 0, 4],
    [0, 4, 0, 0, 0, 0, 0, 3, 0],
    [7, 0, 3, 0, 1, 0, 0, 0, 0]
]

numeric_board= board_2

def run():

    pygame.init()


    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    BOX_WIDTH = 50
    BOX_HEIGHT = 50

    input_board = [[InputBox((BOX_WIDTH + 3)*i, (BOX_HEIGHT +3)*j, BOX_WIDTH, BOX_HEIGHT) for i in range(9)] for j in range(9)]
    # Solve the sudoku


    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    RUNNING = True


    while RUNNING:
        for event in pygame.event.get():
            for row in input_board:
                for input_box in row:
                    input_box.handle_event(event)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    RUNNING = False
                elif event.key == pygame.K_RETURN:
                    print_board()
                    board_to_numeric(input_board)
                    solve()
                    numeric_to_board(input_board)


            # If the player presses window close button
            if event.type == pygame.QUIT:
                RUNNING = False

        screen.fill((255, 255, 255))
        draw_board(screen, input_board)
        pygame.display.flip()

    pygame.quit()


def print_board():
    print("####")
    for row in numeric_board:
        print(row)
    print("####")


def numeric_to_board(board):
    for i in range(9):
        for j in range(9):
            board[i][j].set_text(str(numeric_board[i][j]))

def board_to_numeric(board):
    for i in range(9):
        for j in range(9):
            numeric_board[i][j] = int(board[i][j].get_text())


def draw_board(screen, board):
    for row in board:
        for input_box in row:
            input_box.draw(screen)



def solve(row=0, col=0):
    """Recursive function that solves any sudoku puzzle using recursion

    Args:
        row (int, optional): Starting row. Defaults to 0.
        col (int, optional): Starting column. Defaults to 0.

    Returns:
        func: The solve function, since it uses recursison
    """
    next_row, next_col = next_coord(row, col)
    if numeric_board[row][col] == 0:
        for number in range(1, 10): # Loop through all possible numbers
            if is_valid(row, col, number):
                numeric_board[row][col] = number
                if next_row == -1 and next_col == -1:
                    return True
                if not solve(next_row, next_col):
                    numeric_board[row][col] = 0
                else:
                    return True
    elif not(next_row == -1 and next_col == -1):
        return solve(next_row, next_col)


def next_coord(row, col):
    """Returns the next coordinate to check

    Args:
        row (int): The last checked row
        col (int): The last checked column

    Returns:
        int, int: The next row and col to check
    """
    next_row = row
    next_col = col + 1
    print(next_row)

    if next_col >= 9:
        next_col = 0
        next_row += 1

    if next_row >= 9:
        return -1, -1

    return next_row, next_col


def is_valid(row, col, number):
    """Check whether a number is valid in it's current spot

    Args:
        row (int): The row to check
        col (int): The column to check
        n (int): The number to check

    Returns:
        boolean: Whether the number is valid in the coordinate
    """
    return not (in_square(get_square(row, col), number) or
                in_row(row, number) or
                in_col(col, number))


def get_square(row, col):
    """Get the square belonging to the row and column

    Args:
        row (int): Row of square
        col (int): Column of square

    Returns:
        int: The square number
    """
    return (row // 3) * 3 + col // 3


def in_square(square, number):
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
            if numeric_board[row][col] == number:
                return True

    return False


def in_row(row, number):
    """Check if row contains number

    Args:
        row (int): The row number
        number (int): The number

    Returns:
        boolean: Whether the row contains the number
    """
    return number in numeric_board[row]


def in_col(col, number):
    """Check if column contains number

    Args:
        col (int): The column number
        number (int): The number

    Returns:
        boolean: Whether the column contains the number
    """
    for row in numeric_board:
        if row[col] == number:
            return True

    return False


if __name__ == "__main__":
    run()

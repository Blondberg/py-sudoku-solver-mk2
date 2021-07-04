def numeric_to_board(numeric_board, board):
    for i in range(9):
        for j in range(9):
            board[i][j].set_text(str(numeric_board[i][j]))


def board_to_numeric(board, numeric_board):
    for i in range(9):
        for j in range(9):
            numeric_board[i][j] = int(board[i][j].get_text() if str(board[i][j].get_text()).isnumeric() else 0)


def draw_board(screen, board):
    for row in board:
        for input_box in row:
            input_box.draw(screen)

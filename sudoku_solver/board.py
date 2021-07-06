from input_box import InputBox
import pygame

class Board:
    def __init__(self) -> None:
        self.ROW_COUNT = 9
        self.COL_COUNT = 9
        self.BOX_WIDTH = 50
        self.BOX_HEIGHT = 50

        self.numeric_board = [[0 for i in range(self.COL_COUNT)] for j in range(self.ROW_COUNT)]

        self.board = [[InputBox((self.BOX_WIDTH + 3)*i,
                             (self.BOX_HEIGHT + 3)*j,
                             self.BOX_WIDTH,
                             self.BOX_HEIGHT)
                    for i in range(self.COL_COUNT)] for j in range(self.ROW_COUNT)]


    def board_to_numeric_board(self):
        print("Converting board to numeric board")
        for row in range(self.ROW_COUNT):
            for col in range(self.COL_COUNT):
                self.numeric_board[row][col] = int(self.board[row][col].get_text() if str(self.board[row][col].get_text()).isnumeric() else 0)


    def numeric_board_to_board(self):
        print("Converting numeric board to board")
        for row in range(self.ROW_COUNT):
            for col in range(self.COL_COUNT):
                self.board[row][col].set_text(str(self.numeric_board[row][col]))


    def print_board(self):
        print("####")
        for row in self.board:
            print(row)
        print("####")


    def draw(self, screen):
        for row in self.board:
            for input_box in row:
                input_box.draw(screen)

        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen, pygame.Color(0,0,0),pygame.Rect(i*159, j*159, 158, 158), 3)


    def handle_event(self, event):
        for row in self.board:
                for box in row:
                    box.handle_event(event)


    def get_board(self):
        return self.board


    def get_numeric_board(self):
        return self.numeric_board
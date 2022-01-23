from pygame.constants import K_LEFT, K_RIGHT
from input_box import InputBox
import pygame

class Board:
    def __init__(self) -> None:
        self.ROW_COUNT = 9
        self.COL_COUNT = 9
        self.BOX_WIDTH = 50
        self.BOX_HEIGHT = 50

        self.active_row = 0
        self.active_col = 0

        self.numeric_board = [[0 for i in range(self.COL_COUNT)] for j in range(self.ROW_COUNT)]

        self.board = [[InputBox((self.BOX_WIDTH)*i,
                             (self.BOX_HEIGHT)*j,
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
                pygame.draw.rect(screen, pygame.Color(0,0,0),pygame.Rect(i*150, j*150, 150, 150), 3)


    def handle_event(self, event):
        for row in range(self.ROW_COUNT):
                for col in range(self.COL_COUNT): # Could do foreach, but need the number of row and col
                    box =  self.board[row][col]
                    box.handle_event(event)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if box.active:
                            self.active_row, self.active_col = row, col

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                if self.active_col > 0:
                    self.board[self.active_row][self.active_col].set_active(False)
                    self.active_col -= 1
                    self.board[self.active_row][self.active_col].set_active(True)
            if event.key == K_RIGHT:
                if self.active_col < 8:
                    self.board[self.active_row][self.active_col].set_active(False)
                    self.active_col += 1
                    self.board[self.active_row][self.active_col].set_active(True)
            if event.key == pygame.K_UP:
                if self.active_row > 0:
                    self.board[self.active_row][self.active_col].set_active(False)
                    self.active_row -= 1
                    self.board[self.active_row][self.active_col].set_active(True)
            if event.key == pygame.K_DOWN:
                if self.active_row < 8:
                    self.board[self.active_row][self.active_col].set_active(False)
                    self.active_row += 1
                    self.board[self.active_row][self.active_col].set_active(True)


    def get_board(self):
        return self.board


    def get_numeric_board(self):

        return self.numeric_board


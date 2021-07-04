import pygame
from pygame.locals import K_ESCAPE, KEYDOWN

from input_box import InputBox
from utils.solver import Solver
import utils.convertions as convertions


def run():

    solver = Solver()

    pygame.init()

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    BOX_WIDTH = 50
    BOX_HEIGHT = 50

    input_board = [[InputBox((BOX_WIDTH + 3)*i,
                             (BOX_HEIGHT + 3)*j,
                             BOX_WIDTH,
                             BOX_HEIGHT)
                    for i in range(9)] for j in range(9)]

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
                    convertions.board_to_numeric(input_board, solver.get_board())
                    solver.print_board()
                    solver.solve()
                    solver.print_board()
                    convertions.numeric_to_board(solver.get_board(), input_board)

            # If the player presses window close button
            if event.type == pygame.QUIT:
                RUNNING = False

        screen.fill((255, 255, 255))
        convertions.draw_board(screen, input_board)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run()

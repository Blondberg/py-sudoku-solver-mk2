import pygame
from pygame.locals import K_ESCAPE, KEYDOWN

from utils.solver import Solver
from board import Board


def run():
    pygame.init()

    board = Board()
    solver = Solver(board.get_numeric_board())


    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    RUNNING = True


    while RUNNING:
        for event in pygame.event.get():
            board.handle_event(event)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    RUNNING = False
                elif event.key == pygame.K_RETURN:
                    board.board_to_numeric_board()
                    solver.solve()
                    board.numeric_board_to_board()

            # If the player presses window close button
            if event.type == pygame.QUIT:
                RUNNING = False

        screen.fill((255, 255, 255))
        board.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run()

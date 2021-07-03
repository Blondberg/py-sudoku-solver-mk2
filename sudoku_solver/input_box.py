import pygame

class InputBox:
    def __init__(self, x_pos, y_pos, width, height, number=0):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.number = number
        self.active = False
        self.font = pygame.font.Font(None, 32)
        self.color_active = pygame.Color(255, 255, 0)
        self.color_inactive = pygame.Color(255, 0, 255)
        self.color = self.color_inactive
        self.txt_surface = self.font.render(str(self.number), True, self.color)


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.number)
                elif event.key == pygame.K_BACKSPACE:
                    self.number = self.number[:-1]
                else:
                    self.number = event.unicode if event.unicode.isnumeric() and int(event.unicode) > 0 else self.number
                self.txt_surface = self.font.render(str(self.number), True, self.color)


    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen,self.color, self.rect, 2)


    def set_text(self, text):
        self.number = text
        self.txt_surface = self.font.render(str(self.number), True, self.color)


    def get_text(self):
        return self.number


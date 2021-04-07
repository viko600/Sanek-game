import pygame
from config import *
from helper import Friut, Snake
import sys


class Game:

    def __init__(self):
        pygame.init()

        screen_size = (CELL_COUNT*CELL_SIZE, CELL_COUNT*CELL_SIZE)
        self.display = pygame.display.set_mode(screen_size) 
        self.clock = pygame.time.Clock()
        bg_image = pygame.image.load('images/grass.png')
        self.bg = pygame.transform.scale(bg_image, (screen_size))


        self._screen_update = pygame.USEREVENT
        pygame.time.set_timer(self._screen_update, 100)

        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.friut = Friut(self.display)
        self.snake = Snake(self.display)
        

    def event_loop(self):
        self.create_screen()

        while self.running:
            self.display.blit(self.bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.clean_up()
                elif event.type == self._screen_update:
                    self.snake.move_snake()
                    self.teleport_snake()
                    self.check_for_fail()
                    self.is_friut_eaten()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.clean_up()

                    elif event.key == pygame.K_w and self.snake.snake_position != 'down':
                        self.snake.change_direction(0, -1)
                        self.snake.snake_position = 'up'
                    elif event.key == pygame.K_s and self.snake.snake_position != 'up':
                        self.snake.change_direction(0, 1)
                        self.snake.snake_position = 'down'
                    elif event.key == pygame.K_a and self.snake.snake_position != 'right':
                        self.snake.change_direction(-1, 0)
                        self.snake.snake_position = 'left'
                    elif event.key == pygame.K_d and self.snake.snake_position != 'left':
                        self.snake.change_direction(1, 0)
                        self.snake.snake_position = 'right'

            self.update_on_display()
            
    def clean_up(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def update_on_display(self):
        self.snake.draw_snake()
        self.friut.draw_on_screen()

        pygame.display.update()
        self.clock.tick(60)


    def create_screen(self):
        self.display.fill((175,215,70))

    def is_friut_eaten(self):
        if self.friut.vector == self.snake.snake_body[0]:
            self.friut.new_friut()
            self.snake.increes_snake()

    def check_for_fail(self):
        if self.snake.snake_body[0] in self.snake.snake_body[1:]:
            text = self.font.render("Game Over", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_x = self.display.get_width() / 2 - text_rect.width / 2
            text_y = self.display.get_height() / 2 - text_rect.height / 2
            self.display.blit(text, [text_x, text_y])
            self.clean_up()

    def teleport_snake(self):
        for body in self.snake.snake_body:
            if body.x < 0:
                body.x = CELL_COUNT
            elif body.x > CELL_COUNT:
                body.x = 0
            if body.y < 0:
                body.y = CELL_COUNT
            elif body.y > CELL_COUNT:
                body.y = 0



if __name__=='__main__':
    game = Game()

    game.event_loop()
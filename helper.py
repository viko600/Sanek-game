import pygame
from pygame.math import Vector2
from config import *
import random


class Friut:

    def __init__(self, screen):

        self._screen = screen
        image = pygame.image.load('images/apple.png').convert_alpha()
        self._friut_image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
        self.new_friut()
        

    def draw_on_screen(self):
        rect = pygame.Rect((self.vector.x*CELL_SIZE, self.vector.y*CELL_SIZE), (CELL_SIZE, CELL_SIZE))
        self._screen.blit(self._friut_image, rect)
    
    def new_friut(self):
        self._x = random.randint(0, CELL_COUNT-1)
        self._y = random.randint(0, CELL_COUNT-1)
        self.vector = Vector2(self._x, self._y)



class Snake:

    def __init__(self, screen):

        self.snake_body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self._screen = screen
        self.snake_position = 'right'

        self._direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.snake_body:
            rect = pygame.Rect((block.x*CELL_SIZE, block.y*CELL_SIZE), (CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(self._screen, (0, 0, 255), rect)

    def move_snake(self):

        body = self.snake_body[:-1]
        body.insert(0, body[0] + self._direction)
        self.snake_body = body[:]

    def change_direction(self, new_x, new_y):

        self._direction = Vector2(new_x, new_y)

    def increes_snake(self):
        self.snake_body.append(self.snake_body[-1])
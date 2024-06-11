import pygame
import math


class Explosion:
    def __init__(self, x, y):
        self.images = []
        for num in range(1, 9):
            img = pygame.image.load(f"assets/images/sprites/explosion/{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.position = (x, y)
        self.total_time = 0

    def update(self, elapsed_seconds):
        self.total_time += elapsed_seconds


    def render(self, surface):
        frame_index = math.floor(self.total_time / 0.1)
        if frame_index < len(self.images):
            frame = self.images[frame_index]
            surface.blit(frame, self.position)
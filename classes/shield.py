from random import random
import pygame
import random

class Shield:

    # Loads image and place it with x and y, convert it collidable with a speed
    def __init__(self):
        self.img = pygame.image.load('assets/images/sprites/shield.png')
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = -5000
        self.speed = 1
    


    def render(self, surface):
        surface.blit(self.img, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x = random.randint(100, 700)
        self.rect.y = -5000

    def falling(self, elapsed_seconds):
        self.rect.y += elapsed_seconds   
        if self.rect.y == 1000:
            self.update()

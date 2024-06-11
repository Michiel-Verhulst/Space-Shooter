import pygame
import random
class Alien:

    # Loads image and place it with x and y, convert it collidable with a speed
    def __init__(self, x, y):
        self.img = pygame.image.load('assets/images/sprites/ufo.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1000
        self.lives_count = 4

    # Render image
    def render(self, surface):
        surface.blit(self.img, (self.rect.x, self.rect.y))

    # Makes ufo go down
    def update(self, elapsed_seconds, screen_height, screen_width ):

        # Down speed
        self.rect.y += self.speed * (elapsed_seconds)

        # If at end of screen => put it above screen
        if screen_height + 64 < self.rect.y:
            self.rect.y = -200
            self.rect.x = random.randint(64, screen_width- 64)
            self.lives_count -= 1

    # Fucntion when hitted
    def gotHit(self, screen_width):

        # Place above scren with a random X value
        self.rect.x = random.randint(64, screen_width- 64)
        self.rect.y = -200
       
    
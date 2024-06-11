from random import random
import pygame
import random

class Asteroid:

    # Loads image and place it with x and y, convert it collidable with a speed
    def __init__(self, x, y):
        self.img = pygame.image.load('assets/images/sprites/asteroid1.png')
        self.rect = self.img.get_rect()
        self.x = x
        self.rect.x = round(self.x)
        self.rect.y = y

        self.speed = random.randint(1, 5)
        self.angle = random.randint(1,2)
        self.health = 100

    
    def update_health_bar(self, surface):
        red_bar_color = (255, 0, 0)
        orange_bar_color = (255, 149, 0)
        green_bar_color = (111, 210, 46)
        bar_position = [self.rect.x + 10, self.rect.y + 150, self.health, 5]
        if self.health == 100:
            pygame.draw.rect(surface, green_bar_color, bar_position)
        if self.health == 50:
            pygame.draw.rect(surface, orange_bar_color, bar_position)



    def render(self, surface):
        surface.blit(self.img, (self.rect.x, self.rect.y))

    def update(self):
        self.x = random.randint(100, 700)
        self.rect.x = round(self.x)
        self.health = 100
        self.rect.y = random.randint(-1000, -200)


    def hitted(self):
            self.health -= 50
    
    def check_ast_life(self):
        if self.health == 0:
            return True

    def falling(self, elapsed_seconds):
        self.rect.y += elapsed_seconds

        if self.angle == 1:
            self.x += 0.05
            self.rect.x = round(self.x)
        else:
            self.x -= 0.05
            self.rect.x = round(self.x)
       
        if self.rect.y == 1000:
            self.update()

        if self.x == 1500 or self.x < - 200:
            self.update()

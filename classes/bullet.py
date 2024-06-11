import pygame

class Bullet:

    # Loads image and place it with x and y, convert it collidable with a speed
    def __init__(self, x, y):
        self.img = pygame.image.load('assets/images/sprites/laser.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 100

    # Render image
    def render(self, surface):
        surface.blit(self.img, (self.rect.x, self.rect.y))

    # Makes bullet go up
    def update(self, elapsed_seconds):
        self.rect.y -= self.speed * (elapsed_seconds)

    # Constructor to be able to spawn a bullet with given X and Y
    def Bullet(self, x , y):
        self.rect.x = x
        self.rect.y = y
    
    # Position getter
    @property
    def bulletPosition(self):
        return [ self.rect.x,  self.rect.y]

    # X value setter
    @bulletPosition.setter
    def bulletPositionX(self, xValue):
        self.rect.x = xValue

    # Y value setter
    @bulletPosition.setter
    def bulletPositionY(self, yValue):
        self.rect.y = yValue  


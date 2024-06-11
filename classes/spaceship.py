import pygame

class Spaceship:

    # Loads image and place it with x and y, convert it collidable with a speed
    def __init__(self, skinnumber):
        if skinnumber == 1:
            self.img = pygame.image.load('assets/images/sprites/spaceship.png')
        if skinnumber == 2:
                self.img = pygame.image.load('assets/images/sprites/spaceship2.png')
        if skinnumber == 3:
            self.img = pygame.image.load('assets/images/sprites/spaceship3.png')                     
       
        self.rect = self.img.get_rect()
        self.rect.x = 500
        self.rect.y = 500

    # Render image
    def render(self, surface):
        surface.blit(self.img, (self.rect.x, self.rect.y))

    # Position getter
    @property
    def position(self):
        return [self.rect.x, self.rect.y]

    # X value setter
    @position.setter
    def positionX(self, xValue):
        self.rect.x = xValue
        
    # Y value setter
    @position.setter
    def positionY(self, yValue):
        self.rect.y = yValue     
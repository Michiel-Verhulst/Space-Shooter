import pygame

class Background:

    def __init__(self):
        self.y = 0
        self.source = self.create_image()

    def create_image(self):
        bg = pygame.image.load("assets/images/backgrounds/space.jpg")
        return pygame.transform.scale(bg, (1024, 3840))

    def render(self, surface):
        surface.blit(self.source, (0,self.y))
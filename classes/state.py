import random
import pygame

from classes.asteroid import Asteroid
from classes.bullet import Bullet
from classes.giftbox import Giftbox
from classes.regen import Regen
from classes.shield import Shield
from classes.spaceship import Spaceship
from classes.alien import Alien
from classes.explosion import *

class State:

    # Loads the game with bullet, creates spaceship, creates alien, creates a cooldown and a target counter
    def __init__(self, skin):
        self.bulletImage = pygame.transform.scale(pygame.image.load('assets/images/sprites/ammo.png'), (25, 25))
        self.heart = pygame.image.load('assets/images/sprites/heart.png')
        self.alienHead = pygame.image.load('assets/images/sprites/alien.png')
        self.shieldIcon = pygame.image.load('assets/images/sprites/shield.png')
        

        self.player = Spaceship(skin)
        self.alien = Alien(random.randint(100, 700), 800)

        self.shield = Shield()
        self.regen = Regen()
        self.giftbox = Giftbox()

        self.bullets = []
        self.asteroid = [Asteroid(random.randint(0, 150), random.randint(-1000, -200)), Asteroid(random.randint(150, 300), random.randint(-1000, -200)), Asteroid(random.randint(300, 450), random.randint(-1000, -200)), Asteroid(random.randint(450, 600), random.randint(-1000, -200)), Asteroid(random.randint(600, 750), random.randint(-1000, -200)),Asteroid(random.randint(750, 900), random.randint(-1000, -200)), Asteroid(random.randint(900, 1050), random.randint(-1000, -200))]

        self.cooldown_count = 0
        self.targets_count = 0

        self.explosions = []
        self.explosionSound = pygame.mixer.Sound('assets/sounds/explosions/2.ogg')
        self.astExploSound = pygame.mixer.Sound('assets/sounds/explosions/1.ogg')

        self.protection = False
    
    # Render game
    def render(self, surface, screen_size, screen_height, screen_width):
        # Check if bullet
        if len(self.bullets) != 0:
            for elements in self.bullets:

                # Render bullet and make it move
                elements.render(surface)
                elements.update(0.05)

                # Check if bullet collide with ufo
                if elements.rect.colliderect(self.alien):

                    # Remove bullet
                    self.bullets.pop(0)

                    # Add 1 to target counter
                    self.targets_count += 1

                    # Play explosion sound
                    self.explosionSound.set_volume(0.1)
                    self.explosionSound.play()

                    pos = (self.alien.rect.x, self.alien.rect.y)
                    explosion = Explosion(*pos)
                    self.explosions.append(explosion)
                    # Play explosion animation
                    # self.explosion.render(surface)                    

                    # Put ufo above screen to loop
                    self.alien.gotHit(screen_width)
                
                for asteroidBullet in self.asteroid:
                    if asteroidBullet.rect.colliderect(elements):
                        self.bullets.pop(0)
                        asteroidBullet.hitted()
                        if asteroidBullet.check_ast_life() == True:
                            previousX = asteroidBullet.rect.x
                            previousY = asteroidBullet.rect.y
                            self.play_asteroid()
                            self.play_explosion(previousX, previousY)
                            asteroidBullet.update()
                          
                    

                # If not hit remove it when out of screen
                if elements.bulletPosition[1] < screen_size:
                    self.bullets.pop(0)
        
        # Render ufo on board
        self.alien.render(surface)

        for explosion in self.explosions:
            explosion.render(surface)

        # Render spaceship on board
        if self.protection == True:
             surface.blit(self.shieldIcon, (32, 235))
        self.player.render(surface)

        self.giftbox.render(surface)
        self.giftbox.falling(1)

        self.shield.render(surface)
        self.shield.falling(1)

        self.regen.render(surface)
        self.regen.falling(1)

        self.calculate_next_power(surface)

        if self.regen.rect.colliderect(self.player):
            self.regen.update()
            if self.alien.lives_count < 3:
                self.alien.lives_count += 1

        if self.shield.rect.colliderect(self.player):
            self.shield.update()
            self.protection = True

        if self.giftbox.rect.colliderect(self.player):
            self.giftbox.update()
            randomNulber = random.randint(-5, 5)
            print(randomNulber)
            if randomNulber + self.targets_count <= 0:
                self.targets_count = 1
            else:
                self.targets_count = self.targets_count + randomNulber
                

        for asteroidElement in self.asteroid:
            asteroidElement.render(surface)
            asteroidElement.update_health_bar(surface)
            asteroidElement.falling(1)
            if asteroidElement.rect.colliderect(self.player) and self.protection == False:
                self.alien.lives_count = 0

            if asteroidElement.rect.colliderect(self.alien):
                asteroidElement.update()

            if asteroidElement.rect.colliderect(self.player) and self.protection == True:
                asteroidElement.update()
                self.protection = False

        # Make ufo go down on board
        self.alien.update(0.001, screen_height, screen_width)
        for explosion in self.explosions:
            explosion.update(0.01)

    def play_explosion(self, x, y):
        posAst = (x, y)
        astExplo = Explosion(*posAst)
        self.explosions.append(astExplo)

    def play_asteroid(self):
           self.astExploSound.set_volume(0.05)
           self.astExploSound.play()

    def shoot(self, skin_rate):

        # Check for cooldown
        self.cooldown(skin_rate)
        if self.cooldown_count == 0:

            # Adding bullet
            self.bullets.append(Bullet(self.player.position[0] + 16, self.player.position[1] + 15 ))

            # Shooting Sounds
            pygame.mixer.init()
            laserSound = pygame.mixer.Sound('assets/sounds/shots/pew.ogg')
            laserSound.play()
            self.cooldown_count = 1

    def calculate_health(self, surface):
        if self.alien.lives_count == 3:  
            surface.blit(self.heart,(self.player.rect.x - 25, self.player.rect.y + 65))
            surface.blit(self.heart,(self.player.rect.x + 16 , self.player.rect.y + 65))
            surface.blit(self.heart,(self.player.rect.x + 57, self.player.rect.y + 65))

        if self.alien.lives_count == 2:  
            surface.blit(self.heart,(self.player.rect.x - 4 , self.player.rect.y + 65))
            surface.blit(self.heart,(self.player.rect.x + 36 , self.player.rect.y + 65))

        if self.alien.lives_count == 1:  
            surface.blit(self.heart,(self.player.rect.x + 16 , self.player.rect.y + 65))

    def calculate_alien(self, surface):


            Green=(0, 255, 0)
            font_obj=pygame.font.Font("assets/fonts/GAEMPLAY.TTF",25) 
            text_obj3=font_obj.render(str(self.targets_count),True,Green)

            surface.blit(text_obj3, (65, 35)) 
            surface.blit(self.alienHead,(25, 35))



    def calculate_next_power(self, surface):
            Green = (0, 255, 0)
            Yellow = (235, 198, 49)
            Red = (255, 0, 0)

            font_obj=pygame.font.Font("assets/fonts/GAEMPLAY.TTF",25) 
            if self.regen.rect.y > 0:
                text_obj3=font_obj.render('On screen',True,Green)
            else:
                text_obj3=font_obj.render(str(-1 * (self.regen.rect.y)) + 'm',True,Green)

            if self.shield.rect.y > 0:
                text_obj2=font_obj.render('On screen',True,Yellow)
            else:
                text_obj2=font_obj.render(str(-1 * (self.shield.rect.y)) + 'm',True,Yellow)

            if self.giftbox.rect.y > 0:
                text_obj=font_obj.render('On screen',True,Red)
            else:
                text_obj=font_obj.render(str(-1 * (self.giftbox.rect.y)) + 'm',True,Red) 

            surface.blit(text_obj3, (25, 105)) 
            surface.blit(text_obj2, (25, 135)) 
            surface.blit(text_obj, (25, 165)) 
            

    # Cooldown between shots
    def cooldown(self, skin_rate):
        
        if skin_rate == 1:
            if self.cooldown_count >= 150:
                self.cooldown_count = 0
            elif self.cooldown_count > 0:
                self.cooldown_count += 1
        
        if skin_rate == 2:
            if self.cooldown_count >= 350:
                self.cooldown_count = 0
            elif self.cooldown_count > 0:
                self.cooldown_count += 1
        
        if skin_rate == 3:
            if self.cooldown_count >= 550:
                self.cooldown_count = 0
            elif self.cooldown_count > 0:
                self.cooldown_count += 1

    # Spaceship getter
    @property
    def spaceship(self):
        return self.player
    
# Function to clear board
def clear_surface(surface):
    pygame.Surface.fill(surface, (0, 0, 0))

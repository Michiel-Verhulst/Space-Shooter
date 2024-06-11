import pygame

from classes.state import State
from classes.background import Background


# Create a window with a size
def create_main_surface(first, skin):
    # Initialize Pygame
    pygame.init()

    # Tuple representing width and height in pixels
    screen_size = (1024, 768)

    # Create window with given size
    pygame.display.set_caption('project-45-vijfenveertig')
    pygame.display.set_mode(screen_size)

    # Creating Surface
    surface = pygame.display.set_mode(screen_size)

    # Starts intro music
    if first == 1:
        introMusic()
    
    # Creates game
    game = State(skin)

    background = Background()

    clock = pygame.time.Clock()
   

    running = True
    while running:
        
        FPS = (pygame.time.Clock().get_time())
        if first == 1:
            start_game(surface)
            return
        print(FPS)

        #Movement 
        width, height = pygame.display.get_surface().get_size()
        key_input = pygame.key.get_pressed()
        process_key_input(game, key_input, width, height, skin)

        # Checks if you leave the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    file_object = open('leaderboard.txt', 'a')
                    file_object.write('\n'+ str(0))
                    file_object.close()
                    pygame.quit()
                    return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
        
        # Render screen
        render_frame(surface, game)

        # Background
        surface.fill((0,0,0))
        surface.blit(background.source, (0, background.y))
        surface.blit(background.source, (0, (background.y-3840)))
        if (background.y == 3840):
            background.y = 0
        background.y += 2

        # Render every object ( Spaceship, Ufo, Bullet)
        game.render(surface, -64, height, width)

        # Renders text left corner
        game.calculate_health(surface)
        game.calculate_alien(surface)
        # Creates cooldown
        game.cooldown(skin)  
       
        # Creates clock
        time = pygame.time.get_ticks()
        convertTime(time, surface)

        if game.alien.lives_count == 0:
            file_object = open('leaderboard.txt', 'a')
            file_object.write('\n'+str(game.targets_count))
            file_object.close()
            end_game(surface, skin)
            return
# Movement binds
def process_key_input(state, key, x, y, custom_speed):
    xPosition = state.player.position[0]
    yPosition = state.player.position[1]

    if key[pygame.K_LEFT]:
        if xPosition - 2 >= 0:  
            state.player.positionX = (xPosition - (custom_speed))
    if key[pygame.K_RIGHT]:
        if xPosition + 2 <= x - 64:
             state.player.positionX = (xPosition + (custom_speed ))

    if key[pygame.K_DOWN]:
        if yPosition + 2 <= y - 64:
            state.player.positionY = (yPosition + (custom_speed ))
    if key[pygame.K_UP]:
        if yPosition - 2 >= 0:
         state.player.positionY = (yPosition - (custom_speed ))

    if key[pygame.K_SPACE]:
            state.shoot(custom_speed)
    
def start_game(surface):

        game_over_bg = pygame.image.load("assets/images/backgrounds/game_start.png")
        surface.blit(game_over_bg, (0, 0))

        mouse = pygame.mouse.get_pos()


        
        started = True
        while started == True:
            mouse = pygame.mouse.get_pos()
        


            pygame.display.update()
            pygame.display.flip()
            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    return
                      

                 #checks if a mouse is clicked


                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0] > 90 and mouse[0] < 310 and mouse[1] > 630 and mouse[1] < 700:
                        pygame.mixer.pause()
                        create_main_surface(0, 1)
                        return     
                    if mouse[0] > 400 and mouse[0] < 620 and mouse[1] > 630 and mouse[1] < 700:
                        pygame.mixer.pause()
                        create_main_surface(0, 2)
                        return     
                    if mouse[0] > 720 and mouse[0] < 945 and mouse[1] > 630 and mouse[1] < 700:
                        pygame.mixer.pause()
                        create_main_surface(0, 3)
                        return     
                                  
def end_game(surface, number):
                
        game_over_bg = pygame.image.load("assets/images/backgrounds/game_over.png")
        surface.blit(game_over_bg, (0, 0))

        mouse = pygame.mouse.get_pos()
    

        White=(255,255,255)
        Green=(0, 255, 0)
        Black=(0, 0, 0)

        font_obj=pygame.font.Font("assets/fonts/GAEMPLAY.TTF",45)
        font_obj2=pygame.font.Font("assets/fonts/GAEMPLAY.TTF",25)
        text_obj=font_obj.render("RESTART",True,White)

        scoresArray = leaderBoardArray()
        first = scoresArray[0]
        second = scoresArray[1]
        third = scoresArray[2]
        lastScore = returnLast()

        firstText=font_obj.render(str(first) + " Aliens",True,Green) 
        seecondText=font_obj.render(str(second) + " Aliens",True,Green) 
        thirdText=font_obj.render(str(third) + " Aliens",True,Green)

        lastScore=font_obj2.render(str(lastScore) + " was your last score",True,White) 

        laserSound = pygame.mixer.Sound('assets/sounds/oof.ogg')
        laserSound.set_volume(10)
        laserSound.play()


        ended = True
        while ended == True:

            mouse = pygame.mouse.get_pos()
            surface.blit(text_obj, (400, 680))

            surface.blit(firstText, (150, 296))
            surface.blit(seecondText, (150, 394))
            surface.blit(thirdText, (150, 488))
            surface.blit(lastScore, (180, 583))

            pygame.display.update()
            pygame.display.flip()
            
            for ev in pygame.event.get():
    
                #checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0] > 330 and mouse[0] < 700 and mouse[1] > 660 and mouse[1] < 750:
                            create_main_surface(0, number)
                            return

                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_RETURN:
                        create_main_surface(0, number)
                        return
                
                elif ev.type == pygame.QUIT:
                    pygame.quit()
                    return
                    

                
# Function to convert miliseconds to clock with text on screen
def convertTime(ms, surface):
    millis = int(ms)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24

    White=(255,255,255)

    font_obj=pygame.font.Font("assets/fonts/GAEMPLAY.TTF",25) 
    text_obj=font_obj.render("%dh :%dm :%ds" % (hours, minutes, seconds),True,White) 
    surface.blit(text_obj, (25, 75))

def leaderBoardArray():
    with open('leaderboard.txt') as f:
        lines = f.readlines()

    array = []
    for line in lines:
        if line != '\n':
            array.append(int(line))
            array.sort(reverse=True)

    if len(array) == 1:
        array.append(0)
        array.append(0)

    if len(array) == 2:
        array.append(0)
    return array

def returnLast():
    with open('leaderboard.txt') as f:
        lines = f.readlines()

    array = []
    for line in lines:
        if line != '\n':
            array.append(int(line))
    return array[len(array) - 1]
 
# Starts intro music
def introMusic():
    pygame.mixer.init()
    introMusic = pygame.mixer.Sound('assets/music/intro.ogg')
    introMusic.set_volume(0.35)
    introMusic.play(loops=-1)

# Render screen and update it
def render_frame(surface, state):
    pygame.display.update()
    pygame.display.flip()

def main():
    create_main_surface(1, 1)

main()

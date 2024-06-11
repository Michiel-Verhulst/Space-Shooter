import pygame, random

class SoundLibrary:
    pygame.mixer.init()

    #soundlibrary (dictionary) aanmaken
    soundlibrary = {}

    #explosions
    explosion_1 = pygame.mixer.Sound("assets/sounds/explosions/1.ogg")
    soundlibrary['explosion_1'] = explosion_1
    explosion_2 = pygame.mixer.Sound("assets/sounds/explosions/2.ogg")
    soundlibrary['explosion_2'] = explosion_2
    explosion_3 = pygame.mixer.Sound("assets/sounds/explosions/3.ogg")
    soundlibrary['explosion_3'] = explosion_3
    explosion_4 = pygame.mixer.Sound("assets/sounds/explosions/4.ogg")
    soundlibrary['explosion_4'] = explosion_4
    explosion_5 = pygame.mixer.Sound("assets/sounds/explosions/5.ogg")
    soundlibrary['explosion_5'] = explosion_5
    explosion_6 = pygame.mixer.Sound("assets/sounds/explosions/6.ogg")
    soundlibrary['explosion_6'] = explosion_6

    #shots
    bullet = pygame.mixer.Sound("assets/sounds/shots/bullet.ogg")
    soundlibrary['bullet'] = bullet
    laser = pygame.mixer.Sound("assets/sounds/shots/laser.ogg")
    soundlibrary['laser'] = laser
    pew = pygame.mixer.Sound("assets/sounds/shots/pew.ogg")
    soundlibrary['pew'] = pew
    
    def play_sound(sound):
        pygame.mixer.Sound.play(SoundLibrary.soundlibrary.get(sound))
        while 1>0:
            print()

    def play_random_explosion():
        pygame.mixer.Sound.play(SoundLibrary.soundlibrary.get('explosion_'+str(random.randint(1,6))))
        while 1>0:
            print()

#    AUTO DISCOVERY (werkt niet/ ik wete niet wat er juist moet gebeuren, maar de gehardcode versie werkt wel)

#    def findAudioFiles():
#        import glob, re
#
#        path = 'assets/sounds/'
#        files = [f for f in glob.glob(path + "**/*.ogg", recursive=True)]
#        for f in files:
#            print(re.sub(r'\.+.*',r'',re.sub(r'assets/sounds/',r'',re.sub(r'\\', r'/', f))))

#   print(SoundLibrary.findAudioFiles()) 

#   table = SoundLibrary.createAudioDict(SoundLibrary.findAudioFiles())
#   Should play assets/sounds/shots/laser.ogg
#   table['shots/laser'].play()
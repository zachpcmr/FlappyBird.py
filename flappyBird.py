import pygame
import random
pygame.init()
from sys import exit
#to do the nosediving and stuff we can transform and rotate by a small number, continuesly increasing like gravity, but never past 90 degrees
class Pipe1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pipe1 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe1.png').convert()
        self.pipe2 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe2.png').convert()
        self.pipe3 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe3.png').convert()
        self.pipe4 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe4.png').convert()
        self.pipe5 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe5.png').convert()
        self.pipe6 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe6.png').convert()
        self.pipe7 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe7.png').convert()
        self.pipe8 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe8.png').convert()

        self.pipes = [
            pygame.transform.scale(self.pipe1, (100,450)),
            pygame.transform.scale(self.pipe2, (100,450)),
            pygame.transform.scale(self.pipe3, (100,450)),
            pygame.transform.scale(self.pipe4, (100,450)),
            pygame.transform.scale(self.pipe5, (100,450)),
            pygame.transform.scale(self.pipe6, (100,450)),
            pygame.transform.scale(self.pipe7, (100,450)),
            pygame.transform.scale(self.pipe8, (100,450))
        ]
        Pipe_instance = Pipe()
        self.pipe_index = 0
        self.image = self.pipes[self.pipe_index]
        self.rect = self.image.get_rect(topleft =(1300,Pipe_instance.difference))
        print('  This is the lower pipe:')
        print(Pipe_instance.difference)


    
    def update(self):
       # Move both pipes to the left
        self.rect.x -= 5

        
        # Update pipe index to change pipes over time
        self.pipe_index += 0.05
        if self.pipe_index >= len(self.pipes):
            self.pipe_index = 0
        
        # Set the image for both top and bottom pipes
        self.image = self.pipes[int(self.pipe_index)]

        # Kill the pipe if it goes off the screen
        if self.rect.right == 0:
            print('killed')
            self.kill()

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pipe1 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe1.png').convert()
        self.pipe2 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe2.png').convert()
        self.pipe3 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe3.png').convert()
        self.pipe4 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe4.png').convert()
        self.pipe5 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe5.png').convert()
        self.pipe6 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe6.png').convert()
        self.pipe7 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe7.png').convert()
        self.pipe8 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Tiles\Style 1\pipe8.png').convert()

        self.pipes = [
            pygame.transform.scale(self.pipe1, (100,450)),
            pygame.transform.scale(self.pipe2, (100,450)),
            pygame.transform.scale(self.pipe3, (100,450)),
            pygame.transform.scale(self.pipe4, (100,450)),
            pygame.transform.scale(self.pipe5, (100,450)),
            pygame.transform.scale(self.pipe6, (100,450)),
            pygame.transform.scale(self.pipe7, (100,450)),
            pygame.transform.scale(self.pipe8, (100,450))
        ]
        randNum = random.randint(100, 200)
        self.pipe_index = 0
        self.image = self.pipes[self.pipe_index]
        self.rect = self.image.get_rect(bottomleft =(1300,randNum))
        self.difference = randNum + 200
        print('  This is the upper pipe:')
        print(randNum)
        
    
    def update(self):
       # Move both pipes to the left
        self.rect.x -= 5

        
        # Update pipe index to change pipes over time
        self.pipe_index += .25
        if self.pipe_index >= len(self.pipes):
            self.pipe_index = 0
        
        # Set the image for both top and bottom pipes
        self.image = self.pipes[int(self.pipe_index)]

        # Kill the pipe if it goes off the screen
        if self.rect.right == 0:
            print('killed')
            self.kill()

    

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.bird_fly1 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Player\StyleBird1\Bird1.png').convert()
        self.bird_fly2 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Player\StyleBird1\Bird2.png').convert()
        self.bird_fly3 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Player\StyleBird1\Bird3.png').convert()
        self.bird_fly4 = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Player\StyleBird1\Bird4.png').convert()
        self.bird_fly = [self.bird_fly1,self.bird_fly2,self.bird_fly3,self.bird_fly4]
        self.bird_index = 0

        self.bird_fly = [
            pygame.transform.scale_by(self.bird_fly1, 3.5),
            pygame.transform.scale_by(self.bird_fly2, 3.5),
            pygame.transform.scale_by(self.bird_fly3, 3.5),
            pygame.transform.scale_by(self.bird_fly4, 3.5)
        ]

        self.image = self.bird_fly[self.bird_index]
        self.rect = self.image.get_rect(midbottom = (200,300))
        self.gravity = 0

    def player_input(self):
        self.gravity = -18      
        
    def apply_gravity(self):
        self.gravity += .9
        self.rect.y += self.gravity
        if self.rect.top >= 600:
            self.rect.top = 600
    #def bird_animation(self):


    def update(self):
        
        self.apply_gravity()
        self.bird_index += .1
        if self.bird_index >= len(self.bird_fly):
            self.bird_index = 0
        self.image = self.bird_fly[int(self.bird_index)]
#class Pipes(pygame.sprite.Sprite)
#    def __init__(self):
#need to set the screen
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Flappy Bird.py')

#backgrounds
backgroundSky = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Background\Background5.png').convert()
backgroundSky = pygame.transform.scale(backgroundSky,(1200,545))

backgroundGround = pygame.image.load(r'C:\Users\zkofoed\Documents\python\flappy_bird\Flappy Bird Assets\Background\ground.png').convert()
backgroundGround = pygame.transform.scale(backgroundGround,(1200,200))
backgroundGroundRect = backgroundGround.get_rect(bottom = 620)


#need clock to control frames
clock = pygame.time.Clock()


score = 0
game_active = False

#groups
bird = pygame.sprite.GroupSingle()
bird.add(Bird())
pipes = pygame.sprite.GroupSingle()
pipes.add(Pipe())
pipes1 = pygame.sprite.GroupSingle()
pipes1.add(Pipe1())
#load surfaces
#need game loop
while True:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:  # Key press detected
            if event.key == pygame.K_SPACE:  # Check if it's the spacebar
                bird.sprite.player_input()



    screen.blit(backgroundSky,(0,0))
    screen.blit(backgroundGround,backgroundGroundRect)
    bird.draw(screen)
    bird.update()
    pipes.draw(screen)
    pipes.update()
    pipes1.draw(screen)
    pipes1.update()



    #essential to refresh the screen
    pygame.display.update()
    clock.tick(60)     #frames
#need event loop
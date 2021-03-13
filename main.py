import pygame
import random
import os

WIDTH = 800
HEIGHT = 800
FPS = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imj')
player_img1 = pygame.image.load(os.path.join(img_folder, 'p1_front.png'))
player_img3 = pygame.image.load(os.path.join(img_folder, 'p2_front.png'))
player_img2 = pygame.image.load(os.path.join(img_folder, 'p1_duck.png'))

class Player(pygame.sprite.Sprite):
    flag = True
    speedx = 0
    speedy = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img1
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
    def update(self):
        self.speedx = 0
        self.speedy = 0
        if self.flag:
            self.image = player_img1
        else:
            self.image = player_img1
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        if keystate[pygame.K_SPACE]:
           self.image = player_img2
        #if keystate[pygame.K_LSHIFT]:

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right < 0:
            self.rect.left = WIDTH

        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

        if self.rect.left > WIDTH:
            self.rect.right = 0

        if self.rect.bottom < 0:
            self.rect.top = HEIGHT

class Meteor(pygame.sprite.Sprite):
    speedy = 0
    speedx = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randrange(WIDTH-self.rect.width)
        self.speedy = random.randrange(1,12)
        self.speedx = random.randrange(-5,5)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top >= HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randrange(WIDTH-self.rect.width)

class Bullet(pygame.sprite.Sprite):
    speedy = -15
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
player = Player()
for i in range(10):
    m = Meteor()
    all_sprites.add(m)
    meteors.add(m)
all_sprites.add(player)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    all_sprites.update()
    hits = pygame.sprite.spritecollide(player,meteors,False)
    if hits:
        running = False
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()


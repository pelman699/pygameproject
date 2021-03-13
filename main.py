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
# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imj')
player_img1 = pygame.image.load(os.path.join(img_folder, 'p1_front.png'))
player_img2 = pygame.image.load(os.path.join(img_folder, 'p2_front.png'))

class Player(pygame.sprite.Sprite):
    flag = True
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img1
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        if self.flag:
            self.image = player_img2
            self.flag = not self.flag

        else:
            self.image = player_img1
            self.flag = not self.flag
    def update(self):
        rx = random.randint(9, 10)
        ry = random.randint(9, 10)
        self.rect.x += rx
        self.rect.y += ry
        if self.rect.right < 0:
            self.rect.left = WIDTH

        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT




all_sprites = pygame.sprite.Group()
player = Player()
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
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()


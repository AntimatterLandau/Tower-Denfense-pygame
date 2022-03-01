
import random
import pygame
import sys
from poisontower import Tower
from arrowtower import ArrowTower
from Feiqijiangjun import FeiQiJiangJun
from accessory import Gold, Img

WIDTH = 720
HEIGHT = 480
FPS = 100

#tower positions
positions = [(340, 150), (400, 150), (460, 150), (520, 150), (580, 150), (585, 200), (585, 250), (340, 200), (340, 270), (340, 320),
             (480, 250), (480, 300), (480, 350), (540, 350), (700, 250)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INF = 5000

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load(r".\image\bg_img.jpg").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
screen.blit(bg, (0, 0))
all_sprites = pygame.sprite.Group()
gold = Gold()
frame = Img(r".\image\frame.png", 61, 34, (122, 68))
setting = Img(r".\image\setting.png", 695, 25, (50, 50))
all_towers = []
for position in positions:
    poison_tower = ArrowTower(position)
    all_towers.append(poison_tower)
    all_sprites.add(poison_tower)
all_enemy = []
all_sprites.add(setting)
for i in range(9):
    hero = FeiQiJiangJun(random.randint(-2000, -10))
    all_enemy.append(hero)
    all_sprites.add(hero)
    all_sprites.add(hero.blood_frame)
    all_sprites.add(hero.blood_dis)
all_sprites.add(frame)
all_sprites.add(gold)
pygame.display.set_caption("Tower Defense")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load(r".\image\ico.png").convert_alpha(), (32, 32)))
clock = pygame.time.Clock()
mouse_up = pygame.transform.scale(pygame.image.load(r".\image\mouseico1.png").convert_alpha(), (36, 32))
mouse_down = pygame.transform.scale(pygame.image.load(r".\image\mouseico2.png").convert_alpha(), (36, 32))
mouse_ico = mouse_up
arrow_ico = pygame.transform.scale(pygame.image.load(r"image/arrowTower-1.png").convert_alpha(), (30, 40))
poison_ico = pygame.transform.scale(pygame.image.load(r"image/poisonTower-1.png").convert_alpha(), (30, 40))
frame_ico = pygame.transform.scale(pygame.image.load(r".\image\blood.png").convert_alpha(), (30, 40))

# Game loop
running = True
building = None
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if building:
            if event.type == pygame.MOUSEBUTTONUP:
                if building == "poison":
                    new_tower = Tower((mouse_x, mouse_y))
                    gold.gold -= new_tower.value
                elif building == "arrow":
                    new_tower = ArrowTower((mouse_x, mouse_y))
                    gold.gold -= new_tower.value
                all_sprites.add(new_tower)
                all_towers.append(new_tower)
                building = None
                mouse_ico = mouse_up
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_ico = mouse_down
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_ico = mouse_up
                if 670 <= mouse_x <= 720 and 0 <= mouse_y <= 50:
                    print("setting")
                if 150 <= mouse_x <= 180 and 0 <= mouse_y <= 40:
                    mouse_ico = pygame.transform.scale(pygame.image.load(r"image/poisonTower-1.png").convert_alpha(),
                                                       (30, 40))
                    building = "poison"
                if 180 <= mouse_x <= 210 and 0 <= mouse_y <= 40:
                    mouse_ico = pygame.transform.scale(pygame.image.load(r"image/arrowTower-1.png").convert_alpha(),
                                                       (30, 40))
                    building = "arrow"

    # Update
    for tower in all_towers:
        tower.run(all_enemy, all_sprites)
    gold.gold_update(all_enemy)
    screen.blit(bg, (0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(poison_ico, (150, 0))
    screen.blit(arrow_ico, (180, 0))
    screen.blit(mouse_ico, pygame.mouse.get_pos())

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

import pygame
import math

INF = 5000

class Tower(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r".\image\poisonTower-1.png").convert_alpha()
        self.target = None
        self.target_l = INF
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.poison_arrow = None
        self.attack_boundary = 200
        self.value = 20

    def run(self, targets, sprites):
        for enemy in targets:
            rela_x = enemy.rect.centerx - self.rect.centerx
            rela_y = enemy.rect.centery - self.rect.centery
            rela_l = (rela_x ** 2 + rela_y ** 2) ** 0.5
            if rela_l < self.target_l and rela_l < self.attack_boundary and enemy.blood > 0:
                self.target = enemy
                self.target_l = rela_l
        if self.target:
            if not self.poison_arrow and self.target.blood > 0:
                self.poison_arrow = Poison_arrow(self, self.target)
            rela_x = enemy.rect.centerx - self.rect.centerx
            rela_y = enemy.rect.centery - self.rect.centery
            rela_l = (rela_x ** 2 + rela_y ** 2) ** 0.5
            if rela_l > self.attack_boundary or self.target.blood <= 0:
                self.target = None
                self.target_l = INF
        if self.poison_arrow:
            if not self.poison_arrow.state:
                sprites.add(self.poison_arrow)
                self.poison_arrow.state = True

    def update(self):
        if self.poison_arrow:
            self.poison_arrow.move()
        self.rect.x = self.rect.x

class Poison_arrow(pygame.sprite.Sprite):
    def __init__(self, poison_tower, target):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 90
        self.speed = 4
        self.target = target
        self.state = 0
        self.main_image = pygame.transform.scale(pygame.image.load(r"image/poison_arrow.png"), (8, 20))
        self.image = pygame.transform.rotate(self.main_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = poison_tower.rect.center
        self.poison_tower = poison_tower

    def move(self):
        rela_x = self.target.rect.centerx - self.rect.centerx
        rela_y = self.target.rect.centery - self.rect.centery
        rela_l = (rela_x ** 2 + rela_y ** 2) ** 0.5
        if rela_l < 30:
            self.target.blood -= 5
            self.poison_tower.poison_arrow = None
            pygame.sprite.Sprite.kill(self)
            return
        if rela_x < 0:
            self.angle = 270 + math.asin(rela_y / rela_l) / math.pi * 180
        else:
            self.angle = 450 - math.asin(rela_y / rela_l) / math.pi * 180
        self.rect.centerx += int(self.speed * rela_x / rela_l)
        self.rect.centery += int(self.speed * rela_y / rela_l)

    def update(self):
        self.image = pygame.transform.rotate(self.main_image, self.angle)
        return
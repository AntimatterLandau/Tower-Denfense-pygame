
import pygame
import math

INF = 5000

position = [(320, 150), (340, 150)]

class ArrowTower(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(r".\image\arrowTower-1.png").convert_alpha(), (60, 80))
        self.target = None
        self.target_l = INF
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.arrow = None
        self.attack_boundary = 200
        self.value = 30

    def run(self, targets, all_sprites):
        for enemy in targets:
            rela_x = enemy.rect.centerx - self.rect.centerx
            rela_y = enemy.rect.centery - self.rect.centery
            rela_l = (rela_x ** 2 + rela_y ** 2) ** 0.5
            if rela_l < self.target_l and rela_l < self.attack_boundary and enemy.blood > 0:
                self.target = enemy
                self.target_l = rela_l
        if self.target:
            if not self.arrow and self.target.blood > 0:
                self.arrow = Arrow(self, self.target)
            rela_x = enemy.rect.centerx - self.rect.centerx
            rela_y = enemy.rect.centery - self.rect.centery
            rela_l = (rela_x ** 2 + rela_y ** 2) ** 0.5
            if rela_l > self.attack_boundary or self.target.blood <= 0:
                self.target = None
                self.target_l = INF
        if self.arrow:
            if not self.arrow.state:
                all_sprites.add(self.arrow)
                self.arrow.state = True

    def update(self):
        if self.arrow:
            self.arrow.move()
        self.rect.x = self.rect.x

class Arrow(pygame.sprite.Sprite):
    def __init__(self, arrow_tower, target):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 90
        self.speed = 4
        self.target = target
        self.state = 0
        self.main_image = pygame.transform.scale(pygame.image.load(r"image/arrow.png").convert_alpha(), (8, 20))
        self.image = pygame.transform.rotate(self.main_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = arrow_tower.rect.center
        self.tower = arrow_tower

    def move(self):
        rela_x = self.target.rect.centerx - self.rect.centerx
        rela_y = self.target.rect.centery - self.rect.centery
        rela_l = (rela_x ** 2 + rela_y ** 2) ** 0.5
        if rela_l < 30:
            self.target.blood -= 5
            self.tower.arrow = None
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
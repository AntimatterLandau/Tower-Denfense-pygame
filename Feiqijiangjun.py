
import pygame
from accessory import Gold

class BloodDisplay(pygame.sprite.Sprite):
    def __init__(self, full):
        pygame.sprite.Sprite.__init__(self)
        self.full = full
        self.now = full
        self.main_image = pygame.image.load(r".\image\blood1.png").convert_alpha()
        self.image = pygame.transform.scale(self.main_image, (70, 7))
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30

    def change(self, now, rect_x, rect_y):
        self.rect.x = rect_x - 10
        self.rect.y = rect_y - 10
        self.now = now
        if self.now >= 0:
            self.image = pygame.transform.scale(self.main_image, (int(70 * self.now / self.full), 7))

    def update(self):
        return

class BloodFrame(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(r".\image\blood.png"), (80, 13))
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30

    def change(self, rect_x, rect_y):
        self.rect.x = rect_x - 15
        self.rect.y = rect_y - 13

    def update(self):
        return

class FeiQiJiangJun(pygame.sprite.Sprite):
    def __init__(self, ini_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r".\image\飞琦蒋君右.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (ini_x, 100)
        self.speed = 25
        self.range = 0
        self.blood = 1000
        self.value = 5
        self.arrive_des = False
        self.blood_dis = BloodDisplay(self.blood)
        self.blood_frame = BloodFrame()

    def move_right(self, start_x):
        if self.rect.x == start_x:
            self.image = pygame.image.load(r".\image\飞琦蒋君右.png").convert_alpha()
        self.rect.x += 1

    def move_left(self, start_x):
        if self.rect.x == start_x:
            self.image = pygame.image.load(r".\image\飞琦蒋君左.png").convert_alpha()
        self.rect.x -= 1

    def move_bottom(self, start_y):
        if self.rect.y == start_y:
            self.image = pygame.image.load(r".\image\飞琦蒋君下.png").convert_alpha()
        self.rect.y += 1

    def move_top(self, start_y):
        if self.rect.y == start_y:
            self.image = pygame.image.load(r".\image\飞琦蒋君上.png").convert_alpha()
        self.rect.y -= 1

    def move(self):
        if self.rect.x < 100 and self.rect.y == 60:
            self.rect.x += 1
        elif self.rect.x == 100 and 60 <= self.rect.y < 200:
            self.move_bottom(60)
        elif 50 < self.rect.x <= 100 and self.rect.y == 200:
            self.move_left(100)
        elif self.rect.x == 50 and 200 <= self.rect.y < 300:
            self.move_bottom(200)
        elif 50 <= self.rect.x < 240 and self.rect.y == 300:
            self.move_right(50)
        elif self.rect.x == 240 and 60 < self.rect.y <= 300:
            self.move_top(300)
        elif 240 <= self.rect.x < 610 and self.rect.y == 60:
            self.move_right(240)
        elif self.rect.x == 610 and 60 <= self.rect.y < 260:
            self.move_bottom(60)
        elif 510 < self.rect.x <= 610 and self.rect.y == 260:
            self.move_left(610)
        elif self.rect.x == 510 and 160 < self.rect.y <= 260:
            self.move_top(260)
        elif 400 < self.rect.x <= 510 and self.rect.y == 160:
            self.move_left(510)
        elif self.rect.x == 400 and 160 <= self.rect.y < 350:
            self.move_bottom(160)
        else:
            self.arrive_des = True
            self.blood = 0

    def remove(self):
        pygame.sprite.Sprite.kill(self.blood_frame)
        pygame.sprite.Sprite.kill(self.blood_dis)
        pygame.sprite.Sprite.kill(self)

    def update(self):
        if self.blood <= 0:
            self.remove()
        self.blood_dis.change(self.blood, self.rect.x, self.rect.y)
        self.blood_frame.change(self.rect.x, self.rect.y)
        self.range += self.speed
        if self.range >= 100:
            self.range = 0
            self.move()
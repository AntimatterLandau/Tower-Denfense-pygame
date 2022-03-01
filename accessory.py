
import pygame

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INF = 5000
font_arial = pygame.font.match_font('arial')

class Img(pygame.sprite.Sprite):
    def __init__(self, filename, center_x, center_y, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)

class Font(pygame.sprite.Sprite):
    def __init__(self, size, font_color, text):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.size = size
        self.font_color = font_color
        self.image = pygame.font.Font(font_arial, self.size).render(str(self.text), True, self.font_color)

class Gold(Font):
    def __init__(self):
        self.gold = 300
        super(Gold, self).__init__(13, WHITE, self.gold)
        self.rect = self.image.get_rect()
        self.rect.center = (90, 50)

    def gold_update(self, all_enemy):
        for enemy in all_enemy:
            if enemy.blood <= 0 and not enemy.arrive_des:
                self.gold += enemy.value
                all_enemy.remove(enemy)

    def update(self):
        if self.gold >= 0:
            self.text = self.gold
            self.image = pygame.font.Font(font_arial, self.size).render(str(self.text), True, self.font_color)
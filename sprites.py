import random
import pygame as pg
from settings import *


class Meteor(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/meteorBrown.png")
        size = random.randint(30, 70)

        self.image = pg.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, SCREEN_WIDTH - size), 0)

        self.speedx = random.randint(-2, 2)
        self.speedy = random.randint(1, 2)

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy


class Laser(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/laser.png")
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 2

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()



class Starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/playerShip.png")
        self.image = pg.transform.scale(self.image, (50, 50))
        self.image = pg.transform.rotate(self.image, 180)
        self.image = pg.transform.flip(self.image, False, True)
        self.hp = 3

        self.rect = self.image.get_rect()
        self.rect.midbottom= (SCREEN_WIDTH//2-25, SCREEN_HEIGHT)


    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 2
        if keys[pg.K_RIGHT]:
            self.rect.x += 2

    def draw(self, target_surf):
        if self.hp > 0:
            target_surf.blit(self.image, self.rect)
            # if self.hp < 4:
            #     target_surf.blit(self.images[-self.hp], self.rect)
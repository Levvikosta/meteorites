import pygame as pg
import time
from sprites import *



pg.init()
pg.mixer.init()

size = (800, 600)
screen = pg.display.set_mode(size)
pg.display.set_caption("Meteorites")

FPS = 120
clock = pg.time.Clock()

is_running = True
mode = "meteorites"


#загрузка изображений
background = pg.image.load("images/Stars.png")
background = pg.transform.scale(background, size)
heart = pg.image.load("images/heart.png").convert_alpha()
heart = pg.transform.scale(heart, (40,40))

heart_count = 3

starship = Starship()
meteorites = pg.sprite.Group()
lasers = pg.sprite.Group()


while is_running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    if mode == "game":
        screen.blit(background, (0,0))

    if mode == "meteorites":

        if random.randint(1,50) == 1:
            meteorites.add(Meteor())




        meteorites.update()
        starship.update()

        #если добавить жизни кораблю
        # hits = pg.sprite.spritecollide(starship, meteorites, True)

        # for hit in hits:
        #     heart_count -= 1
        #     if heart_count <= 0:
        #         is_running = False

        for meteor in meteorites:
            if meteor.rect.bottom >= size[1]:
                heart_count -= 1
                meteorites.remove(meteor)
                if heart_count <= 0:
                    is_running = False
                    mode = "final_scene"
                break


        screen.blit(background, (0,0))
        screen.blit(starship.image, starship.rect)
        meteorites.draw(screen)

        for i in range(heart_count):
            screen.blit(heart, (i*40, 0))

    if mode == "final_scene":
        ...

    pg.display.flip()
    clock.tick(FPS)

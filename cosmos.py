import pygame as pg
import random
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

# загрузка изображений
background = pg.image.load("images/Stars.png")
background = pg.transform.scale(background, size)
heart = pg.image.load("images/heart.png").convert_alpha()
heart = pg.transform.scale(heart, (40, 40))


def reset_game():
    """Сбрасывает все переменные игры до начального состояния"""
    global heart_count, points, starship, meteorites, lasers, mode
    heart_count = 3
    points = 0
    starship = Starship()
    meteorites = pg.sprite.Group()
    lasers = pg.sprite.Group()
    mode = "meteorites"


# Начальные значения
heart_count = 3
points = 0
starship = Starship()
meteorites = pg.sprite.Group()
lasers = pg.sprite.Group()

# Загрузка звуков
pg.mixer.music.load("space_ambiance.wav")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play()

laser_sound = pg.mixer.Sound("sounds/shot.wav")
laser_sound.set_volume(0.1)

lose_sound = pg.mixer.Sound("sounds/Dun Dun Dunnn.wav")
lose_sound.set_volume(0.1)

hit_sound = pg.mixer.Sound("sounds/hit.wav")
hit_sound.set_volume(0.1)

met_las_sound = pg.mixer.Sound("sounds/echo-of-a-powerful-explosion.wav")
met_las_sound.set_volume(0.1)

# Шрифты для финальной сцены
font_large = pg.font.Font(None, 74)
font_medium = pg.font.Font(None, 50)
font_small = pg.font.Font(None, 36)

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

        # Обработка нажатий клавиш в разных режимах
        if event.type == pg.KEYDOWN:
            if mode == "meteorites":
                if event.key == pg.K_SPACE:
                    lasers.add(Laser(starship.rect.midtop))
                    laser_sound.play()

            elif mode == "final_scene":
                if event.key == pg.K_r:
                    reset_game()
                elif event.key == pg.K_ESCAPE:
                    is_running = False

    if mode == "meteorites":
        # Спавн метеоритов
        if random.randint(1, 100) == 1:
            rand_met = random.randint(1,2)
            meteorites.add(Meteor(rand_met))

        # Обновление объектов
        meteorites.update()
        starship.update()
        lasers.update()

        # Проверка касания метеоритами дна
        for meteor in meteorites:
            if meteor.rect.bottom >= size[1] and (meteor.rect.centerx >0 and meteor.rect.centerx < SCREEN_WIDTH):
                heart_count -= 1
                meteorites.remove(meteor)
                hit_sound.play()
                if heart_count <= 0:
                    pg.time.wait(1000)
                    lose_sound.play()
                    pg.time.wait(2000)
                    mode = "final_scene"
                break

        # Столкновения лазеров с метеоритами
        hits = pg.sprite.groupcollide(lasers, meteorites, True, True)
        for hit in hits:
            met_las_sound.play()
            points += 10

        # Отрисовка
        screen.blit(background, (0, 0))
        screen.blit(starship.image, starship.rect)
        meteorites.draw(screen)
        lasers.draw(screen)

        # Отрисовка сердечек (жизней)
        for i in range(heart_count):
            screen.blit(heart, (i * 40, 0))

        # Отрисовка очков
        score_text = font_small.render(f"Score: {points}", True, (255, 255, 255))
        screen.blit(score_text, (size[0] - 120, 10))

    elif mode == "final_scene":
        # Затемняем фон
        overlay = pg.Surface(size)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # Текст "GAME OVER"
        game_over_text = font_large.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(size[0] // 2, size[1] // 2 - 100))
        screen.blit(game_over_text, text_rect)

        # Текст с финальным счётом
        score_text = font_medium.render(f"Your score: {points}", True, WHITE)
        score_rect = score_text.get_rect(center=(size[0] // 2, size[1] // 2 - 30))
        screen.blit(score_text, score_rect)

        # Подсказка о перезапуске
        restart_text = font_medium.render("Press R to restart", True, GREEN)
        restart_rect = restart_text.get_rect(center=(size[0] // 2, size[1] // 2 + 40))
        screen.blit(restart_text, restart_rect)

        # Подсказка о выходе
        exit_text = font_small.render("Press ESC to exit", True, GREY)
        exit_rect = exit_text.get_rect(center=(size[0] // 2, size[1] // 2 + 100))
        screen.blit(exit_text, exit_rect)


    pg.display.flip()
    clock.tick(FPS)

pg.quit()

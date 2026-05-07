import pygame
from pygame import *
from random import *



pygame.init()
# создай окно игры

WIN_W = 700
WIN_H = 500
FPS  = 90
# название окна 
display.set_caption('Pin-pong')
back = transform.scale(image.load('hole.jpg'), (WIN_W, WIN_H))
window = display.set_mode((700, 500)) 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width=65, height=65):

        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
        self.height = height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):

    def update(self):

        keys = key.get_pressed()

    # клавиша a (влево)
        if keys[K_a] and self.rect.y > 0:
            self.rect.x -= self.speed

    # клавиша d (вправо)
        if keys[K_d] and self.rect.y < 720 - 80:
            self.rect.x += self.speed


finish = False
game = False
# Игровой цикл
while game:

#обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = True
    if finish != True:
        window.blit(back, (0, 0))

        # добавление кадров/секунду
        clock.tick(FPS)


        # обновление дисплея (картинки)
        display.update()

        pygame.event.pump()
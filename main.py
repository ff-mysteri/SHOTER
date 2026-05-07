
from pygame import *
from random import *




# создай окно игры

WIN_W = 700
WIN_H = 500
FPS  = 90

clock = time.Clock()
# название окна 
display.set_caption('Pin-pong')
back = transform.scale(image.load('fon.png'), (WIN_W, WIN_H))
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

    def update_l(self):

        keys = key.get_pressed()


        if keys[K_w] and self.rect.y > 15:
            self.rect.y -= self.speed


        if keys[K_s] and self.rect.y < 365:
            self.rect.y += self.speed
    
    def update_r(self):

        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 15:
            self.rect.y -= self.speed


        if keys[K_DOWN] and self.rect.y < 365:
            self.rect.y += self.speed

player_left = Player('f.png', 20, 192, 2, 15, 120)
player_right = Player('f.png', 665, 192, 2, 15, 120)
pool = Player('poo.png', 320, 220, 4, 65, 65)
finish = False
game = True
# Игровой цикл
while game:

#обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(back, (0, 0))

        player_left.reset()

        player_left.update_l()

        player_right.reset()

        player_right.update_r()

        pool.reset()

        


        # добавление кадров/секунду
        clock.tick(FPS)


        # обновление дисплея (картинки)
        display.update()

        event.pump()
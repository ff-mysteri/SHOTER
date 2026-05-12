
from pygame import *
from random import *
font.init()



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
    def __init__(self, player_image, player_x , player_y, player_speed = 0, width=65, height=65):

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

player_speed_x = 3

player_speed_y = 3

class Poool(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x = 3, player_speed_y = 3, width=65, height=65):

        super().__init__(player_image, player_x, player_y)
        self.player_speed_x = player_speed_x
        self.player_speed_y = player_speed_y

    def update_x(self):
        self.rect.x += self.player_speed_x
        
        if sprite.collide_rect(player_left, pool) or sprite.collide_rect(player_right, pool) and timer <= 0:
            self.player_speed_x *= -1

    def update_y(self):
        self.rect.y += self.player_speed_y
        if self.rect.y >= 435 or self.rect.y <= 0 and timer <= 0:
            self.player_speed_y *= -1





player_left = Player('f.png', 20, 192, 2, 15, 120)
player_right = Player('f.png', 665, 192, 2, 15, 120)
pool = Poool('poo.png', 320, 220, 3, 3, 65, 65)
timer = 60
# фон
font = font.SysFont('Arial', 40)
lose_l = font.render('Правые ворота забивают 🤯ГОЛ💀', True, (255, 0, 0))
lose_r = font.render('Левые ворота забивают 🤯ГОЛ💀', True, (255, 0, 0))
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

        pool.update_x()

        pool.update_y()

        if pool.rect.x <= 0:
            finish = True
            window.blit(lose_l, (130, 220))

        if pool.rect.x >= 700:
            finish = True
            window.blit(lose_r, (130, 220))
        timer -= 1
        # добавление кадров/секунду
        clock.tick(FPS)


        # обновление дисплея (картинки)
        display.update()

        event.pump()
from pygame import *

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def rest(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x <= 410:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x <= 80:
            self.direction = 'right'
        if self.rect.x >= 220:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Labirint')
background = transform.scale(image.load('background3.png'), size=(win_width, win_height))

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

player = Player('hero.png', 5, win_height - 100, 3)
monster = Enemy('cyborg.png', win_height - 70, 280, 3)
monster2 = Enemy2('cyborg.png', win_width - 120, 140, 2)
final = GameSprite('sunduk1.png', win_width - 100, win_height - 110, 0)
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

w1 = Wall(82, 0, 204, 70, 20, 610, 10)
w2 = Wall(82, 0, 204, 70, 20, 10, 370)
w3 = Wall(82, 0, 204, 70, 470, 610, 10)
w4 = Wall(82, 0, 204, 170, 200, 10, 280)
w5 = Wall(82, 0, 204, 280, 20, 10, 185)
w6 = Wall(82, 0, 204, 255, 205, 70, 10)
w7 = Wall(82, 0, 204, 255, 215, 10, 110)
w8 = Wall(82, 0, 204, 255, 325, 70, 10)
w9 = Wall(82, 0, 204, 280, 335, 10, 55)
w10 = Wall(82, 0, 204,400, 100, 10, 370)
w11 = Wall(82, 0, 204, 490, 20, 10, 260)
w12 = Wall(82, 0, 204, 490, 340, 10, 60)
w13 = Wall(82, 0, 204,580, 100,10, 180)
w14 = Wall(82, 0, 204, 580, 340, 10, 130)
w15 = Wall(82, 0, 204, 680, 20, 10, 460)
w16 = Wall(82, 0, 204, 170, 100, 10, 37)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()
        monster2.update()

        player.rest()
        monster.rest()
        monster2.rest()
        final.rest()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()

    if sprite.collide_rect(player, monster)or sprite.collide_rect(player, w1) or sprite.collide_rect(player,w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(player, w12) or sprite.collide_rect(player, w13) or sprite.collide_rect(player, w14) or sprite.collide_rect(player, w15) or sprite.collide_rect(player, w16):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()

    display.update()
    clock.tick(FPS)






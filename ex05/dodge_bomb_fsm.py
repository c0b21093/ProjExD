from turtle import screensize
import pygame as pg
import sys
from random import randint

class Screen:
    def __init__(self, title, wh, bg_img):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bg_sfc = pg.image.load(bg_img)
        self.bg_rct = self.bg_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bg_sfc, self.bg_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, avater, scale, xy):
        sfc = pg.image.load(avater) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, scale) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400
    
    def blit(self, screen):
        screen.sfc.blit(self.sfc, self.rct) # 練習3

    def update(self, screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, screen.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(screen) #scr.sfc.blit(self.sfc, self.rct)

class Bomb:
    def __init__(self, color, r, v, screen):
        self.sfc = pg.Surface((r*2, r*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (r, r), r) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, screen.rct.width)
        self.rct.centery = randint(0, screen.rct.height)
        self.vx, self.vy = v # 練習6

    def blit(self, screen):
        screen.sfc.blit(self.sfc, self.rct)

    def update(self, screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, screen.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(screen) #screen.sfc.blit(self.sfc, self.rct)


###追加
class Gameover:
    def __init__(self, font, color, screen):
        self.text = font.render("GAMEOVER", True, color)
        
    def blit(self, screen):
        screen.sfc.blit(self.text,[200, 400])

    def update(self, screen):
        self.blit(screen)



def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    # 練習1
    screen = Screen("にげろこうかとん！", (1600, 900), "fig/pg_bg.jpg")

    # 練習3
    bird = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5
    bomb = Bomb((255, 0, 0), 10, (+1, +1), screen)
    font1 = pg.font.Font(None, 300)
    clock = pg.time.Clock() # 練習1
    avater_num = 0
    while True:
        screen.blit()

        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return        

        bird.update(screen) #renshu4

        # 練習7
        bomb.update(screen)
    
        # 練習8
        if bird.rct.colliderect(bomb.rct): # こうかとんrctが爆弾rctと重なったら
            gameover = Gameover(pg.font.Font(None, 300), (0, 0, 0), screen)
            gameover.update(screen)
            

            pg.display.update() #練習2
            clock.tick(0.5)
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()

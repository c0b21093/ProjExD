import pygame as pg
from pygame.locals import *
import sys

SCR_RECT = Rect(0,0,400,300)

class Paimon:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, color, r, screen):
        self.sfc = pg.Surface((r*2, r*2))
        self.sfc.set_colorkey((0,0,0))
        pg.draw.circle(self.sfc, color, (r,r), r)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = 40
        self.rct.centery = 40
        self.vx, self.vy = (+1, +1)

    def blit(self, screen):
        screen.sfc.blit(self.sfc, self.rct)
    
    def update(self, screen):
        key_states = pg.key.get_pressed()
        for key, delta in self.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
        self.blit(screen)


class Map:
    map = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    tate, yoko = len(map), len(map[0])
    imgs = [None] * 256
    msize = 20

    def draw(self, screen):
        for i in range(self.tate):
            for j in range(self.yoko):
                screen.blit(self.imgs[self.map[i][j]], (j*self.msize, i*self.msize))


def load_img(file, colorkey=None):
    img = pg.image.load(file)
    img = img.convert()
    
    if colorkey == -1:
        colorkey = img.get_at((0,0))
        img.set_colorkey(colorkey, RLEACCEL)
    return img


def main():
    pg.init()
    screen = pg.display.set_mode(SCR_RECT.size)
    pg.display.set_caption("PAIMON")
    Map.imgs[0] = load_img("fig/kuro.jpg")
    Map.imgs[1] = load_img("fig/ao.jpg")
    paimon = Paimon((255,212,0), 1.5, screen)
    map = Map()

    while (1):
        map.draw(screen)
        pg.display.update()
        paimon.update(screen)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()
        
        



if __name__ == '__main__':
    main()
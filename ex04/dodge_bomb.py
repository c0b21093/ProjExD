from codecs import BOM_BE
import tkinter as tk
import pygame as pg
import sys
import random

def main():
    tori_x, tori_y = 900, 400
    pg.init()
    pg.display.set_mode((1600,900), 0, 32)
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.get_surface()
    

    bg = pg.image.load("fig/haikei.png")
    rect_bg = bg.get_rect()

    tori = pg.image.load("fig/6.png")
    tori = pg.transform.rotozoom(tori, 0, 2.0)
    rect_tori = tori.get_rect()
    rect_tori.center = (tori_x, tori_y)

    bomb_x = random.randint(10,890)
    bomb_y = random.randint(10,1590)
    bomb = pg.Surface((20, 20))
    bomb.set_colorkey((0,0,0))
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)
    rect_bomb = bomb.get_rect()
    

    while(1):
        screen.blit(bg, rect_bg)
        screen.blit(tori, rect_tori)
        screen.blit(bomb, (bomb_x, bomb_y))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            rect_tori.move_ip(0, -1)
        if key_states[pg.K_DOWN]:
            rect_tori.move_ip(0, 1)
        if key_states[pg.K_LEFT]:
            rect_tori.move_ip(-1, 0)
        if key_states[pg.K_RIGHT]:
            rect_tori.move_ip(1, 0)

        
        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)
        


if __name__ == '__main__':
    main()


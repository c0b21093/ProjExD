import tkinter as tk
import pygame as pg
import sys

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

    while(1):
        screen.blit(bg, rect_bg)
        screen.blit(tori, rect_tori)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                rect_tori.move_ip(0, 10)
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                rect_tori.move_ip(0, -10)
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                rect_tori.move_ip(-10, 0)
            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                rect_tori.move_ip(10, 0)

        
        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)
        


if __name__ == '__main__':
    main()


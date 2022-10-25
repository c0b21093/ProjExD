import tkinter as tk
import pygame as pg
import sys

def main():
    pg.init()
    pg.display.set_mode((1600,900), 0, 32)
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.get_surface()
    

    bg = pg.image.load("fig/haikei.png").convert_alpha()
    rect_bg = bg.get_rect()

    while(1):
        pg.display.update()
        screen.blit(bg, rect_bg)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
        


if __name__ == '__main__':
    main()


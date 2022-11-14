#from tkinter import font
import sys
from pygame.locals import *
import pygame as pg
import random


WIDTH  = 440    # 画面横サイズ
HEIGHT = 280    # 画面縦サイズ
B_SIZE = 40   # 辺長
M_SIZE = 20   # 半径
M_DOT  = 40   # 移動ドット
W_TIME = 20   # 待ち時間
F_SIZE = 60   # フォントサイズ
#enemy
enemyImage = pg.transform.scale(pg.image.load('fig/goast.png'), (60,60)) 
enemy1X, enemy1Y = 225, 100
enemy2X, enemy2Y = 150, 200
enemyV = 2
enemy2V = 2

clock = pg.time.Clock()
surface = pg.display.set_mode((WIDTH, HEIGHT))

####### 0 1 2 3 4 5 6 7 8 9 10  #####
MAP = [
        [1,1,1,1,1,1,1,1,1,1,1],   # 0
        [1,0,1,0,1,0,1,0,1,0,1],   # 1
        [1,1,1,1,1,1,1,1,1,1,1],   # 2
        [1,0,1,0,1,0,1,0,1,0,1],   # 3
        [1,1,1,1,1,1,1,1,1,1,1],   # 4
        [1,0,1,0,1,0,1,0,1,0,1],   # 5
        [1,1,1,1,1,1,1,1,1,1,2]]   # 6

def main():
    pg.init()
    font = pg.font.Font(None, F_SIZE)
    input_key()

def enemy(x, y):
    surface.blit(enemyImage, (x, y))


'''
def move_bomb(): # 動く敵
    ene =  pygame.image.load("fig/8.png")
    surface.blit(ene,(160,120))
    pygame.display.update()
'''

def draw_maze():  #マップ表示
    ### 座標初期化
    x = 0
    y = 0

    for b1 in MAP:          # 1次元リスト
        for b2 in b1:       # 2次元リスト
            if   b2 == 0:   # 壁描画
                pg.draw.rect(surface, (48, 48, 48), (x*B_SIZE,y*B_SIZE,B_SIZE,B_SIZE), 0)
            elif b2 == 1:   # 通路描画
                pg.draw.rect(surface, (224,224,224), (x*B_SIZE,y*B_SIZE,B_SIZE,B_SIZE), 0)
            elif b2 == 2:   # ゴール描画
                pg.draw.rect(surface, (0,0,255), (x*B_SIZE,y*B_SIZE,B_SIZE,B_SIZE), 0)
            x += 1
        ### 座標更新
        else:
            x = 0
            y += 1

def hantei(p_x, p_y, e_x, e_y):
    global running
    if ((p_x-40 < e_x+30) and (e_x+30 < p_x) and (p_y-40 < e_y+30) and (e_y+30 < p_y)
            or (p_x-40 < e_x) and (e_x < p_x) and (p_y-40 < e_y+30) and (e_y+30 < p_y)
            or (p_x-40 < e_x+30) and (e_x+30 < p_x) and (p_y-40 < e_y) and (e_y < p_y)
            or (p_x-40 < e_x) and (e_x < p_x) and (p_y-40 < e_y) and (e_y < p_y)):
        font = pg.font.SysFont(None, 80)
        end_message = font.render("Game Over", False, (50, 0, 255))
        surface.blit(end_message, (60, 70))
        #pg.time.wait(1000)
        running = False


def input_key(): # キャラの描画とキーの移動
 
    ### 座標初期化
    row = 0         # リスト縦
    col = 0         # リスト横
    now_x = M_SIZE  # 横座標
    now_y = M_SIZE  # 縦座標
    bak_x = M_SIZE  # 横前座標
    bak_y = M_SIZE  # 縦前座標
    e_flag = 0      # 終了フラグ

    global enemyImage, enemy1X, enemy1Y, enemy2X, enemy2Y,enemyV, enemy2V
 
    ### イベント待ち
    running = True
    while running:
        draw_maze()
        #enemy
        if enemy1Y == 230:
            enemyV = -2
        if enemy1Y == -10:
            enemyV = 2
        enemy1Y += enemyV

        if enemy2Y == 230:
            enemy2V = -2
        if enemy2Y == -10:
            enemy2V = 2
        enemy2Y += enemy2V


        ### ゴール確認
        if MAP[row][col] == 3:
 
            ### 初回のみ
            if e_flag == 0:
                pg.draw.circle(surface, (255,  0,  0), (now_x,now_y), M_SIZE, 0)
                pg.draw.circle(surface, (224,224,224), (bak_x,bak_y), M_SIZE, 0)
                pg.display.update()
                pg.time.wait(100)
                e_flag = 1
 
            ### テキスト設定
            text = font.render("GOAL!", True, (224,224,255))
 
            ### ゴール描画
            surface.fill((0,0,0))
            surface.blit(text, [140,120])
 
        ### 未ゴール
        if e_flag == 0:
 
            ### 移動キャラクター描画
            pg.draw.circle(surface, (255,0,0), (now_x,now_y), M_SIZE, 0)
 
            ### 移動後通路の色に戻す
            if now_x != bak_x or now_y != bak_y:
                pg.draw.circle(surface, (224,224,224), (bak_x,bak_y), M_SIZE, 0)
 
        ### 画面再描画
        #pygame.display.update()
        pg.time.wait(W_TIME)
 
        ### 位置保存
        bak_x = now_x
        bak_y = now_y
 
        ### イベント取得
        for event in pg.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    if (now_x > 0      + B_SIZE) and (MAP[row][col-1] != 0):
                        col -= 1
                        now_x -= M_DOT
                if event.key == K_RIGHT:
                    if (now_x < WIDTH  - B_SIZE) and (MAP[row][col+1] != 0):
                        col += 1
                        now_x += M_DOT
                if event.key == K_UP:
                    if (now_y > 0      + B_SIZE) and (MAP[row-1][col] != 0):
                        row -= 1
                        now_y -= M_DOT
                if event.key == K_DOWN:
                    if (now_y < HEIGHT - B_SIZE) and (MAP[row+1][col] != 0):
                        row += 1
                        now_y += M_DOT  
        enemy(enemy1X, enemy1Y)
        enemy(enemy2X, enemy2Y)
        hantei(now_x, now_y, enemy1X, enemy1Y)
        pg.display.update()
        clock.tick(60)
    exit()

''''''
def exit():
    pg.quit()
    sys.exit()
 

if __name__ == "__main__":
    main()
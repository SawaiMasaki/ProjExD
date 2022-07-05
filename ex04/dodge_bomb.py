import pygame as pg
import tkinter as tk
import sys
import random
import datetime

def main():
    clock = pg.time.Clock()
    #スクリーン
    pg.display.set_caption("逃げろ！こうかとん")
    window_sfc = pg.display.set_mode((1600, 900))
    window_rect = window_sfc.get_rect()

    #背景
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rect = bg_sfc.get_rect()
    window_sfc.blit(bg_sfc, bg_rect)

    #こうかとん
    tori_sfc = pg.image.load("fig/9.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rect = tori_sfc.get_rect()
    tori_rect.center = 900, 400
    window_sfc.blit(tori_sfc, tori_rect)


    #爆弾
    bm_sfc = pg.Surface((20, 20))
    bm_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bm_sfc, (255, 0, 0), (10, 10),10)
    bm_rect = bm_sfc.get_rect()
    bm_rect.centerx = random.randint(0, window_rect.width)
    bm_rect.centery = random.randint(0, window_rect.height)
    vx, vy = +1, +1
    
    while(True):
        window_sfc.blit(bg_sfc, bg_rect)
        window_sfc.blit(tori_sfc, tori_rect)
        window_sfc.blit(bm_sfc, bm_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_a:  #Aを押すと爆弾が加速する
                vx *= 1.2
                vy *= 1.2
            if event.type == pg.KEYDOWN and event.key == pg.K_r:  #Rを押すと爆弾の速度がリセットされる
                vx = 1
                vy = 1

        #こうかとんの操作
        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:
            tori_rect.centery -= 1
            if tori_rect.centery < 50:
                tori_rect.centery += 1

        if key_list[pg.K_DOWN]:
            tori_rect.centery += 1
            if tori_rect.centery > 850:
                tori_rect.centery -= 1

        if key_list[pg.K_LEFT]:
            tori_rect.centerx -= 1
            if tori_rect.centerx < 50:
                tori_rect.centerx += 1

        if key_list[pg.K_RIGHT]:
            tori_rect.centerx += 1
            if tori_rect.centerx > 1550:
                tori_rect.centerx -= 1
        window_sfc.blit(tori_sfc, tori_rect)

        bm_rect.move_ip(vx, vy)
        #爆弾が壁と接触した時の処理
        if bm_rect.centerx > 1600 or bm_rect.centerx < 0:
            vx *= -1
        if bm_rect.centery > 900 or bm_rect.centery < 0:
            vy *= -1

        #爆弾と接触した時の処理
        if tori_rect.colliderect(bm_rect):
            return

        pg.display.update()
        clock.tick(1000)

def time_msg(): 
            end = datetime.datetime.now()
            root = tk.Tk()
            root.geometry("300x50")
            root.title("ゲームオーバー")
            label = tk.Label(root,
                            text=f"{(end - start).seconds}秒生き残りました",
                            font=("Ricty Diminished", 20),
                            justify="center")
            label.pack()
            root.mainloop()

if __name__ == "__main__":
    pg.init()
    start = datetime.datetime.now() 
    main()
    time_msg()
    pg.quit()
    sys.exit()
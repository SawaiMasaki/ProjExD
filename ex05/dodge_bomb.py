import pygame as pg
import tkinter as tk
import sys
import random

#ウインドウ
class Screen():

    #初期設定
    def __init__(self, title, size, bg):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size)
        self.rect = self.sfc.get_rect()
        #背景画像
        self.bg_sfc = pg.image.load(bg)
        self.bg_rect = self.bg_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bg_sfc, self.bg_rect)

#こうかとん
class Bird():
    key_delta = dict()

    #初期設定
    def __init__(self, name, per, xy):
        self.tori_sfc = pg.image.load(name)
        self.tori_sfc = pg.transform.rotozoom(self.tori_sfc, 0, per)
        self.tori_rect = self.tori_sfc.get_rect()
        self.tori_rect.center = xy

    #配置
    def blit(self, scr: Screen):
        scr.sfc.blit(self.tori_sfc, self.tori_rect)

    #移動方法
    def update(self, scr: Screen):
        key_delta = pg.key.get_pressed()
        if key_delta[pg.K_UP]:
            self.tori_rect.centery -= 1
            if self.tori_rect.centery < 50:
                self.tori_rect.centery += 1

        if key_delta[pg.K_DOWN]:
            self.tori_rect.centery += 1
            if self.tori_rect.centery > 850:
                self.tori_rect.centery -= 1

        if key_delta[pg.K_LEFT]:
            self.tori_rect.centerx -= 1
            if self.tori_rect.centerx < 50:
                self.tori_rect.centerx += 1

        if key_delta[pg.K_RIGHT]:
            self.tori_rect.centerx += 1
            if self.tori_rect.centerx > 1550:
                self.tori_rect.centerx -= 1
        self.blit(scr)

#爆弾
class Bomb():

    #初期設定
    def __init__(self, color, r, vxy, scr: Screen):
        self.bm_sfc = pg.Surface((2*r, 2*r))
        self.bm_sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.bm_sfc, color, (r, r),r)
        self.bm_rect = self.bm_sfc.get_rect()
        self.bm_rect.centerx = random.randint(0, scr.rect.width)
        self.bm_rect.centery = random.randint(0, scr.rect.height)
        self.vx, self.vy = vxy
    
    #配置
    def blit(self, scr: Screen):
        scr.sfc.blit(self.bm_sfc, self.bm_rect)
    
    #爆弾の移動
    def update(self, scr: Screen):
        self.bm_rect.move_ip(self.vx, self.vy)
        if self.bm_rect.centerx > 1600 or self.bm_rect.centerx < 0:
            self.vx *= -1
        if self.bm_rect.centery > 900 or self.bm_rect.centery < 0:
            self.vy *= -1
        self.blit(scr)

#全体の流れ
def main():
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")  #スクリーン
    tori = Bird("fig/9.png", 2.0, (900, 400))                       #こうかとん
    bomb = Bomb((255, 0, 0), 10, (1, 1), scr)                       #爆弾 

    while True:
        scr.blit()
        tori.blit(scr)
        tori.update(scr)
        bomb.blit(scr)
        bomb.update(scr)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #爆弾に接触した時の処理
        if tori.tori_rect.colliderect(bomb.bm_rect):
            return
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

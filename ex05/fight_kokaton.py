from ast import Delete
from winreg import DeleteValue
import pygame as pg
import tkinter as tk
import sys
import random
import datetime

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

#モンスター
class Monster():

    #初期設定
    def __init__(self, name, per, vxy, scr: Screen):
        self.mons_sfc = pg.image.load(name)
        self.mons_sfc = pg.transform.rotozoom(self.mons_sfc, 0, per)
        self.mons_rect = self.mons_sfc.get_rect()
        self.mons_rect.centerx = random.randint(0, scr.rect.width)
        self.mons_rect.centery = random.randint(0, scr.rect.height)
        self.vx, self.vy = vxy
    
    #配置
    def blit(self, scr: Screen):
        scr.sfc.blit(self.mons_sfc, self.mons_rect)
    
    #モンスターの移動
    def update(self, scr: Screen):
        self.mons_rect.move_ip(self.vx, self.vy)
        if self.mons_rect.centerx > 1600 or self.mons_rect.centerx < 0:
            self.vx *= -1
        if self.mons_rect.centery > 900 or self.mons_rect.centery < 0:
            self.vy *= -1
        self.blit(scr)


#全体の流れ
def main():
    n = random.randint(0, 255)
    clock = pg.time.Clock()
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")  #スクリーン
    tori = Bird("fig/9.png", 2.0, (900, 400))                       #こうかとん
    bomb = Bomb((255, 0, 0), 10, (1, 1), scr)                         #爆弾
    monster = Monster("fig/monster.png", 0.3, (1, 1), scr)         #モンスター

    while True:
        scr.blit()
        tori.blit(scr)
        tori.update(scr)
        bomb.blit(scr)
        bomb.update(scr)
        monster.blit(scr)
        monster.update(scr)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_a:  #Aを押すと爆弾が加速する
                vx *= 1.2
                vy *= 1.2
            if event.type == pg.KEYDOWN and event.key == pg.K_r:  #Rを押すと爆弾の速度がリセットされる
                vx = 1
                vy = 1

        #爆弾に接触した時の処理
        if tori.tori_rect.colliderect(bomb.bm_rect):
            #del bomb
            return

        #モンスターと接触した時の処理
        if tori.tori_rect.colliderect(monster.mons_rect):
            #del monster
            return        
        pg.display.update()
        clock.tick(1000)

def time_msg(): 
            end = datetime.datetime.now()
            root = tk.Tk()
            root.geometry("300x50")
            root.title("勝利！")
            label = tk.Label(root,
                            text=f"{(end - start).seconds}秒で破壊しました",
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

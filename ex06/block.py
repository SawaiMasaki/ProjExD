import pygame as pg
import tkinter as tk
import sys
import random
import datetime

WIDTH = 960
HEIGHT = 900
block_size = 52


#ウインドウ
class Screen:

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


#操作する棒
class Bar(pg.sprite.Sprite):
    key_data = dict()

    #初期設定
    def __init__(self, name, x, y):
        pg.sprite.Sprite.__init__(self)
        self.bar_width = 126
        self.bar_height = 54
        self.bar_sfc = pg.image.load(name)
        self.bar_rect = self.bar_sfc.get_rect()
        self.bar_rect.center = [x, y]


    def blit(self, scr:Screen):
        scr.sfc.blit(self.bar_sfc, self.bar_rect)


    def update(self, scr:Screen):
        key_data = pg.key.get_pressed()
        if key_data[pg.K_RIGHT]:
            self.bar_rect.centerx += 1
            if self.bar_rect.centerx > 900:
                self.bar_rect.centerx -= 1
        
        if key_data[pg.K_LEFT]:
            self.bar_rect.centerx -= 1
            if self.bar_rect.centerx < 60:
                self.bar_rect.centerx +=1
        self.blit(scr)


#ボール
class Ball(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self_ball_width = 24
        self_ball_height = 24
        self.ball_sfc = pg.image.load("fig/ball.png")
        self.ball_rect = self.ball_sfc.get_rect()
        self.ball_rect.center = [x, y]
        self.vx ,self.vy = 1, 1
        self.max_speed = 10


    def blit(self, scr:Screen):
        scr.sfc.blit(self.ball_sfc, self.ball_rect)


    def update(self, scr:Screen, bar:Bar):
        self.ball_rect.move_ip(self.vx, self.vy)
        if self.ball_rect.centerx > 960 or self.ball_rect.centerx < 0:
            self.vx *= -1
        if self.ball_rect.centery < 0:
            self.vy *= -1
        if self.ball_rect.colliderect(bar.bar_rect):
            self.vy *= -1
        if self.ball_rect.top > scr.rect.bottom:
            time_msg()
        self.blit(scr)

#ブロック
class Block(pg.sprite.Sprite):
    def __init__(self, x, y, index):
        pg.sprite.Sprite.__init__(self)
        self.block_width = 52
        self.block_height = 52
        
        self.block_images = [pg.image.load(f"fig/block_{i}.png") for i in range(1, 6)]

        self.block_sfc = self.block_images[index]
        
        self.block_rect = self.block_sfc.get_rect()
        self.block_rect.topleft = [x, y]
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.block_sfc, self.block_rect)

blocks = [[random.randint(0, 4) for i in range(10)] for i in range(4)]


#全体の処理
def main():
    pg.init()
    clock = pg.time.Clock()
    col_num = 0
    window = Screen("ブロック崩し", (WIDTH, HEIGHT), "fig/pg_bg.jpg")
    bar = Bar("fig/bar.png" ,WIDTH/2 ,HEIGHT-100)
    bar_group = pg.sprite.GroupSingle(bar)
    ball = Ball(bar.rect.centerx, bar.rect.centery)
    ball_group = pg.sprite.GroupSingle(ball)
    block_group = pg.sprite.Group()

    #ブロックの描画
    for col in blocks:
        row_num = 0
        for row in col:
            if row == 0:
                block = Block(100+block_size*row_num, block_size*col_num, 0)
            if row == 1:
                block = Block(100+block_size*row_num, block_size*col_num, 1)
            if row == 2:
                block = Block(100+block_size*row_num, block_size*col_num, 2)
            if row == 3:
                block = Block(100+block_size*row_num, block_size*col_num, 3)
            if row == 4:
                block = Block(100+block_size*row_num, block_size*col_num, 4)
            row_num += 1
        col_num += 1


    while True:
        window.blit()
        pg.display.update()
        block_group.draw(window)
        ball_group.draw(window)
        bar_group.draw(window)

        bar_group.update()

        ball_group.update()

        coli_num = 10

        #ボールとブロックが衝突したときの処理
        for block in block_group:
            if pg.sprite.collide_rect(ball, block):
                if abs(block.rect.top - ball.rect.bottom) < coli_num and ball.vy < 0:
                    ball.vy *= -1
                    block.kill()
                if abs(block.rect.bottom - ball.rect.top) < coli_num and ball.vy > 0:
                    ball.vy *= -1
                    block.kill()
                if abs(block.rect.right - ball.rect.left) < coli_num and ball.vx < 0:
                    ball.vx *= -1
                    block.kill()
                if abs(block.rect.left - ball.rect.right) < coli_num and ball.vx > 0:
                    ball.vx *= -1
                    block.kill()

        clock.tick(1000)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

#時間を測定
def time_msg(): 
            end = datetime.datetime.now()
            root = tk.Tk()
            root.geometry("300x50")
            root.title("ゲームオーバー")
            label = tk.Label(root,
                            text=f"{(end - start).seconds}秒です",
                            font=("Ricty Diminished", 20),
                            justify="center")
            label.pack()
            root.mainloop()
        
if __name__ == "__main__":
    start = datetime.datetime.now()
    main()

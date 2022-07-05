import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
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
    pg.draw.circle(bm_sfc, (255, 0, 0), (10, 10), 10)
    bm_rect = bm_sfc.get_rect()
    bm_rect.centerx = random.randint(0, window_rect.width)
    bm_rect.centery = random.randint(0, window_rect.height)
    vx, vy = +1, +1
    
    while(True):
        window_sfc.blit(bg_sfc, bg_rect)
        window_sfc.blit(tori_sfc, tori_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP] == True:
            tori_rect.centery -= 1
            if tori_rect.centery < 50:
                tori_rect.centery += 1

        if key_list[pg.K_DOWN] == True:
            tori_rect.centery += 1
            if tori_rect.centery > 850:
                tori_rect.centery -= 1

        if key_list[pg.K_LEFT] == True:
            tori_rect.centerx -= 1
            if tori_rect.centerx < 50:
                tori_rect.centerx += 1

        if key_list[pg.K_RIGHT] == True:
            tori_rect.centerx += 1
            if tori_rect.centerx > 1550:
                tori_rect.centerx -= 1
        window_sfc.blit(tori_sfc, tori_rect)

        bm_rect.move_ip(vx, vy)
        if bm_rect.centerx > 1600 or bm_rect.centerx < 0:
            vx *= -1
        if bm_rect.centery > 900 or bm_rect.centery < 0:
            vy *= -1    
        window_sfc.blit(bm_sfc, bm_rect)

        if tori_rect.colliderect(bm_rect) == True:
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
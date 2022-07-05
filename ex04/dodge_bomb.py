import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    window_sfc = pg.display.set_mode((1600, 900))
    widow_rect = window_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rect = bg_sfc.get_rect()
    window_sfc.blit(bg_sfc, bg_rect)

    tori_sfc = pg.image.load("fig/9.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rect = tori_sfc.get_rect()
    tori_rect.center = 900, 400
    window_sfc.blit(tori_sfc, tori_rect)

    key_list = pg.key.get_pressed()
    if key_list[pg.K_LEFT] == True:
        pass

    
    while(True):
        window_sfc.blit(bg_sfc, bg_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
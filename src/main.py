import pygame as pg
import sys
from pygame.locals import *
from const import *
from movements import Move
from map import *
from individual import *
import random


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WINDOW_SIZE, RESIZABLE)
        pg.display.set_caption("生态箱")
        self.clock = pg.time.Clock()
        self.fullScreen = False
        self.pause = False
        self.move = Move()
        generate("noise_img")

    def run(self):
        while 1:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_F11:
                        self.fullScreen = not self.fullScreen
                        if self.fullScreen:
                            window = pg.display.set_mode(WINDOW_SIZE_FULL, RESIZABLE | FULLSCREEN | HWSURFACE)
                        else:
                            window = pg.display.set_mode(WINDOW_SIZE, RESIZABLE)

                if event.type == MOUSEBUTTONUP:
                    pass
                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        self.pause = not self.pause

            if not self.pause:
                pass

            dt = self.clock.tick() / 1000
            self.move.run(dt)
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()

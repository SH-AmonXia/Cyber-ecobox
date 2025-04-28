import pygame as pg
import sys
from pygame.locals import *
from const import *
from movements import Move
from UI import UI
from map import *
import individual
import random


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WINDOW_SIZE, RESIZABLE)
        pg.display.set_caption("生态箱")
        self.clock = pg.time.Clock()
        self.fullScreen = False
        self.pause = False
        self.move = Move(0)
        self.ui = UI()
        generate("nutrition_map", 0)

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
                    if event.key == K_SPACE:
                        self.move.camera_scale_ratio = 1

                if event.type == MOUSEBUTTONUP:
                    pass
                # if event.type == MOUSEWHEEL:
                #     if event.y == 1 and self.move.camera_scale_ratio < 2:
                #         self.move.camera_scale_ratio += 0.1
                #     if event.y == -1 and self.move.camera_scale_ratio > 0.7:
                #         self.move.camera_scale_ratio -= 0.1

                if event.type == KEYUP:
                    if event.key == K_SPACE:
                        self.pause = not self.pause
                if event.type == VIDEORESIZE:
                    self.move.update_size()

            if not self.pause:
                # camera movement
                key_pressed = pg.key.get_pressed()
                if key_pressed[K_a] or key_pressed[K_LEFT]:
                    self.move.camerax = max(self.move.camera_sizex/2, self.move.camerax - 1)
                if key_pressed[K_s] or key_pressed[K_DOWN]:
                    self.move.cameray = min(self.move.mapSize-self.move.camera_sizey/2, self.move.cameray + 1)
                if key_pressed[K_d] or key_pressed[K_RIGHT]:
                    self.move.camerax = min(self.move.mapSize-self.move.camera_sizex/2, self.move.camerax + 1)
                if key_pressed[K_w] or key_pressed[K_UP]:
                    self.move.cameray = max(self.move.camera_sizey/2, self.move.cameray - 1)

            dt = self.clock.tick() / 1000
            self.move.run(dt)
            self.ui.display(dt)
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()

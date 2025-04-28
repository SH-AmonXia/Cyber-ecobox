import pygame as pg
from const import *


class Move:
    def __init__(self, mapSize):
        self.display_surface = pg.display.get_surface()
        self.all_sprites = CameraGroup()
        self.background_pic = pg.image.load(IMG_PATH + 'noise_img.png')
        self.camera_scale_ratio = 1
        self.camera_sizex, self.camera_sizey = self.display_surface.get_size()
        self.camerax = int(self.camera_sizex/2)
        self.cameray = int(self.camera_sizey/2)
        self.mapSize = MAP_SIZE[mapSize]

    def update_size(self):
        self.camera_sizex, self.camera_sizey = self.display_surface.get_size()
        self.camerax = max(self.camera_sizex/2, self.camerax - 1)
        self.cameray = max(self.camera_sizey/2, self.cameray - 1)
        self.camerax = min(self.mapSize - self.camera_sizex/2, self.camerax + 1)
        self.cameray = min(self.mapSize - self.camera_sizey/2, self.cameray + 1)

    def run(self, dt):
        self.display_surface.fill("green")
        self.display_surface = pg.display.get_surface()
        print(self.camera_sizex, self.camera_sizey, self.camerax, self.cameray, self.camera_scale_ratio)
        scaled_background_pic = pg.transform.smoothscale(self.background_pic,
                                                         (MAP_SIZE * self.camera_scale_ratio,
                                                          MAP_SIZE * self.camera_scale_ratio))
        self.display_surface.blit(scaled_background_pic, (self.camera_sizex/2-self.camerax, self.camera_sizey/2-self.cameray))
        self.all_sprites.customDraw()
        self.all_sprites.update(dt)


class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

    def customDraw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)

import pygame as pg
from const import *

class Move:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.all_sprites = CameraGroup()
        self.background_pic = pg.image.load(IMG_PATH+'noise_img.png')
        self.camerax = 0
        self.cameray = 0
        self.camera_sizex, self.camera_sizey = self.display_surface.get_size()

    def run(self, dt):
        self.display_surface.fill("green")
        self.display_surface = pg.display.get_surface()
        self.display_surface.blit(self.background_pic, (-self.camera_sizex-self.camerax, -self.camera_sizey-self.cameray))
        self.all_sprites.customDraw()
        self.all_sprites.update(dt)


class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

    def customDraw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)






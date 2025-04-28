import pygame as pg
from const import *


class UI(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

    def display(self, dt):
        # resource info
        # creature info
        # population   genetic pattern

        self.update(dt)

    def update_elements(self):
        pass



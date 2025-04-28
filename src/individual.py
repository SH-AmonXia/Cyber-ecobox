import pygame as pg
import math
from const import *


class Individual(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.nutrition = 0
        self.mass = 0
        self.pos = [x, y]

    def action(self):
        pass


def calc_distance(a: Individual, b: Individual):
    return math.sqrt((a.pos[0] - b.pos[0]) ^ 2 + (a.pos[1] - b.pos[1]) ^ 2)


class Creature(Individual):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.atp = 0
        self.age = 0
        self.speed = 0
        self.gene = {}

    def breed(self):
        pass


class Producer(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gene = {"energy_converting_rate": 1}

    def Photosynthesis(self):  # co2 ---> o2
        pass


class Consumer(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)

    def aerobic_respiration(self):  # o2 ---> co2
        pass

    def die(self):
        pass


class Decomposer(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gene = {"nutrition_to_breed": 10
                     }

    def depositing(self):  # dead ---> nutrition
        pass


class Herbivorous(Consumer):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gene = {"speed": 1,
                     "min_atp_to_eat": 50}

    def move(self):
        pass


class Carnivore(Consumer):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gene = {"speed": 1.5,
                     "detecting_distance": 300,
                     "max_prey_num": 10,
                     "min_atp_to_prey": 50,
                     "distance_with_same_kind": 300}

    def move(self):
        pass


class Omnivores(Consumer):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gene = {"speed": 1,
                     "preference": 0.5}

    def move(self):
        pass

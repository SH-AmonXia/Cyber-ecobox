import pygame as pg
from const import *


class Individual(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nutrition = 0
        self.mass = 0

    def action(self):
        pass


class Creature(Individual):
    def __init__(self):
        super().__init__()
        self.atp = 0
        self.age = 0
        self.speed = 0
        self.gene = {}

    def breed(self):
        pass


class Producer(Creature):
    def __init__(self):
        super().__init__()
        self.gene = {"energy_converting_rate": 1}

    def Photosynthesis(self):   # co2 ---> o2
        pass


class Consumer(Creature):
    def __init__(self):
        super().__init__()

    def aerobic_respiration(self):  # o2 ---> co2
        pass


class Decomposer(Creature):
    def __init__(self):
        super().__init__()
        self.gene = {"nutrition_to_breed": 10
                     }

    def depositing(self):   # dead ---> nutrition
        pass


class Herbivorous(Consumer):
    def __init__(self):
        super().__init__()
        self.gene = {"speed": 1,
                     "min_atp_to_eat": 50}

    def move(self):
        pass


class Carnivore(Consumer):
    def __init__(self):
        super().__init__()
        self.gene = {"speed": 1.5,
                     "detecting_distance": 300,
                     "max_prey_num": 10,
                     "min_atp_to_prey": 50,
                     "distance_with_same_kind": 300}

    def move(self):
        pass


class Omnivores(Consumer):
    def __init__(self):
        super().__init__()
        self.gene = {"speed": 1,
                     "preference": 0.5}

    def move(self):
        pass

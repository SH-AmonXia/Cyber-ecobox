import random
import matplotlib.pyplot as plt
from noise import pnoise2
from const import *


def perlinNoise(width, height, scale, octaves, persistence, lacunarity, seed):
    noise = [[0 for y in range(height)] for x in range(width)]
    for x in range(width):
        for y in range(height):
            noise[x][y] = pnoise2(x / scale, y / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity,
                                  base=seed)
            if noise[x][y] <= 0:
                noise[x][y] = 0
    return noise


def generate(name, mapSize):
    noise_image = perlinNoise(MAP_SIZE[mapSize], MAP_SIZE[mapSize], 128, 1, 1, 1, random.randint(1, 255))
    plt.imshow(noise_image, cmap='gray')
    plt.imsave(IMG_PATH+name+'.png', noise_image, cmap='gray')
    return noise_image


def store_map(noise_image):
    plt.imsave(IMG_PATH+'nutrition_map.png', noise_image, cmap='gray')



#!/usr/bin/env python
from itertools import chain
import os
import numpy as np
from PIL import Image

img_pth = "./img.png"
if not os.path.exists(img_pth):
    grid = np.zeros([100, 1000, 3], dtype=np.int8)
    for clear, size in enumerate([
        0, 1, 2, 3, 4, 5, 5, 6, 6, 7,
        7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        9, 9, 9, 9, 9, 9, 10, 10, 10, 10,
        11, 11, 11, 12, 12, 12, 13, 13, 14, 14,
        15, 16, 17, 19, 21, 23, 26, 29, 32, 37,
        500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
    ]):
        for this in chain(range(size), range(-1, (-1 - size), -1)):
            grid[clear][this] = [255, 255, 255]
    Image.fromarray(grid, "RGB").save(img_pth)

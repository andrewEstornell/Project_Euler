import numpy as np

# How many paths are there from the top left, to the bottom left, of a 20 x 20 grid

grid = [[i + j for j in range(0, 20)] for i in range(0, 20)]

for i in range(20):
    for j in range(20):
        print(grid[i][j], '',  end='')
    print(' ')

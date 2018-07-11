# import pdb
from helpers import normalize, blur
from simulate import print2d_list

import pdb

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    print("belief_per_cell area = height "+str(height)+" * width "+str(width))
    print("belief_per_cell = 1/ area = 1/",area)
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)

        #print("beliefs row{},{%2f}".format(i,row))
        beliefs.append(row)

    print2d_list(beliefs)
    return beliefs

def sense(sensed_color, world_grid, beliefs, p_hit, p_miss):
    updated_normd_prob = []
    print("sensed_color ",sensed_color)
    #
    # TODO - implement this in part 2
    #

    # loop through all grid cells
    # row colume way to scane
    for i in range(len(world_grid)):
        new_row_prob = []
        for j in range(len(world_grid[i])):
            # check if the sensor reading is equal to the color of the grid cell
            # if so, hit = 1
            # if not, hit = 0
            #print(world_grid[i][j])
            hit =int (sensed_color == world_grid[i][j])
            #print(hit)
            new_row_prob.append(beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss))

        updated_normd_prob.append(new_row_prob)

    #print(updated_normd_prob)
    # sum up all the components
    s =sum(map(sum,updated_normd_prob))#2d
    #s = sum(updated_normd_prob)#1d
    # divide all elements of q by the sum to normalize
    for i in range(len(world_grid)):
        for j in range(len(world_grid[i])):
            updated_normd_prob[i][j] = updated_normd_prob[i][j] / s

    return updated_normd_prob

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        new_i = (i + dy ) % height

        for j, cell in enumerate(row):
            new_j = (j + dx ) % width
            #debugger, pasue code, and read temp value
            #pdb.set_trace()

            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
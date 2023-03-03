"""Maze Game"""
import readchar
import os

"""Variables constants"""
POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
""" --------------- """

my_position = [6, 3]
map_objects = [[2, 3], [5, 6], [8, 9], [13, 8]]

while True:
    """ Draw Map """
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            for map_obj in map_objects:
                if map_obj[POS_X] == coordinate_x and map_obj[POS_Y] == coordinate_y:
                    char_to_draw = "*"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    """ --------------------------------- """

    """ Ask user where he wants to move """

    # direction = input("¿Donde te quieres mover? (Usa las teclas) [WASD]: ")
    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -= 1
        if my_position[POS_Y] < 0:
            my_position[POS_Y] = MAP_HEIGHT - 1
    elif direction == "s":
        my_position[POS_Y] += 1
        if my_position[POS_Y] >= MAP_HEIGHT:
            my_position[POS_Y] = 0
    elif direction == "a":
        my_position[POS_X] -= 1
        if my_position[POS_X] < 0:
            my_position[POS_X] = MAP_WIDTH - 1
    elif direction == "d":
        my_position[POS_X] += 1
        if my_position[POS_X] >= MAP_WIDTH:
            my_position[POS_X] = 0
    elif direction == "q":
        break

    os.system("clear")
    """ ----------------------------------- """

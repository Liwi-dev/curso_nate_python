"""Maze Game"""
import os
import random
import readchar

"""Variables constants"""
POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15


my_position = [6, 3]

''' List Objects '''
NUM_OBJECT_MAP = 11
tail_length = 0
tail = []
map_objects = []

while len(map_objects) < NUM_OBJECT_MAP:
    new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)

''' Game Loop '''
while True:
    """ Draw Map """
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_cell = None

            for map_obj in map_objects:
                if map_obj[POS_X] == coordinate_x and map_obj[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_cell = map_obj
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_cell:
                    map_objects.remove(object_cell)
                    tail_length += 1
                    NUM_OBJECT_MAP += 1
                    new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]
                    map_objects.append(new_position)

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    ''' Check if the sanke collided with itself '''
    if my_position in tail:
        print("Game Over")
        break

    """ Ask user where he wants to move """

    # direction = input("¿Donde te quieres mover? (Usa las teclas) [WASD]: ")
    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        if my_position[POS_Y] < 0:
            my_position[POS_Y] = MAP_HEIGHT - 1

    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        if my_position[POS_Y] >= MAP_HEIGHT:
            my_position[POS_Y] = 0

    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        if my_position[POS_X] < 0:
            my_position[POS_X] = MAP_WIDTH - 1

    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        if my_position[POS_X] >= MAP_WIDTH:
            my_position[POS_X] = 0

    elif direction == "q":
        break

    os.system("clear")

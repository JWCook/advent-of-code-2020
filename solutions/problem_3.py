#!/usr/bin/env python3
from logging import getLogger

from solutions import get_input_data

logger = getLogger(__file__)


def main():
    input_data = get_input_data(3)
    n_trees = count_trees_in_path(input_data)
    logger.info(f'Solution 3a: {n_trees}')


def count_trees_in_path(input_data):
    """ '.' represents an empty space, '#' represents a tree """
    height = len(input_data)
    width = len(input_data[0])
    x_index = 0
    y_index = 0
    path_chars = ''
    logger.info(
        f'Counting trees encountered in a map {height} spaces high and '
        f'infinite width; {width} spaces repeating'
    )

    for i in range(height):
        # Pattern repeats along X axis, so "wrap" X index to equivalent list index
        wrapped_x_index = x_index % width
        path_chars += input_data[y_index][wrapped_x_index]

        # Move three spaces right, one space down
        x_index += 3
        y_index += 1

    return path_chars.count('#')


if __name__ == '__main__':
    main()

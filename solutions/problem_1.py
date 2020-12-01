#!/usr/bin/env python3
import math
from itertools import product
from random import shuffle
from typing import Tuple

from solutions import get_input_data


def get_target_addends(numbers, target_sum, num_addends=2) -> Tuple[int]:
    """Get an arbitrary number of numbers from the specified list that add up to a specified sum"""
    if target_sum in numbers and 0 in numbers:
        return target_sum, 0

    # Get sets of numbers to search in different sorting orders; start with desc and asc order
    numbers = sorted([n for n in numbers if n < target_sum])
    number_sets = [numbers, numbers[::-1]]
    # Any additional sets will be in randomized order
    for i in range(num_addends - 2):
        number_set = numbers.copy()
        shuffle(number_set)
        number_sets.append(number_set)

    print(f'Searching {len(numbers)} numbers for {num_addends} numbers with a sum of {target_sum}')
    n_checks = 0
    for combination in product(*number_sets):
        n_checks += 1
        if sum(combination) == target_sum:
            print(f'Found addends {combination} in {n_checks} iterations')
            return combination

    print('No solution found')
    return [None] * num_addends


if __name__ == '__main__':
    numbers = list(map(int, get_input_data(1)))
    solution_a = get_target_addends(numbers, 2020, 2)
    print(f'Solution 1a: {math.prod(solution_a)}')
    solution_b = get_target_addends(numbers, 2020, 3)
    print(f'Solution 1b: {math.prod(solution_b)}')

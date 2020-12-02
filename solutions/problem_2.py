#!/usr/bin/env python3
import re
from logging import getLogger
from typing import List, Tuple

from solutions import get_input_data


LINE_PATTERN = re.compile(r'([0-9]+)-([0-9]+)+\s*(\w):\s*(\S+)')
InputLine = Tuple[int, int, str, str]
logger = getLogger(__file__)


def main():
    input_data = get_input_data(2)
    input_lines = [parse_line(line) for line in input_data]
    valid_passwords = [line[3] for line in input_lines if line and is_valid(*line)]
    logger.info(f'{len(valid_passwords)} out of {len(input_data)} passwords are valid')


def parse_line(line: str) -> InputLine:
    """Parse an input line into min, max, character, password"""
    line = line.strip()
    if not line:
        return None

    match = LINE_PATTERN.match(line)
    if not match:
        logger.warning(f'Invalid line: {line}')
        return None

    char_min, char_max, required_char, password = match.groups()
    return int(char_min), int(char_max), required_char, password


def is_valid(char_min: int, char_max: int, required_char: str, password: str) -> bool:
    # return char_min <= password.count(required_char) <= char_max
    char_count = password.count(required_char)
    valid = char_min <= char_count <= char_max
    if not valid:
        logger.debug(
            f'Invalid: "{password}" contains "{required_char}" {char_count} times; '
            f'requires {char_min}-{char_max}'
        )
    return valid


if __name__ == '__main__':
    main()

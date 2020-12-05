#!/usr/bin/env python3
from logging import getLogger

from solutions import get_input_data

logger = getLogger(__file__)


REQUIRED_FIELDS = {
    'byr': 'Birth Year',
    'iyr': 'Issue Year',
    'eyr': 'Expiration Year',
    'hgt': 'Height',
    'hcl': 'Hair Color',
    'ecl': 'Eye Color',
    'pid': 'Passport ID',
}
OPTIONAL_FIELDS = {'cid': 'Country ID'}


def main():
    input_data = get_input_data(4, split=False)
    passports = parse_passports(input_data)
    n_valid_passports = count_valid_passports_r1(passports)
    logger.info(f'Solution 4a: {n_valid_passports} out of {len(passports)} passports are valid')


def parse_passports(input_data):
    chunks = input_data.split('\n\n')
    logger.info(f'Found {len(chunks)} chunks of text in {len(input_data.splitlines())} total lines')
    return [parse_passport(chunk) for chunk in chunks]


def parse_passport(chunk):
    """Parse a single chunk of text into passport fields"""
    # Split fields by either single newline or space; then split fields into key-value pairs
    fields = [field.split(':') for field in chunk.split()]
    return {field[0]: field[1] for field in fields}


def count_valid_passports_r1(passports):
    """Count the total number of valid passports, according to the rule in part 1"""
    def validate_passport(passport):
        return all([field in passport for field in REQUIRED_FIELDS])

    return len([p for p in passports if validate_passport(p)])


if __name__ == '__main__':
    main()

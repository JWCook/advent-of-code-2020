from os.path import abspath, dirname, join

INPUTS_DIR = join(abspath(dirname(dirname(__file__))), 'inputs')


def get_input_data(day: int):
    with open(join(INPUTS_DIR, f'input_{day}')) as f:
        return f.read().splitlines()

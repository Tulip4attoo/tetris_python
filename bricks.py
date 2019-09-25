# this file contains all brick types
# one brick is just a dict with 4 states
# (as 4 rotations).

import numpy as np


BRICKS_L = {
    0: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0))),
    1: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 0),
                 (1, 1, 1, 0),
                 (0, 0, 0, 0))),
    2: np.array(((0, 0, 0, 0),
                 (0, 1, 0, 0),
                 (0, 1, 0, 0),
                 (0, 1, 1, 0))),
    3: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 1),
                 (0, 1, 0, 0),
                 (0, 0, 0, 0)))
}

BRICKS_J = {
    0: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0),
                 (0, 1, 1, 0))),
    1: np.array(((0, 0, 0, 0),
                 (0, 1, 0, 0),
                 (0, 1, 1, 1),
                 (0, 0, 0, 0))),
    2: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 1),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0))),
    3: np.array(((0, 0, 0, 0),
                 (0, 0, 0, 0),
                 (0, 1, 1, 1),
                 (0, 0, 0, 1)))
}

BRICKS_O = {
    0: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 0),
                 (0, 1, 1, 0),
                 (0, 0, 0, 0))),
    1: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 0),
                 (0, 1, 1, 0),
                 (0, 0, 0, 0))),
    2: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 0),
                 (0, 1, 1, 0),
                 (0, 0, 0, 0))),
    3: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 0),
                 (0, 1, 1, 0),
                 (0, 0, 0, 0)))
}

BRICKS_I = {
    0: np.array(((0, 0, 1, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0))),
    1: np.array(((0, 0, 0, 0),
                 (0, 0, 0, 0),
                 (1, 1, 1, 1),
                 (0, 0, 0, 0))),
    2: np.array(((0, 0, 1, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0))),
    3: np.array(((0, 0, 0, 0),
                 (0, 0, 0, 0),
                 (1, 1, 1, 1),
                 (0, 0, 0, 0)))
}

BRICKS_S = {
    0: np.array(((0, 0, 0, 0),
                 (0, 1, 0, 0),
                 (0, 1, 1, 0),
                 (0, 0, 1, 0))),
    1: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 1),
                 (0, 1, 1, 0),
                 (0, 0, 0, 0))),
    2: np.array(((0, 0, 0, 0),
                 (0, 1, 0, 0),
                 (0, 1, 1, 0),
                 (0, 0, 1, 0))),
    3: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 1),
                 (0, 1, 1, 0),
                 (0, 0, 0, 0)))
}

BRICKS_Z = {
    0: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 0),
                 (0, 1, 1, 0),
                 (0, 1, 0, 0))),
    1: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 0),
                 (0, 0, 1, 1),
                 (0, 0, 0, 0))),
    2: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 0),
                 (0, 1, 1, 0),
                 (0, 1, 0, 0))),
    3: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 0),
                 (0, 0, 1, 1),
                 (0, 0, 0, 0)))
}

BRICKS_T = {
    0: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 0),
                 (0, 1, 1, 0),
                 (0, 0, 1, 0))),
    1: np.array(((0, 0, 0, 0),
                 (0, 0, 0, 0),
                 (0, 1, 1, 1),
                 (0, 0, 1, 0))),
    2: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 1),
                 (0, 0, 1, 0))),
    3: np.array(((0, 0, 0, 0),
                 (0, 0, 1, 0),
                 (0, 1, 1, 1),
                 (0, 0, 0, 0)))
}

BRICKS_LIST = [BRICKS_L, BRICKS_O, BRICKS_I, BRICKS_Z, \
    BRICKS_S, BRICKS_T, BRICKS_J]

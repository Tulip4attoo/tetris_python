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
                 (0, 1, 1, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0))),
    2: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0))),
    3: np.array(((0, 0, 0, 0),
                 (0, 1, 1, 0),
                 (0, 0, 1, 0),
                 (0, 0, 1, 0)))
}

BRICKS_LIST = [BRICKS_L]

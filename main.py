import numpy as np
import utils
import bricks
import cfg
import random


class Field():
    """
    the field contains a numpy array that represents the field.
    """

    def __init__(self, shape=cfg.FIELD_SHAPE, padding=cfg.PADDING):
        """
        default shape is (20, 10)
        """
        self.padding_size = padding
        self.field_render = np.zeros(shape)
        self.field_padding = np.zeros((shape[0] + 2*padding, shape[1] + 2*padding))

    def add_bricks(self, bricks_cl):
        """
        when a brick hit the floor, it will be attached into the field
        """
        self.field_render, self.field_padding = utils.calc_move(self.field_padding, bricks_cl)

    def check_and_clear_a_row(self):
        """
        
        """
        pass


class Bricks():
    """
    the Bricks has 3 values:
        - a dictionary that contains 4 numpy arrays size (4, 4)
            as the 4 rotation renders of the bricks itself.
        - a (x_coord, y_coord) list that is the top-left coord of the above
            numpy array.
        - a number that show the rotation of the bricks.
    """

    def __init__(self, coord=cfg.DEFAULT_COORD):
        self.bricks = {"bricks": {},
                       "coord": coord[:],
                       "rotation": 0}
        self.random_brick()
        self.dumb_bricks = self.copy_bricks(self.bricks)
        self.action_dict = {0       : self.do_nothing,
                            ord("w"): self.rotate,
                            ord("a"): self.move_left,
                            ord("d"): self.move_right,
                            ord("s"): self.move_down}

    def copy_bricks(self, brick_a):
        """
        return brick_a.copy()
        """
        new_bricks = {"bricks": brick_a["bricks"].copy(),
                      "coord": brick_a["coord"].copy(),
                      "rotation": brick_a["rotation"]}
        return new_bricks

    def random_brick(self):
        bricks_list = bricks.BRICKS_LIST[:]
        random_brick = random.choice(bricks_list)
        self.bricks["bricks"] = random_brick
        self.bricks["rotation"] = random.choice([0, 1, 2, 3])
        return self.bricks

    def control_brick(self, key):
        """
        this function is to control the bricks, includes rotation= and move
        key is a number of ord(key)
        will refactor by adding into a dict of moveset later
        """
        self.dumb_bricks = self.copy_bricks(self.bricks)
        action = self.action_dict[key]
        action()

    def revert(self):
        """
        in case there is a invalid move, we can revert to previous state.
        """
        self.bricks = self.copy_bricks(self.dumb_bricks)

    def do_nothing(self):
        pass

    def rotate(self):
        """
        this function is to change the rotation value in self.bricks
        always turn right aka +1 to the value
        """
        self.bricks["rotation"] = (self.bricks["rotation"] + 1) % 4

    def move_left(self):
        self.bricks["coord"][1] -= 1

    def move_right(self):
        self.bricks["coord"][1] += 1

    def move_down(self):
        self.bricks["coord"][0] -= 1

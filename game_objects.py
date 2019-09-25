import numpy as np
import utils
import bricks
import cfg
import random


class Field():
    """
    the field contains a numpy array that represents the field.
    """

    def __init__(self):
        """
        """
        self.padding_size = cfg.PADDING
        self.field_render = np.zeros(cfg.FIELD_SHAPE)
        self.field_padding = np.zeros((cfg.FIELD_SHAPE[0] + 2*cfg.PADDING, \
            cfg.FIELD_SHAPE[1] + 2*cfg.PADDING))

    def add_brick(self, brick_cl):
        """
        when a brick hit the floor, it will be attached into the field
        """
        self.field_render, self.field_padding = \
            utils.calc_move(self.field_padding, brick_cl)

    def check_and_clear_rows(self):
        self.field_render = utils.clear_rows(self.field_render)
        self.field_padding = utils.clear_rows(self.field_padding)

    def revert_to_state(self, f_render, f_padding):
        self.field_render = f_render.copy()
        self.field_padding = f_padding.copy()


class Brick():
    """
    the brick has 3 values:
        - a dictionary that contains 4 numpy arrays size (4, 4)
            as the 4 rotation renders of the brick itself.
        - a (x_coord, y_coord) list that is the top-left coord of the above
            numpy array.
        - a number that show the rotation of the brick.
    """

    def __init__(self, coord=cfg.DEFAULT_COORD):
        self.brick = {"brick": {},
                      "coord": coord[:],
                      "rotation": 0}
        self.next_brick = {"brick": {},
                           "coord": coord[:],
                           "rotation": 0}
        self.random_brick()
        self.random_next_brick()
        self.dumb_brick = self.copy_brick(self.brick)
        self.action_dict = {-1:        self.do_nothing,
                            ord("w"): self.rotate,
                            ord("a"): self.move_left,
                            ord("d"): self.move_right,
                            ord("s"): self.move_down,
                            ord(" "): self.move_to_floor}

    def copy_brick(self, brick_a):
        """
        return brick_a.copy()
        """
        new_brick = {"brick": brick_a["brick"].copy(),
                     "coord": brick_a["coord"].copy(),
                     "rotation": brick_a["rotation"]}
        return new_brick

    def create_new_brick(self):
        self.brick = self.copy_brick(self.next_brick)
        self.random_next_brick()

    def random_brick(self):
        brick_list = bricks.BRICKS_LIST[:]
        random_brick = random.choice(brick_list)
        self.brick["brick"] = random_brick
        self.brick["rotation"] = random.choice([0, 1, 2, 3])
        return self.brick

    def random_next_brick(self):
        brick_list = bricks.BRICKS_LIST[:]
        random_brick = random.choice(brick_list)
        self.next_brick["brick"] = random_brick
        self.next_brick["rotation"] = random.choice([0, 1, 2, 3])
        return self.next_brick

    def control_brick(self, key, field):
        """
        this function is to control the brick, includes rotation= and move
        key is a number of ord(key)
        will refactor by adding into a dict of moveset later
        """
        self.dumb_brick = self.copy_brick(self.brick)
        action = self.action_dict[key]
        action(field)

    def revert(self):
        """
        in case there is a invalid move, we can revert to previous state.
        """
        self.brick = self.copy_brick(self.dumb_brick)

    def revert_to_state(self, saved_brick, saved_next_brick):
        """
        revert into a saved state
        """
        self.brick = self.copy_brick(saved_brick)
        self.next_brick = self.copy_brick(saved_next_brick)

    def do_nothing(self, field):
        pass

    def rotate(self, field):
        """
        this function is to change the rotation value in self.brick
        always turn right aka +1 to the value
        """
        self.brick["rotation"] = (self.brick["rotation"] + 1) % 4

    def move_left(self, field):
        self.brick["coord"][1] -= 1

    def move_right(self, field):
        self.brick["coord"][1] += 1

    def move_down(self, field):
        self.brick["coord"][0] -= 1

    def move_to_floor(self, field):
        while utils.check_valid(field, self):
            self.brick["coord"][0] -= 1
        self.brick["coord"][0] += 1

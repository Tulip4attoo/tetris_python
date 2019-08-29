import numpy as np
import utils
import bricks
import cfg
import random


class Field():
    """
    the field contains a numpy array that represents the field.
    """

    def __init__(self, shape=cfg.FIELD_SHAPE):
        """
        default shape is (20, 10)
        """
        self.field = np.zeros(shape)
        # self.field_rendered = self.render_field()

    def render_field(self):
        """
        render self.field into a viewable field.
        We change 0 into "-" and 1 into *
        """
        rows_rendered = []
        for row in self.field:
            row_rendered = ""
            for i in row:
                if i == 0:
                    row_rendered += "-"
                else:
                    row_rendered += "*"
            rows_rendered.append(row_rendered)
        self.field_rendered = "\n".join(rows_rendered)
        return self.field_rendered


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
        # init a self.bricks
        self.bricks = {"bricks": {},
                       "coord": coord,
                       "rotation": 0}
        self.random_brick()

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
        if key == ord("w"):
            self.rotate()
        elif key == ord("a"):
            self.move_left()
        elif key == ord("d"):
            self.move_right()
        elif key == ord("s"):
            self.move_down()

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

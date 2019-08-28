import numpy as np
import utils


class Field():
    """
    the field contains a numpy array.
    """

    def __init__(self, shape=(20, 8)):
        """
        default shape is (20,8) # will correct later
        """
        print(shape)
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
        - a numpy array size (4,4) that contains the bricks itself.
        - a (x_coord, y_coord) list that is the top-left coord of the above
            numpy array.
    """
    def __init__(size=()):
        pass

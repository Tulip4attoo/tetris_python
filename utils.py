import numpy as np
import cfg


def create_screen(field, bricks):
    """
    combine field and bricks into a string, that will be feed to render
    the screen
    """
    rows_rendered = []
    new_bricks = np.zeros(field.shape)
    x_brick = cfg.FIELD_SHAPE[0] - bricks["coord"][0]
    y_brick = bricks["coord"][1]
    new_bricks[x_brick: x_brick + 4, y_brick: y_brick + 4] = \
        bricks["bricks"][bricks["rotation"]]

    combine_field = field + new_bricks
    for row in combine_field:
        row_rendered = ""
        for i in row:
            if i == 0:
                row_rendered += "-"
            else:
                row_rendered += "*"
        rows_rendered.append(row_rendered)
    field_rendered = "\n".join(rows_rendered)
    return field_rendered

import numpy as np
import cfg


def create_screen(field_cl, bricks_cl):
    """
    combine field and bricks into a string, that will be feed to render
    the screen
    """
    rows_rendered = []

    combine_field, _ = calc_move(field_cl.field_padding, bricks_cl)
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


def check_valid(field_cl, bricks_cl):
    """

    """
    field = np.array(field_cl.field_render, dtype=np.bool)
    bricks = bricks_cl.bricks["bricks"][bricks_cl.bricks["rotation"]]
    n_bricks = np.array(bricks, dtype=np.bool)
    combine_field, _ = calc_move(field_cl.field_padding, bricks_cl)
    combine_field = np.array(combine_field, dtype=np.bool)
    return field.sum() + bricks.sum() == combine_field.sum()


def calc_move(field_padding, bricks_cl):
    """
    combine field and bricks into a string, that will be feed to render
    the screen
    """
    field = field_padding[:]
    bricks = bricks_cl.bricks
    pad = cfg.PADDING
    f_shape = cfg.FIELD_SHAPE
    new_bricks = np.zeros(field.shape)
    x_brick = cfg.FIELD_SHAPE[0] - bricks["coord"][0]
    y_brick = bricks["coord"][1]
    new_bricks[x_brick + pad: x_brick + 4 + pad, y_brick + pad: y_brick + 4 + pad] = \
        bricks["bricks"][bricks["rotation"]]

    f_combine_field = field + new_bricks
    combine_field = f_combine_field[pad: pad + f_shape[0], \
        pad: pad + f_shape[1]]
    return combine_field, f_combine_field
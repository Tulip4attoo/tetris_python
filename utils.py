import numpy as np
import cfg
import time
import game_objects as go


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
                row_rendered += ". "
            else:
                row_rendered += "██"
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
    attached brick into field, get result as 2 numpy array
    field_render and field_padding
    """
    field = field_padding[:]
    bricks = bricks_cl.bricks
    pad = cfg.PADDING
    f_shape = cfg.FIELD_SHAPE
    new_bricks = np.zeros(field.shape)
    x_brick = cfg.FIELD_SHAPE[0] - bricks["coord"][0] + pad
    y_brick = bricks["coord"][1] + pad
    new_bricks[x_brick: x_brick + 4, y_brick: y_brick + 4] = \
        bricks["bricks"][bricks["rotation"]]

    f_combine_field = field + new_bricks
    combine_field = f_combine_field[pad: pad + f_shape[0], \
        pad: pad + f_shape[1]]
    return combine_field, f_combine_field


def clear_rows(field, sum_require=cfg.FIELD_SHAPE[1]):
    """
    """
    new_f_render = np.zeros(field.shape)
    f_row = field.shape[0] - 1
    for i in range(field.shape[0] - 1, -1, -1):
        if field[i].sum() != sum_require:
            new_f_render[f_row] = field[i]
            f_row -= 1
    return new_f_render


def get_field_score(field_render):
    """
    return a list that contains 4 values:
        + agg_height
        + complete_lines
        + holes
        + bumpiness
    """
    result = [0, 0, 0, 0]
    result[0], col_heights = get_agg_height(field_render)
    result[1] = get_complete_lines(field_render)
    result[2] = get_holes(field_render, result[0])
    result[3] = get_bumpiness(col_heights)
    return result


def get_agg_height(field):
    result = 0
    col_heights = []
    field_transpose = field.transpose()
    for row in field_transpose:
        trigger = True
        for i in range(len(row)):
            if row[i] != 0:
                result += len(row) - i
                col_heights.append(len(row) - i)
                trigger = False
                break
        if trigger:
            col_heights.append(0)
    return result, col_heights


def get_complete_lines(field):
    result = 0
    for row in field:
        if row.sum() == cfg.FIELD_SHAPE[1]:
            result += 1
    return result


def get_holes(field, agg_height):
    return agg_height - field.sum()


def get_bumpiness(col_heights):
    result = 0
    for i in range(cfg.FIELD_SHAPE[1] - 1):
        result += abs(col_heights[i] - col_heights[i+1])
    return result


def calc_combine_score(score_list):
    """

    """
    result = 0
    for i in range(len(score_list)):
        result += score_list[i] * cfg.RESULT_PARAMS[i]
    return result


def score_a_moveset(field_cl, brick_cl, moveset):
    """
    a moveset is a string that contains the move, like: wwas
    """
    move_list = [ord(i) for i in list(moveset)]
    saved_state = brick_cl.copy_bricks(brick_cl.bricks)
    for move in move_list:
        brick_cl.control_brick(move, field_cl)
        valid = check_valid(field_cl, brick_cl)
        if not valid:
            brick_cl.revert()
    new_f_render, _ = calc_move(field_cl.field_padding, brick_cl)
    score_list = get_field_score(new_f_render)
    combine_score = calc_combine_score(score_list)

    brick_cl.revert_to_state(saved_state)
    return combine_score


def get_moveset(field_cl, brick_cl):
    """
    choose the moveset with the highest score
    """
    score_list = [0] * len(cfg.MOVESET_LIST)
    for ind in range(len(cfg.MOVESET_LIST)):
        moveset = cfg.MOVESET_LIST[ind]
        score_list[ind] = score_a_moveset(field_cl, brick_cl, moveset)
    # return the moveset with highest score in score_list
    moveset = cfg.MOVESET_LIST[score_list.index(max(score_list))]
    keys_list = [ord(i) for i in list(moveset)]
    return keys_list

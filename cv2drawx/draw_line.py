

import cv2
import numpy as np


def draw_line(MatLike: np.ndarray,
              start: tuple[int, int],
              end: tuple[int, int],
              color: tuple[int, int, int],
              thickness: int=1,
              dash_size: int=1,
              dash_gap: int=1
              ):

    if dash_size != 0 and dash_gap != 0:
        x1, y1 = start
        x2, y2 = end

        dx = x2 - x1
        dy = y2 - y1

        length = int(np.hypot(dx, dy))

        for i in range(0, length, dash_size + dash_gap):
            x_start = int(x1 + dx * (i / length))
            y_start = int(y1 + dy * (i / length))

            x_end = int(x1 + dx * min((i + dash_size), length)/length)
            y_end = int(y1 + dy * min((i + dash_size), length)/length)

            cv2.line(
                MatLike,
                (x_start, y_start),
                (x_end, y_end),
                color,
                thickness,
                cv2.LINE_AA
            )

    else:
        cv2.line(
            MatLike,
            start,
            end,
            color,
            thickness,
            cv2.LINE_AA
        )
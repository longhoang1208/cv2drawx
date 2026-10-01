

import cv2
import numpy as np
from cv2drawx.draw_line import draw_line


def draw(MatLike: np.ndarray,
         start_point: tuple[int, int],
         end_point: tuple[int, int],
         fill_color: tuple[int, int, int],
         border_color: tuple[int, int, int]|None=None,
         border_thickness: int|None=None,
         thickness: int=-1,
         dash_size: int=0,
         dash_gap: int=0,
         border_radius: int=1
         ) -> None:

    x1, y1 = start_point
    x2, y2 = end_point

    # TOP-LEFT CORNER
    cv2.circle(
        MatLike,
        (
            x1 + border_radius,
            y1 + border_radius
        ),
        radius=border_radius,
        color=fill_color,
        thickness=thickness,
        lineType=cv2.LINE_AA
    )

    # TOP-RIGHT CORNER
    cv2.circle(
        MatLike,
        (
            x2 - border_radius,
            y1 + border_radius
        ),
        radius=border_radius,
        color=fill_color,
        thickness=thickness,
        lineType=cv2.LINE_AA
    )

    # BOTTOM-LEFT CORNER
    cv2.circle(
        MatLike,
        (
            x1 + border_radius,
            y2 - border_radius
        ),
        radius=border_radius,
        color=fill_color,
        thickness=thickness,
        lineType=cv2.LINE_AA
    )

    # BOTTOM-RIGHT CORNER
    cv2.circle(
        MatLike,
        (
            x2 - border_radius,
            y2 - border_radius
        ),
        radius=border_radius,
        color=fill_color,
        thickness=thickness,
        lineType=cv2.LINE_AA
    )


    """
    =========================================
    DRAW BOX CORNER BORDER
    =========================================
    Draw no-fill circles to create border.
    -----------------------------------------
    """
    if (border_color is not None and
        border_color is not None):

        # TOP-LEFT BORDER
        cv2.circle(
            MatLike,
            (
                x1 + border_radius,
                y1 + border_radius
            ),
            radius=border_radius,
            color=border_color,
            thickness=border_thickness,
            lineType=cv2.LINE_AA
        )


        # TOP-RIGHT BORDER
        cv2.circle(
            MatLike,
            (
                x2 - border_radius,
                y1 + border_radius
            ),
            radius=border_radius,
            color=border_color,
            thickness=border_thickness,
            lineType=cv2.LINE_AA
        )

        # BOTTOM-LEFT BORDER
        cv2.circle(
            MatLike,
            (
                x1 + border_radius,
                y2 - border_radius
            ),
            radius=border_radius,
            color=border_color,
            thickness=border_thickness,
            lineType=cv2.LINE_AA
        )

        # BOTTOM-RIGHT BORDER
        cv2.circle(
            MatLike,
            (
                x2 - border_radius,
                y2 - border_radius
            ),
            radius=border_radius,
            color=border_color,
            thickness=border_thickness,
            lineType=cv2.LINE_AA
        )

    # MAIN FILL
    cv2.rectangle(
        MatLike,
        (
            x1 + border_radius,
            y1
        ),
        (
            x2 - border_radius,
            y2
        ),
        color=fill_color,
        thickness=-1,
        lineType=cv2.LINE_AA
    )

    # LEFT SIDE FILL
    cv2.rectangle(
        MatLike,
        (
            x1,
            y1 + border_radius
        ),
        (
            x1 + border_radius,
            y2 - border_radius
        ),
        color=fill_color,
        thickness=thickness,
        lineType=cv2.LINE_AA
    )

    # RIGHT SIDE FILL
    cv2.rectangle(
        MatLike,
        (
            x2,
            y1 + border_radius
        ),
        (
            x2 - border_radius,
            y2 - border_radius
        ),
        color=fill_color,
        thickness=thickness,
        lineType=cv2.LINE_AA
    )


    """
    =========================================
    DRAW BOX SIDES BORDER
    =========================================
    Draw lines to create sides border.
    -----------------------------------------
    """
    if (border_color is not None and
        border_color is not None):
        # LEFT BORDER
        draw_line(
            MatLike,
            (
                x1,
                y1 + border_radius
            ),
            (
                x1,
                y2 - border_radius
            ),
            color=border_color,
            thickness=border_thickness,
            dash_size=dash_size,
            dash_gap=dash_gap
        )

        # RIGHT BORDER
        draw_line(
            MatLike,
            (
                x2,
                y1 + border_radius
            ),
            (
                x2,
                y2 - border_radius
            ),
            color=border_color,
            thickness=border_thickness,
            dash_size=dash_size,
            dash_gap=dash_gap
        )

        # TOP BORDER
        draw_line(
            MatLike,
            (
                x1 + border_radius,
                y1
            ),
            (
                x2 - border_radius,
                y1
            ),
            color=border_color,
            thickness=border_thickness,
            dash_size=dash_size,
            dash_gap=dash_gap
        )

        # BOTTOM BORDER
        draw_line(
            MatLike,
            (
                x1 + border_radius,
                y2
            ),
            (
                x2 - border_radius,
                y2
            ),
            color=border_color,
            thickness=border_thickness,
            dash_size=dash_size,
            dash_gap=dash_gap
        )
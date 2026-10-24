

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


def box(MatLike: np.ndarray,
        start_point: tuple[int, int],
        end_point: tuple[int, int],
        fill_color: tuple[int, int, int]|None=None,
        border_color: tuple[int, int, int]|None=None,
        border_thickness: int|None=None,
        dash_size: int=0,
        dash_gap: int=0,
        border_radius: int=0
        ) -> None:
    if fill_color is None and border_thickness is None:
        raise RuntimeError("Can't draw box")

    x1, y1 = start_point
    x2, y2 = end_point

    if fill_color:
        """
        =========================================
        BOX CORNERS
        =========================================
        """
        # TOP-LEFT CORNER
        cv2.ellipse(
            MatLike,
            (
                x1 + border_radius,
                y1 + border_radius
            ),
            axes=[border_radius]*2,
            angle=0,
            startAngle=180,
            endAngle=270,
            color=fill_color,
            thickness=-1
        )

        # TOP-RIGHT CORNER
        cv2.ellipse(
            MatLike,
            (
                x2 - border_radius,
                y1 + border_radius
            ),
            axes=[border_radius]*2,
            angle=0,
            startAngle=270,
            endAngle=360,
            color=fill_color,
            thickness=-1
        )

        # BOTTOM-LEFT CORNER
        cv2.ellipse(
            MatLike,
            (
                x1 + border_radius,
                y2 - border_radius
            ),
            axes=[border_radius]*2,
            angle=0,
            startAngle=90,
            endAngle=180,
            color=fill_color,
            thickness=-1
        )

        # BOTTOM-RIGHT CORNER
        cv2.ellipse(
            MatLike,
            (
                x2 - border_radius,
                y2 - border_radius
            ),
            axes=[border_radius]*2,
            angle=0,
            startAngle=0,
            endAngle=90,
            color=fill_color,
            thickness=-1
        )


        """
        =========================================
        BOX FILL
        =========================================
        """
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
            thickness=-1,
            lineType=cv2.LINE_AA
        )

        # RIGHT SIDE FILL
        cv2.rectangle(
            MatLike,
            (
                x2 - border_radius,
                y1 + border_radius
            ),
            (
                x2,
                y2 - border_radius
            ),
            color=fill_color,
            thickness=-1,
            lineType=cv2.LINE_AA
        )


    """
    =========================================
    DRAW BOX BORDER
    =========================================
    """
    if (border_color is not None and
        border_color is not None):
        # TOP-LEFT CORNER
        cv2.ellipse(
            MatLike,
            (
                x1 + border_radius,
                y1 + border_radius
            ),
            axes=[border_radius]*2,
            angle=0,
            startAngle=180,
            endAngle=270,
            color=border_color,
            thickness=border_thickness
        )

        # TOP-RIGHT CORNER
        cv2.ellipse(
            MatLike,
            (
                x2 - border_radius,
                y1 + border_radius
            ),
            axes=[border_radius]*2,
            angle=0,
            startAngle=270,
            endAngle=360,
            color=border_color,
            thickness=border_thickness
        )

        # BOTTOM-LEFT CORNER
        cv2.ellipse(
            MatLike,
            (
                x1 + border_radius,
                y2 - border_radius
            ),
            axes=[border_radius]*2,
            angle=0,
            startAngle=90,
            endAngle=180,
            color=border_color,
            thickness=border_thickness
        )

        # BOTTOM-RIGHT CORNER
        cv2.ellipse(
            MatLike,
            (
                x2 - border_radius,
                y2 - border_radius
            ),
            axes=[border_radius]*2,
            angle=0,
            startAngle=0,
            endAngle=90,
            color=border_color,
            thickness=border_thickness
        )

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


"""
=========================================
TEXT BOX
=========================================
Get text size and fitting text box
-----------------------------------------
"""
def text_box(MatLike: np.ndarray,
             text: str,
             org: tuple[int, int],
             fontFace: int,
             fontScale: float,
             fontColor: tuple[int, int, int],
             fontThickness: int,
             boxFill: tuple[int, int, int],
             border_color: tuple[int, int, int]|None=None,
             border_thickness: int|None=None,
             padding: list[int, int, int, int]=[1]*4,
             dash_size: int=0,
             dash_gap: int=0,
             border_radius: int=1
             ) -> None:

    (tw, th), baseline = cv2.getTextSize(
        text, fontFace, fontScale, fontThickness
    )

    tx, ty = org

    pad_left   = padding[0]
    pad_top    = padding[1]
    pad_right  = padding[2]
    pad_bottom = padding[3]

    x1 = tx - pad_left
    y1 = ty - th - pad_top

    x2 = tx + tw + pad_right
    y2 = ty + baseline + pad_bottom

    box(
        MatLike,
        (x1, y1),
        (x2, y2),
        boxFill,
        border_color,
        border_thickness,
        dash_size,
        dash_gap,
        border_radius
    )

    cv2.putText(
        MatLike,
        text,
        org,
        fontFace,
        fontScale,
        fontColor,
        fontThickness,
        cv2.LINE_AA
    )


def progress_bar(MatLike: np.ndarray,
                 start_point: tuple[int, int],
                 end_point: tuple[int, int],
                 max_value: float,
                 current_value: float,
                 background_fill: tuple[int, int, int],
                 bar_fill: tuple[int, int, int],
                 thickness: int,
                 border_color: tuple[int, int, int]|None=None
                 ) -> None:
    x1, _ = start_point
    x2, y2 = end_point

    bar_width = x2 - x1

    """
    Percentage must be in range [0; 1]
    """
    perc = max(
        0.0,
        min(current_value / max_value, 1.0)
    )
    fill_size = int(bar_width * perc)

    box(
        MatLike,
        start_point,
        end_point,
        fill_color=background_fill,
        border_color=None,
        border_thickness=None
    )

    if fill_size > 0:
        box(
            MatLike,
            start_point,
            (x1 + fill_size, y2),
            bar_fill
        )

    if border_color and thickness:
        box(
            MatLike,
            start_point,
            end_point,
            fill_color=None,
            border_color=border_color,
            border_thickness=thickness
        )
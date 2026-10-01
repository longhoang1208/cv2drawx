

import cv2
import numpy as np
from draw_line import draw_line


class RoundedCornerBox:
    def __init__(self,
                 MatLike: np.ndarray,
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
        self.MatLike = MatLike

        self.x1, self.y1 = start_point
        self.x2, self.y2 = end_point

        self.fill = fill_color if fill_color else None

        self.thickness = thickness

        if (border_thickness is not None and
            border_color is not None):
            self.border_color = border_color
            self.border_thickness = border_thickness
        else:
            self.border_color = None
            self.border_thickness = None

        self.border_radius = border_radius

        self.dash_gap = dash_gap
        self.dash_size = dash_size

        self.width = self.x2 - self.x1
        self.height = self.y2 - self.y1

    def draw(self):
        # TOP-LEFT CORNER
        cv2.circle(
            self.MatLike,
            (
                self.x1 + self.border_radius,
                self.y1 + self.border_radius
            ),
            radius=self.border_radius,
            color=self.fill,
            thickness=self.thickness,
            lineType=cv2.LINE_AA
        )

        # TOP-RIGHT CORNER
        cv2.circle(
            self.MatLike,
            (
                self.x2 - self.border_radius,
                self.y1 + self.border_radius
            ),
            radius=self.border_radius,
            color=self.fill,
            thickness=self.thickness,
            lineType=cv2.LINE_AA
        )

        # BOTTOM-LEFT CORNER
        cv2.circle(
            self.MatLike,
            (
                self.x1 + self.border_radius,
                self.y2 - self.border_radius
            ),
            radius=self.border_radius,
            color=self.fill,
            thickness=self.thickness,
            lineType=cv2.LINE_AA
        )

        # BOTTOM-RIGHT CORNER
        cv2.circle(
            self.MatLike,
            (
                self.x2 - self.border_radius,
                self.y2 - self.border_radius
            ),
            radius=self.border_radius,
            color=self.fill,
            thickness=self.thickness,
            lineType=cv2.LINE_AA
        )


        """
        =========================================
        DRAW BOX CORNER BORDER
        =========================================
        Draw no-fill circles to create border.
        -----------------------------------------
        """
        if (self.border_color is not None and
            self.border_color is not None):

            # TOP-LEFT BORDER
            cv2.circle(
                self.MatLike,
                (
                    self.x1 + self.border_radius,
                    self.y1 + self.border_radius
                ),
                radius=self.border_radius,
                color=self.border_color,
                thickness=self.border_thickness,
                lineType=cv2.LINE_AA
            )


            # TOP-RIGHT BORDER
            cv2.circle(
                self.MatLike,
                (
                    self.x2 - self.border_radius,
                    self.y1 + self.border_radius
                ),
                radius=self.border_radius,
                color=self.border_color,
                thickness=self.border_thickness,
                lineType=cv2.LINE_AA
            )

            # BOTTOM-LEFT BORDER
            cv2.circle(
                self.MatLike,
                (
                    self.x1 + self.border_radius,
                    self.y2 - self.border_radius
                ),
                radius=self.border_radius,
                color=self.border_color,
                thickness=self.border_thickness,
                lineType=cv2.LINE_AA
            )

            # BOTTOM-RIGHT BORDER
            cv2.circle(
                self.MatLike,
                (
                    self.x2 - self.border_radius,
                    self.y2 - self.border_radius
                ),
                radius=self.border_radius,
                color=self.border_color,
                thickness=self.border_thickness,
                lineType=cv2.LINE_AA
            )

        # MAIN FILL
        cv2.rectangle(
            self.MatLike,
            (
                self.x1 + self.border_radius,
                self.y1
            ),
            (
                self.x2 - self.border_radius,
                self.y2
            ),
            color=self.fill,
            thickness=-1,
            lineType=cv2.LINE_AA
        )

        # LEFT SIDE FILL
        cv2.rectangle(
            self.MatLike,
            (
                self.x1,
                self.y1 + self.border_radius
            ),
            (
                self.x1 + self.border_radius,
                self.y2 - self.border_radius
            ),
            color=self.fill,
            thickness=self.thickness,
            lineType=cv2.LINE_AA
        )

        # RIGHT SIDE FILL
        cv2.rectangle(
            self.MatLike,
            (
                self.x2,
                self.y1 + self.border_radius
            ),
            (
                self.x2 - self.border_radius,
                self.y2 - self.border_radius
            ),
            color=self.fill,
            thickness=self.thickness,
            lineType=cv2.LINE_AA
        )


        """
        =========================================
        DRAW BOX SIDES BORDER
        =========================================
        Draw lines to create sides border.
        -----------------------------------------
        """
        if (self.border_color is not None and
            self.border_color is not None):
            # LEFT BORDER
            draw_line(
                self.MatLike,
                (
                    self.x1,
                    self.y1 + self.border_radius
                ),
                (
                    self.x1,
                    self.y2 - self.border_radius
                ),
                color=self.border_color,
                thickness=self.border_thickness,
                dash_size=self.dash_size,
                dash_gap=self.dash_gap
            )

            # RIGHT BORDER
            draw_line(
                self.MatLike,
                (
                    self.x2,
                    self.y1 + self.border_radius
                ),
                (
                    self.x2,
                    self.y2 - self.border_radius
                ),
                color=self.border_color,
                thickness=self.border_thickness,
                dash_size=self.dash_size,
                dash_gap=self.dash_gap
            )

            # TOP BORDER
            draw_line(
                self.MatLike,
                (
                    self.x1 + self.border_radius,
                    self.y1
                ),
                (
                    self.x2 - self.border_radius,
                    self.y1
                ),
                color=self.border_color,
                thickness=self.border_thickness,
                dash_size=self.dash_size,
                dash_gap=self.dash_gap
            )

            # BOTTOM BORDER
            draw_line(
                self.MatLike,
                (
                    self.x1 + self.border_radius,
                    self.y2
                ),
                (
                    self.x2 - self.border_radius,
                    self.y2
                ),
                color=self.border_color,
                thickness=self.border_thickness,
                dash_size=self.dash_size,
                dash_gap=self.dash_gap
            )
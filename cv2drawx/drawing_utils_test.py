import cv2
import numpy as np
from drawing_utils import text_box

frame = np.zeros((720, 1280, 3), dtype=np.uint8)
frame.fill(200)

while True:
    # =======================================
    # DRAW TEXT BOX
    # =======================================
    text_box(
        frame,
"""
Lorem ipsum dolor sit amet
Lorem ipsum dolor sit amet
Lorem ipsum dolor sit amet
Lorem ipsum dolor sit amet""",
        (50, 200),
        cv2.FONT_HERSHEY_SIMPLEX,
        2, (0, 0, 0), 2,
        (255, 180, 20),
        (0, 0, 0), 3, [20, 50, 300, 50],
        dash_size=10, dash_gap=10, border_radius=10
    )

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
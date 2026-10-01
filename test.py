import cv2
import numpy as np
from box import RoundedCornerBox

frame = np.zeros((720, 1280, 3), dtype=np.uint8)
frame.fill(200)

while True:
    box = RoundedCornerBox(
        MatLike=frame,
        start_point=(50, 50),
        end_point=(500, 500),
        fill_color=(50, 50, 50),
        border_thickness=1,
        border_color=(0, 200, 230),
        border_radius=10,
        dash_size=15,
        dash_gap=10
    )
    box.draw()

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
# [PYTHON] cv2drawx

This is source code for the `cv2drawx` package project. This package includes new drawing features for opencv-python such as draw dash lines, rounded boxes, etc.


## Sample code

### Import packages
```python
import cv2
import numpy as np
from cv2drawx.box import RoundedCornerBox
from cv2drawx.draw_line import draw_line
```

### Setup a blank cv2 window
```python
frame = np.zeros((720, 1280, 3), dtype=np.uint8)
frame.fill(200)
```

### Draw elements
```python
while True:
    # =======================================
    # DRAW ROUNDED CORNER BOX
    # WITH DASH BORDER
    # =======================================
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

    # =======================================
    # DRAW DIAGONAL DASH LINE
    # =======================================
    draw_line(
        frame,
        (0, 0),
        (frame.shape[1], frame.shape[0]),
        (0, 0, 0),
        1, 10, 10
    )

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
```
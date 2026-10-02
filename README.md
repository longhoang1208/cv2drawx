# [PYTHON] cv2drawx

This is source code for the `cv2drawx` package project. This package includes new drawing features for opencv-python such as draw dash lines, rounded boxes, etc.


## Sample code

### Import packages
```python
import cv2
import numpy as np
from cv2drawx.drawing_utils import text_box
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
        (0, 0, 0), 3, [20, 50, 300, 80],
        dash_size=10, dash_gap=10, border_radius=10
    )

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
```

### Result
<img width="600" alt="result" src="https://github.com/user-attachments/assets/8f61ba64-af80-4c93-a77c-ff1bbee070f0" />

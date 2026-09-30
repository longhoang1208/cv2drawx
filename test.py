import cv2
import numpy as np

frame = np.zeros((720, 1280, 3), dtype=np.uint8)

while True:
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
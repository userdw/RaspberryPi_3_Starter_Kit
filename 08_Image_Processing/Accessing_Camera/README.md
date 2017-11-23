# [ENGLISH] Accessing Camera

It doesn't really appealing to us if we only process static images. Therefore in this part we will connect Raspberry Pi 3 with webcam. Accessing webcam through OpenCV is simple. The example is as below.

```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()

  # Our operations on the frame come here
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Display the resulting frame
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```

The implementation of [labelling](/08_Image_Processing/Labelling) with camera can be found [here](/08_Image_Processing/Accessing_Camera/camera).

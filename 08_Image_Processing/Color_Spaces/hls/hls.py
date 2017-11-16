import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

_projectDirectory = os.path.dirname(__file__)
_imagesDirectory = os.path.join(_projectDirectory, "images")

_images = []
for _root, _dirs, _files in os.walk(_imagesDirectory):
	for _file in _files:
		if _file.endswith(".jpg"):
			_images.append(os.path.join(_imagesDirectory, _file))

_imageIndex = 0
_imageTotal = len(_images)

_img1 = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED)
_fig = plt.figure("Color Spaces")
_gs = GridSpec(3, 3)

_fig1 = plt.subplot(_gs[0:3, 0:2])
_fig1.set_title("RGB Space")
_img1Show = cv2.cvtColor(_img1, cv2.COLOR_BGR2RGB) #for displaying purpose
plt.imshow(_img1Show)

_img1 = cv2.cvtColor(_img1, cv2.COLOR_BGR2HLS)
_img2, _img3, _img4 = cv2.split(_img1)

_fig2 = plt.subplot(_gs[0, 2])
_fig2.set_title("Hue Channel")
plt.imshow(_img2, cmap = "gray")

_fig3 = plt.subplot(_gs[1, 2])
_fig3.set_title("Lightness Channel")
plt.imshow(_img3, cmap = "gray")

_fig4 = plt.subplot(_gs[2, 2])
_fig4.set_title("Saturation Channel")
plt.imshow(_img4, cmap = "gray")

plt.tight_layout()
plt.show()

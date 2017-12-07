import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

_intensityBGR = 256

_projectDirectory = os.path.dirname(__file__)
_imagesDirectory = os.path.join(_projectDirectory, "images")

_images = []
for _root, _dirs, _files in os.walk(_imagesDirectory):
	for _file in _files:
		if _file.endswith(".jpg"):
			_images.append(os.path.join(_imagesDirectory, _file))

_imageIndex = 0
_imageTotal = len(_images)

_img = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED)
_img = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
_fig = plt.figure("Histogram Equalization")
_gs = GridSpec(16, 2)

_fig1 = plt.subplot(_gs[0:7, 0])
_fig1.set_title("Image")
plt.tight_layout()
_fig1ShowIt = plt.imshow(_img, cmap = "gray")

_fig2 = plt.subplot(_gs[0:7, 1])
_fig2.set_title("Histogram")
_hist = cv2.calcHist([_img], [0], None, [256], [0, 256]) / _img.size
plt.xlabel("Intensity")
plt.ylabel("PMF")
plt.tight_layout()
_fig2ShowIt = plt.plot(_hist)

_imgEqu = cv2.equalizeHist(_img)
_fig3 = plt.subplot(_gs[8:15, 0])
_fig3.set_title("Equalized Image")
plt.tight_layout()
_fig3ShowIt = plt.imshow(_imgEqu, cmap = "gray")

_fig4 = plt.subplot(_gs[8:15, 1])
_fig4.set_title("Equalized Histogram")
_histEqu = cv2.calcHist([_imgEqu], [0], None, [256], [0, 256]) / _imgEqu.size
plt.xlabel("Intensity")
plt.ylabel("PMF")
plt.tight_layout()
_fig4ShowIt = plt.plot(_histEqu)

plt.show()

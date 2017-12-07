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
_img = cv2.cvtColor(_img, cv2.COLOR_BGR2RGB)
_fig = plt.figure("Histogram")
_gs = GridSpec(15, 2)

_fig1 = plt.subplot(_gs[0:15, 0])
_fig1.set_title("Image")
plt.tight_layout()
_fig1ShowIt = plt.imshow(_img)

_fig2 = plt.subplot(_gs[0:15, 1])
_fig2.set_title("Histogram")
_histB = cv2.calcHist([_img], [0], None, [256], [0, 256]) / _img.size
_histG = cv2.calcHist([_img], [1], None, [256], [0, 256]) / _img.size
_histR = cv2.calcHist([_img], [2], None, [256], [0, 256]) / _img.size
plt.xlabel("Intensity")
plt.ylabel("PMF")
_intensityPlotBGR = np.arange(_intensityBGR)
plt.tight_layout()
_fig2ShowIt = plt.plot(_intensityPlotBGR, _histB, "b", _intensityPlotBGR, _histG, "g", _intensityPlotBGR, _histR, "r", alpha = 0.8)

plt.show()

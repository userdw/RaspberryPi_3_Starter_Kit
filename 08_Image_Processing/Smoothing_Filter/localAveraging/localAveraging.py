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

_img = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED)
_img = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
_imgHeight, _imgWidth = _img.shape

_fig = plt.figure("Local Averaging Smoothing")
_gs = GridSpec(1, 3)

_noiseMean = 0.0
_stdDeviation = 0.3
_nRollingWindow = 3

_fig1 = plt.subplot(_gs[0, 0])
_fig1.set_title("Original")
plt.imshow(_img, cmap = "gray")

_fimg = np.empty((_imgHeight, _imgWidth))
_fimg = cv2.normalize(_img, _fimg, 0.0, 1.0, cv2.NORM_MINMAX, cv2.CV_32F)

_fig2 = plt.subplot(_gs[0, 1])
_fig2.set_title("Deviation: " + str(_stdDeviation))
_fnoise = np.empty((_imgHeight, _imgWidth))
cv2.randn(_fnoise, _noiseMean, _stdDeviation)
_fresult = _fimg + _fnoise
_fresult = cv2.normalize(_fresult, _fresult, 0.0, 1.0, cv2.NORM_MINMAX, cv2.CV_32F)
plt.imshow(_fresult, cmap = "gray")

_fig3 = plt.subplot(_gs[0, 2])
_fig3.set_title("Window: " + str(_nRollingWindow))
_blurImg = cv2.blur(_fresult, (_nRollingWindow, _nRollingWindow))
plt.imshow(_blurImg, cmap = "gray")

plt.tight_layout()
plt.show()
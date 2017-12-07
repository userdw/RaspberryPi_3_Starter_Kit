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
_fig = plt.figure("Averaging Smoothing")
_gs = GridSpec(3, 4)

_noiseMean1 = 0.0
_stdDeviation1 = 0.5
_noiseMean2 = 0.0
_stdDeviation2 = 0.5
_noiseMean3 = 0.0
_stdDeviation3 = 0.5
_noiseMean4 = 0.0
_stdDeviation4 = 0.5

_fig1 = plt.subplot(_gs[0:3, 3])
_fig1.set_title("Original")
plt.imshow(_img, cmap = "gray")

_fimg = np.empty((_imgHeight, _imgWidth))
_fimg = cv2.normalize(_img, _fimg, 0.0, 1.0, cv2.NORM_MINMAX, cv2.CV_32F)

_fig2 = plt.subplot(_gs[0:1, 0])
_fig2.set_title("Deviation: " + str(_stdDeviation1))
_fnoise1 = np.empty((_imgHeight, _imgWidth))
cv2.randn(_fnoise1, _noiseMean1, _stdDeviation1)
_fresult1 = _fimg + _fnoise1
_fresult1 = cv2.normalize(_fresult1, _fresult1, 0.0, 1.0, cv2.NORM_MINMAX, cv2.CV_32F)
plt.imshow(_fresult1, cmap = "gray")

_fig3 = plt.subplot(_gs[2:3, 0])
_fig3.set_title("Deviation: " + str(_stdDeviation2))
_fnoise2 = np.empty((_imgHeight, _imgWidth))
cv2.randn(_fnoise2, _noiseMean2, _stdDeviation2)
_fresult2 = _fimg + _fnoise2
_fresult2 = cv2.normalize(_fresult2, _fresult2, 0.0, 1.0, cv2.NORM_MINMAX, cv2.CV_32F)
plt.imshow(_fresult2, cmap = "gray")

_fig4 = plt.subplot(_gs[0:1, 1])
_fig4.set_title("Deviation: " + str(_stdDeviation3))
_fnoise3 = np.empty((_imgHeight, _imgWidth))
cv2.randn(_fnoise3, _noiseMean3, _stdDeviation3)
_fresult3 = _fimg + _fnoise3
_fresult3 = cv2.normalize(_fresult3, _fresult3, 0.0, 1.0, cv2.NORM_MINMAX, cv2.CV_32F)
plt.imshow(_fresult3, cmap = "gray")

_fig5 = plt.subplot(_gs[2:3, 1])
_fig5.set_title("Deviation: " + str(_stdDeviation4))
_fnoise4 = np.empty((_imgHeight, _imgWidth))
cv2.randn(_fnoise4, _noiseMean4, _stdDeviation4)
_fresult4 = _fimg + _fnoise4
_fresult4 = cv2.normalize(_fresult4, _fresult4, 0.0, 1.0, cv2.NORM_MINMAX, cv2.CV_32F)
plt.imshow(_fresult4, cmap = "gray")

_fig6 = plt.subplot(_gs[0:3, 2])
_fig6.set_title("Averaging")
_fresult5 = (_fresult1 + _fresult2 + _fresult3 + _fresult4) / 4
plt.imshow(_fresult5, cmap = "gray")

plt.tight_layout()
plt.show()

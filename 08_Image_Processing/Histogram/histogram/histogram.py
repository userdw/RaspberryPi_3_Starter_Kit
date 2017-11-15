import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.widgets import Slider, Button

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

_img1 = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED)
_img1 = cv2.cvtColor(_img1, cv2.COLOR_BGR2RGB)
_fig = plt.figure("Histogram")
_gs = GridSpec(15, 2)

_fig1 = plt.subplot(_gs[0:15, 0])
_fig1.set_title("Image")
plt.tight_layout()
_fig1ShowIt = plt.imshow(_img1)

_fig2 = plt.subplot(_gs[0:15, 1])
_fig2.set_title("Histogram")
_histB = cv2.calcHist([_img1], [0], None, [256], [0, 256])
_histG = cv2.calcHist([_img1], [1], None, [256], [0, 256])
_histR = cv2.calcHist([_img1], [2], None, [256], [0, 256])
plt.xlabel("Intensity")
plt.ylabel("PMF")
plt.tight_layout()
_intensityPlotBGR = np.arange(_intensityBGR)
_fig2ShowIt = plt.plot(_intensityPlotBGR, _histB, "b", _intensityPlotBGR, _histG, "g", _intensityPlotBGR, _histR, "r", alpha = 0.8)
#_fig2ShowIt, = plt.plot(_hist)

'''_cumSumHist = np.zeros(256)
_cumSumhist = _cumulativeSumHist(_hist)
_imgEq = np.zeros(_img.size)
_imgEq = _mapImage(_img, _cumSumhist)

_fig3 = plt.subplot(_gs[7:13, 0])
plt.xticks([]), plt.yticks([]) #hide tick values on X and Y axis
_fig3.set_title("Equalized Image")
plt.tight_layout()
_fig3ShowIt = plt.imshow(_imgEq, cmap = "gray")

_fig4 = plt.subplot(_gs[7:13, 1])
_fig4.set_title("Equalized Histogram")
_hist = np.zeros(256)
_hist = _normalizedHistogram(_imgEq)
plt.xlabel("Intensity")
plt.ylabel("PMF")
plt.tight_layout()
_fig4ShowIt, = plt.plot(_hist)

_ChangeAx = _fig.add_axes([0.4, 0.02, 0.2, 0.05])
_changeButton = Button(_ChangeAx, "Change Image")
_changeButtonCid = _changeButton.on_clicked(_changeImage)'''

plt.show()
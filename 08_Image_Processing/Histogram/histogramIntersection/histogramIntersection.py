import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

_intensityHLS = 256
_intensityPlotHLS = np.arange(_intensityHLS)

_projectDirectory = os.path.dirname(__file__)
_imagesDirectory = os.path.join(_projectDirectory, "images")

def _intersection(_hist1, _hist2, _channel):
	_indexMin1 = _hist1 < _hist2
	_indexMin2 = _hist2 < _hist1
	_indexSame = _hist1 == _hist2
	return (np.sum(_hist1[_indexMin1]) + np.sum(_hist2[_indexMin2]) + np.sum(_hist1[_indexSame])) * _channel

_images = []
for _root, _dirs, _files in os.walk(_imagesDirectory):
	for _file in _files:
		if _file.endswith(".jpg"):
			_images.append(os.path.join(_imagesDirectory, _file))

_imageIndex = 0
_imageTotal = len(_images)

_img1 = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED)
_img1HLS = cv2.cvtColor(_img1, cv2.COLOR_BGR2HLS)
_img2 = cv2.imread(_images[_imageIndex + 1], cv2.IMREAD_UNCHANGED)
_img2HLS = cv2.cvtColor(_img2, cv2.COLOR_BGR2HLS)

_histH1 = cv2.calcHist([_img1HLS], [0], None, [256], [0, 256])
_histL1 = cv2.calcHist([_img1HLS], [1], None, [256], [0, 256])
_histS1 = cv2.calcHist([_img1HLS], [2], None, [256], [0, 256])
_histH2 = cv2.calcHist([_img2HLS], [0], None, [256], [0, 256])
_histL2 = cv2.calcHist([_img2HLS], [1], None, [256], [0, 256])
_histS2 = cv2.calcHist([_img2HLS], [2], None, [256], [0, 256])

_histHIntersect = cv2.compareHist(_histH1, _histH2, cv2.HISTCMP_INTERSECT)
_histLIntersect = cv2.compareHist(_histL1, _histL2, cv2.HISTCMP_INTERSECT)
_histSIntersect = cv2.compareHist(_histS1, _histS2, cv2.HISTCMP_INTERSECT)
_histIntersect = (_histHIntersect + _histLIntersect + _histSIntersect) / _img1.size

_fig = plt.figure("Histogram Intersection")
_gs = GridSpec(3, 3)

_fig1 = plt.subplot(_gs[0:3, 0])
_fig1.set_title("Image 1", color = "blue")
plt.tight_layout()
_fig1ShowIt = plt.imshow(cv2.cvtColor(_img1, cv2.COLOR_BGR2RGB))

_fig2 = plt.subplot(_gs[0, 1])
_fig2.set_title("Hue Histogram Intersection")
plt.xlabel("Intensity")
plt.ylabel("PMF")
plt.tight_layout()
_fig2ShowIt = plt.plot(_intensityPlotHLS, _histH1, "b", _intensityPlotHLS, _histH2, "r", alpha = 0.8)

_fig3 = plt.subplot(_gs[1, 1])
_fig3.set_title("Lightness Histogram Intersection")
plt.xlabel("Intensity")
plt.ylabel("PMF")
plt.tight_layout()
_fig3ShowIt = plt.plot(_intensityPlotHLS, _histL1, "b", _intensityPlotHLS, _histL2, "r", alpha = 0.8)

_fig4 = plt.subplot(_gs[2, 1])
_fig4.set_title("Saturation Histogram Intersection")
plt.xlabel("Intensity")
plt.ylabel("PMF")
plt.tight_layout()
_fig4ShowIt = plt.plot(_intensityPlotHLS, _histS1, "b", _intensityPlotHLS, _histS2, "r", alpha = 0.8)

_fig5 = plt.subplot(_gs[0:2, 2])
_fig5.set_title("Image 2", color = "red")
plt.tight_layout()
_fig5ShowIt = plt.imshow(cv2.cvtColor(_img2, cv2.COLOR_BGR2RGB))

_fig6 = plt.subplot(_gs[2, 2])
plt.xticks(())
plt.yticks(())
plt.tight_layout()
plt.text(0.5, 0.5, "Likelihood: " + str("%.5f" %_histIntersect), ha = "center", va = "center", size = 12)

plt.show()

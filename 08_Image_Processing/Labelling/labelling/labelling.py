import os, cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.widgets import Slider, Button
from scipy.ndimage import label

def _changeThreshold(val):
	global _percentThreshold
	global _threshold
	_percentThreshold = _slider.val
	_threshold = _percentThreshold / 100 * 255
	_changeImage(None)
	
def _changeMorphologyIterations1(val):
	global _morphIterations1
	_morphIterations1 = _sliderMor1.val
	_changeImage(None)
	
def _changeMorphologyIterations2(val):
	global _morphIterations2
	_morphIterations2 = _sliderMor2.val
	_changeImage(None)

def _changeImage(event):
	if event != None:
		global _imageIndex
		_imageIndex += 1
		if _imageIndex == _imageTotal:
			_imageIndex = 0
	
	_img = cv2.imread(_images[_imageIndex], cv2.IMREAD_UNCHANGED)
	_img = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
	_fig1ShowIt.set_array(_img)
	
	_ret, _imgBin = cv2.threshold(_img, _threshold, 255, cv2.THRESH_BINARY)
	_imgBin = cv2.erode(_imgBin, _kernel, iterations = int(_morphIterations1))
	_imgBin = cv2.dilate(_imgBin, _kernel, iterations = int(_morphIterations2))
	_labeledBin, _count = label(_imgBin)
	_fig2.set_title("Result: " + str(_count) + " coin(s)")
	
	_fig2ShowIt.set_array(_labeledBin)
	plt.draw()

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

_sliderInitVal = 50
_percentThreshold = _sliderInitVal
_threshold = _percentThreshold / 100 * 255
_kernel = np.ones((5, 5), np.uint8)

_slider2InitVal = 2
_morphIterations1 = _slider2InitVal

_slider3InitVal = 2
_morphIterations2 = _slider3InitVal

_fig = plt.figure("Labelling")
_gs = GridSpec(15, 2)
_fig1 = plt.subplot(_gs[0:10, 0])
_fig1.set_title("Original")
_fig1ShowIt = plt.imshow(_img, cmap = "gray")

_ret, _imgBin = cv2.threshold(_img, _threshold, 255, cv2.THRESH_BINARY)
_imgBin = cv2.erode(_imgBin, _kernel, iterations = int(_morphIterations1))
_imgBin = cv2.dilate(_imgBin, _kernel, iterations = int(_morphIterations2))
_labeledBin, _count = label(_imgBin)
_fig2 = plt.subplot(_gs[0:10, 1])
_fig2.set_title("Result: " + str(_count) + " coin(s)")
_fig2ShowIt = plt.imshow(_labeledBin, cmap = "nipy_spectral")

_sliderAx = _fig.add_axes([0.1, 0.2, 0.65, 0.05])
_slider = Slider(_sliderAx, "Threshold (%)", 0, 100, valinit = _sliderInitVal)
_sliderCid = _slider.on_changed(_changeThreshold)

_sliderAxMor1 = _fig.add_axes([0.1, 0.1, 0.35, 0.05])
_sliderMor1 = Slider(_sliderAxMor1, "Iterations 1", 0, 10, valinit = _slider2InitVal)
_sliderCidMor1 = _sliderMor1.on_changed(_changeMorphologyIterations1)

_sliderAxMor2 = _fig.add_axes([0.55, 0.1, 0.35, 0.05])
_sliderMor2 = Slider(_sliderAxMor2, "Iterations 2", 0, 10, valinit = _slider3InitVal)
_sliderCidMor2 = _sliderMor2.on_changed(_changeMorphologyIterations2)

_ChangeAx = _fig.add_axes([0.8, 0.2, 0.1, 0.05])
_changeButton = Button(_ChangeAx, "Change Image")
_changeButtonCid = _changeButton.on_clicked(_changeImage)

plt.show()
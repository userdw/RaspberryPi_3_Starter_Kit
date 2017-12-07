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
_gs = GridSpec(2, 2)

_fig1 = plt.subplot(_gs[0:2, 0])
_fig1.set_title("RGB Space")
_img1Show = cv2.cvtColor(_img1, cv2.COLOR_BGR2RGB) #for displaying purpose
plt.imshow(_img1Show)

_fig2 = plt.subplot(_gs[0:2, 1])
_fig2.set_title("Grayscale Space")
_img2 = cv2.cvtColor(_img1, cv2.COLOR_BGR2GRAY)
plt.imshow(_img2, cmap = "gray")

plt.tight_layout()
plt.show()

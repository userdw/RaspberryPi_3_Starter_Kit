# [ENGLISH] Histogram

Histogram is another way of understanding an image. It is a plot with x-axis ranging from 0 to 255 (usually) describing pixel intensity, and y-axis describing the number of pixels with corresponding intensity found in the image. By looking at the histogram of an image, we get intuition about contrast, brightness, intensity distribution etc. of that image.

Calculating histogram in OpenCV can be done using ```cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])```. The explanation for those parameters is as below:
1. ```images```: it is the source image of type uint8 or float32. it should be given in square brackets, ie, ```[img]```.
2. ```channels```: it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is ```[0]```. For color image, you can pass ```[0]```, ```[1]``` or ```[2]``` to calculate histogram of blue, green or red channel respectively.
3. ```mask```: mask image. To find histogram of full image, it is given as ```None```. But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask.
4. ```histSize```: this represents our BIN count. Need to be given in square brackets. For full scale, usually we pass ```[256]```.
5. ```ranges```: this is our RANGE. Usually, it is ```[0,256]```.

More theory about histogram can be found [here](https://en.wikipedia.org/wiki/Histogram).

## Plotting Histogram
The example of how to plot histogram of an image can be found [here](/08_Image_Processing/Histogram/histogram). The result can be shown as the image below.

<img src="/images/histogram.png" height="400">

## Histogram Equalization
Histogram equalization is a technique to stretch histogram so it doesn't confined to some specific range of values only. Histogram of a dark image tends to confined to low values, on the contrary histogram of a bright image tends to confined to high values. Compare two images below.

<img src="/images/poorLightHistogram.png" height="400">

<img src="/images/equalizedHistogram.png" height="400">

## Histogram Distance

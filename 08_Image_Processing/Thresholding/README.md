# [ENGLISH] Thresholding

The output from thresholding an image is binary image whose only have two possibilities for each pixels value. The value is either 0 (black-background) or 1 (white-foreground). Sometimes we represents 1 as 255. This leads to smaller image size and simpler way of analyzing it. Thresholding can be done using some methods as follow.

## Simple Thresholding
Simple thresholding, just as its name, works by following simple formula below.

<img src="/images/simpleThresholdingFormula.png" width="400">

When a pixel has value which is lower than the predetermined **th** then it will be set to 0. On the contrary, when a pixel has value which is higher than or equal to the predetermined **th** then it will be set as 255. Simple thresholding can be done by using ```cv2.threshold``` function and ```cv2.THRESH_BINARY``` as parameter.

<img src="/images/simpleThresholding.png" height="400">

The example code on how to do simple thresholding can be found [here](/08_Image_Processing/Thresholding/simpleThresholding).

## Adaptive Thresholding
Adaptive thresholding, unlike simple thresholding, is a thresholding which has a different value of **th** for each pixels. The value of **th** will be determined by pixel's neighbor. For block size of 3 (or kernel size of 3x3), the formula for determining **th** is as below.

<img src="/images/adThresholdingFormula.png" width="800">

Block size is usually (but not always) an odd number, because it will be easier to determine the center. When a pixel has value which is lower than the calculated **th** then it will be set to 0. On the contrary, when a pixel has value which is higher than or equal to the calculated **th** then it will be set as 255. Adaptive thresholding can be done by using ```cv2.adaptiveThreshold``` function and ```cv2.ADAPTIVE_THRESH_MEAN_C``` as parameter. ```cv2.adaptiveThreshold``` works only with odd number of block size.

<img src="/images/adaptiveThresholding.png" height="400">

The example code on how to do adaptive thresholding can be found [here](/08_Image_Processing/Thresholding/adaptiveThresholding).

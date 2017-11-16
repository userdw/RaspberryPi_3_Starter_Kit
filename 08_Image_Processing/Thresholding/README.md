# [ENGLISH] Thresholding

The output from thresholding an image is binary image whose only have two possibilities for each pixels value. The value is either 0 (black-background) or 1 (white-foreground). Sometimes we represents 1 as 255. This leads to smaller image size and simpler way of analyzing it. Thresholding can be done using some methods as follow.

## Simple Thresholding
Simple thresholding, just as its name, it works by following simple formula below.

<img src="/images/simpleThresholdingFormula.png" width="400">

When a pixel has value which is lower than the predetermined **th** then it will be set to 0. On the contrary, when a pixel has value which is higher than or equal to the predetermined **th** then it will be set as 255. Simple thresholding can be done by using ```cv2.threshold``` function and ```cv2.THRESH_BINARY``` as parameter.

<img src="/images/simpleThresholding.png" width="400">

The example code on how to do simple thresholding can be found [here](/08_Image_Processing/Thresholding/simpleThresholding).

## Adaptive Thresholding
Grayscale is one of the most popular color space used in image processing. Grayscale is simpler to process since it is represented in 1 channel, compared to 3 channels in color image. Most information in an image usually can be found through its luminance, and grayscale capture the luminance pretty well. In fact the conversion formula from RGB/BGR to grayscale used in OpenCV's function is the same with conversion formula from RGB/BGR to Y (luminance) component in YCrCb color space. Not only grayscale is simpler to compute, but it also captures a lot of information within an image. To convert a BGR image to grayscale we just need to use ```cv2.COLOR_BGR2GRAY``` as ```cv2.cvtColor``` parameter. Below is the code to convert BGR color space to grayscale. The code can be found [here](/08_Image_Processing/Color_Spaces/grayscale).

<img src="/images/grayscaleFormula.png" width="500">

<img src="/images/grayscaleSpace.png" height="400">

## HLS
HLS (Hue, Lightness, Saturation) color space is another way to represent colors. HLS color space defines colors more naturally. Hue specifies the base color, the other two values then let you specify the saturation of that color and how bright the color should be. HLS color space is cylindrical, and can be represented as the image below. To convert a BGR image to HLS we just need to use ```cv2.COLOR_BGR2HLS``` as ```cv2.cvtColor``` parameter. The code can be found [here](/08_Image_Processing/Color_Spaces/hls).

<img src="/images/HLS_Color_Space.png" height="200">

credits to: https://commons.wikimedia.org/wiki/User:SharkD

<img src="/images/hlsFormula.jpg" width="500">

If the value of H after calculation is less than 0, we will add 360 to it. The outputs from the above equation will be:
* 0 <= L <= 1
* 0 <= S <= 1
* 0 <= H <= 360

Since we usually use 8-bit depth for each channel, the value of L and S will be scaled-up to 0 - 255, and H will be divided by 2 so it will fit the 8-bit range.

<img src="/images/hlsSpace.png" height="400">

## YCrCb
YCrCb color space is used because of RGB color space has a lot of redudancy thus inefficient to be used as representation for storage and transmission. YCrCb is a 3 channels color space with Y, Cr, and Cb components. Y represents luminance, and Cr Cb represents chroma. YCrCb is a 3D color space and can be represented as the image below. To convert a BGR image to YCrCb we just need to use ```cv2.COLOR_BGR2YCrCb``` as ```cv2.cvtColor``` parameter. The code can be found [here](/08_Image_Processing/Color_Spaces/ycrcb).

<img src="/images/YCrCb_Color_Space.jpg" height="400">

credits to: http://www.personal-view.com/talks/profile/1243/tida

<img src="/images/ycrcbFormula.png" width="500">

<img src="/images/ycrcbSpace.png" height="400">

As we can see in the image above that most of the information can be captured from Y (luminance) component. If we look at it closer the image of Y component is the same with grayscale. That's because the formula used in converting RGB to grayscale is the same with formula used to calculate Y component in YCrCb color space.

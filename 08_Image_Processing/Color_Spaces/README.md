# [ENGLISH] Color Spaces

<img src="/images/Lenna.jpg" height="400">

Colors don't exist and they don't have any form as they are just what we perceive with our vision. A color model or color space is an abstract mathematical model describing the way colors can be represented as tuples of numbers. One color space is better suited for some cases than the other, therefore it's important for us to know some of the color spaces available.

## RGB
RGB (Red, Green, Blue) is the most usual way to represent a color image. It came from the philosophy that everything start from black. A given color can be produced through emitting and combining red, green, and blue light together with specific intensity for each light. OpenCV use BGR instead of RGB. They are basically the same in value but different in order. As for why OpenCV use BGR, [this article](https://www.learnopencv.com/why-does-opencv-use-bgr-color-format/) might give you the reason. You can get each channel value with built-in OpenCV function ```cv2.split```. The code can be found [here](/08_Image_Processing/Color_Spaces/rgb).

<img src="/images/rgbSpace.png" height="400">

## Grayscale
Grayscale is one of the most popular color space used in image processing. Grayscale is simpler to process since it is represented in 1 channel, compared to 3 channels in color image. Most information in an image usually can be found through its luminance, and grayscale capture the luminance pretty well. In fact the conversion formula from RGB/BGR to grayscale used in OpenCV's function is the same with conversion formula from RGB/BGR to Y (luminance) component in YCrCb color space. Not only grayscale is simpler to compute, but it also captures a lot of information within an image. To convert a BGR image to grayscale we just need to use ```cv2.COLOR_BGR2GRAY``` as ```cv2.cvtColor``` function parameter. Below is the code to convert BGR color space to grayscale. The code can be found [here](/08_Image_Processing/Color_Spaces/grayscale).

<img src="/images/grayscaleFormula.png" width="500">

<img src="/images/grayscaleSpace.png" height="400">

## HLS
HLS (Hue, Lightness, Saturation) color space is another way to represent colors. HLS color space defines colors more naturally. Hue specifies the base color, the other two values then let you specify the saturation of that color and how bright the color should be. HLS color space is cylindrical, and can be represented as the image below. To convert a BGR image to HLS we just need to use ```cv2.COLOR_BGR2HLS``` as ```cv2.cvtColor``` function parameter. The code can be found [here](/08_Image_Processing/Color_Spaces/hls).

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
YCrCb color space is used because of RGB color space has a lot of redudancy thus inefficient to be used as representation for storage and transmission. YCrCb is a 3 channels color space with Y, Cr, and Cb components. Y represents luminance, and Cr Cb represents chroma. YCrCb is a 3D color space and can be represented as the image below. To convert a BGR image to YCrCb we just need to use ```cv2.COLOR_BGR2YCrCb``` as ```cv2.cvtColor``` function parameter. The code can be found [here](/08_Image_Processing/Color_Spaces/ycrcb).

<img src="/images/YCrCb_Color_Space.jpg" height="400">

credits to: http://www.personal-view.com/talks/profile/1243/tida

<img src="/images/ycrcbFormula.png" width="500">

<img src="/images/ycrcbSpace.png" height="400">

As we can see in the image above that most of the information can be captured from Y (luminance) component. If we look at it closer, the image of Y component is the same with grayscale. That's because the formula used in converting RGB to grayscale is the same with formula used to calculate Y component in YCrCb color space.

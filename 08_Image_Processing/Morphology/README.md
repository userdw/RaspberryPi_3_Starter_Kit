# [ENGLISH] Morphology

Sometimes we are using binary images because we only interested in object's form. This case can be found in industrial process such as counting objects on conveyor belt, sorting products, etc. Morphological transformations, commonly performed on binary image, are some simple operations based on the image shape. Some basic morphological transformations are:
* Erosion.
* Dilation.
* Opening.
* Closing.

Before we continue, there are some terminologies used in morphology:
* Foreground: pixel with value of 1.
* Background: pixel with value of 0.
* Structuring element: kernel that will slide through an image.

## Structuring Element
Structuring element (also called as kernel) is simply a mask that allows us to define arbitrary neighborhood structures. Structure element **will slide through the image**.

<img src="/images/structElement.png" width="600">

## Erosion
Erosion, just as its name, will erode the boundaries of foreground object. A pixel in the original image will be considered as foreground only if all the pixels under the kernel is foreground as well, otherwise it is eroded (set to background). Erosion can be done by using ```cv2.erode``` function.

<img src="/images/erosionIllustration.png" width="600">

## Dilation
Dilation is the opposite of erosion, it will increases the region of foreground. Usually in noise removal, erosion is followed by dilation. When we erode an image, the noise will get removed as well as some part of our objects' area. To make our objects to have the same size as before we erode the image, we dilate it. Since the noise is gone, they won't come back. Dilation can be done by using ```cv2.dilate``` function.

<img src="/images/dilationIllustration.png" width="600">

## Opening
Opening is erosion followed by dilation. Opening is useful in removing noise. Opening can be done by using ```cv2.morphologyEx``` function with ```cv2.MORPH_OPEN``` as the parameter.

## Closing
Closing is dilation followed by erosion. Closing is useful in closing small holes (or black area) inside our foreground objects. Closing can be done by using ```cv2.morphologyEx``` function with ```cv2.MORPH_CLOSE``` as the parameter.

## Example of Morphology Transformation
The image below is the result of doing simple thresholding on image of coins.

<img src="/images/morphologyExampleBefore.png" height="400">

As we can see in the image above that the output is noisy. We can remove the noise with opening transformation. After opening transformation the output image is as below.

<img src="/images/morphologyExampleAfter.png" height="400">

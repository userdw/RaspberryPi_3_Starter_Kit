# [ENGLISH] Smoothing Filter

Two most commonly encountered type of noise on images are Gaussian noise (or white noise) and salt-and-pepper noise.

<img src="/images/lennaNoise.png" width="600">

Noise can corrupt pixel's value thus can cause misinterpretation of information. White noise on image is due to natural processes such as electrical noise during acquisition. As for salt-and-pepper noise, it can be caused by malfunctioning of camera's sensor cells. White noise and salt-and-pepper noise [Probability Density Function (PDF)](https://en.wikipedia.org/wiki/Probability_density_function) is as below.

<img src="/images/noisePdf.png" width="600">

PDF gives us probability of pixel's value. In white noise the probability of pixel's value is in the form of Gaussian distribution. For salt-and-pepper noise the probability is in the form of impulse which is either lowest intensity (black) or highest intensity (white) deppending on its intensity (```g```).

We can enhance the image in some ways to get a better information from it. Depending on the condition and the type of noise, we can use:
* Image averaging
* Local averaging (mean filter)
* Median filter

## Image Averaging
Image averaging can be used if we have some images of the exactly same scene, but with different white noise. The concept is very simple, we just need to add all those images together then divide it by the number of images. The example code can be found [here](/08_Image_Processing/Smoothing_Filter/averaging).

<img src="/images/imageAveraging.png" height="400">

The drawback of this method is that we need to have multiple images of the exactly same scene. This method can be applied for cases such as if our camera and scene are static.

## Local averaging (mean filter)
Local averaging or mean filter works by averaging pixel's value and its neighbors. The calculated value will be used to update the pixel's value. Example of local averaging of ```3x3``` window is as below.

<img src="/images/meanFilter.png" width="700">

Local averaging can be done by using ```cv.blur``` function.

<img src="/images/localAveragingResult.png" height="400">

The example code can be found [here](/08_Image_Processing/Smoothing_Filter/imageAveraging).

## Median filter
Both image averaging and local averaging works by averaging pixels value, thus reducing the noise. The noise itself is still presents, but less apparent. Both filters are suitable to filter white noise since the actual pixel's value won't be "far" from its noisy value. 

Salt-and-pepper is another different story. Since noisy pixels will have either lowest intensity or highest intensity, averaging them won't do much. Therefore we will use median filter instead of local averaging.

<img src="/images/medianFilter3.png" width="400">

Median filtering can be done by using ```cv.medianBlur``` function.

<img src="/images/medianFilterResult.png" height="400">

The example code can be found [here](/08_Image_Processing/Smoothing_Filter/medianFilter).

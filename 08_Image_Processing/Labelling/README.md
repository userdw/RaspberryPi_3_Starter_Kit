# [ENGLISH] Labelling

As human we have incredible ways of thinking and analyzing everything in just a fraction of second with our vision alone. For example if we are shown the image of circles as below, we can automatically count them.

<img src="/images/targetCount.png" height="300">

Raspberry Pi 3 (or computer) can't do that as long as we don't tell them how. For that matter, we can use [connected-component labelling](https://en.wikipedia.org/wiki/Connected-component_labeling) algorithm. In Python we can do connected-component labelling with the help of ```label``` function found in SciPy package. The result of doing connected-component labelling on the image above is as below.

<img src="/images/labellingExample.png" height="400">

# [ENGLISH] Labelling

As human we have incredible ways of thinking and analyzing everything around us in just a fraction of second. For example if we are shown the image of circles as below, we can automatically count them.

<img src="/images/targetCount.png" height="300">

Raspberry Pi 3 (or computer) can't do that as long as we don't tell them how. We can use [connected-component labelling](https://en.wikipedia.org/wiki/Connected-component_labeling) algorithm, and the most commonly used is two-pass algorithm.

In Python we can do connected-component labelling with the help of ```label``` function found in SciPy package.

<img src="/images/targetCount.png" height="400">

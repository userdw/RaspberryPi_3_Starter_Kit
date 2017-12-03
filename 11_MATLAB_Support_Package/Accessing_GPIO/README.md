# [ENGLISH] Accessing GPIO
Raspberry Pi 3 comes with GPIO pins and we can use them to interface with external circuits such as sensors or actuators. First we want to know pins that are available, and we can do it by running the commands below.

```matlab
rpi = raspi() %initializing Raspberry Pi connection
showPins(rpi) %show available pins on Raspberry Pi
```

If we are using Raspberry Pi IO Expansion Shield, we can use the pin table below as reference.

<img src="/images/matlabPins.png" height="500">

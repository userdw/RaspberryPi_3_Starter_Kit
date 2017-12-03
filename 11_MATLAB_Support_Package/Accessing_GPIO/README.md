# [ENGLISH] Accessing GPIO
Raspberry Pi 3 comes with GPIO pins and we can use them to interface with external circuits such as sensors or actuators. First we want to know pins that are available, and we can do it by running the commands below.

```matlab
rpi = raspi() %initializing Raspberry Pi connection
showPins(rpi) %show available pins on Raspberry Pi
```

The output should be as below.

<img src="/images/pins.jpg" height="400">

After knowing that available LED is ```'led0'```, we can now try to blink it by running the commands below.

```matlab
for i = 1:5
  writeLED(rpi, 'led0', true)
  pause(1)
  writeLED(rpi, 'led0', false)
  pause(1)
end
```

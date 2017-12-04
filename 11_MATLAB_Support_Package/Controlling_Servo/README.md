# [ENGLISH] Controlling Servo
Raspberry Pi 3 comes with GPIO pins and we can use them to interface with external circuits such as sensors or actuators. First we want to know pins that are available, and we can do it by running the commands below.

```matlab
rpi = raspi() %initializing Raspberry Pi connection
showPins(rpi) %show available pins on Raspberry Pi
```

If we are using Raspberry Pi IO Expansion Shield, we can use the pin table below as reference.

<img src="/images/matlabPins.png" height="500">

## Configuring Pins
Pins need to be configured before they can be used. We can use command below to configure a pin.

```matlab
%configurePin(rpi, pinNumber, mode)
configurePin(rpi, 5, 'DigitalOutput') %mode can be either 'DigitalInput', 'DigitalOutput', or 'PWM'
configurePin(rpi, 12, 'DigitalInput')
```

If we want to know which mode a pin currently using, we can run the command below.

```matlab
%pinMode = configurePin(rpi, pinNumber)
pinMode5 = configurePin(rpi, 5) %pinMode value is the mode which currently being used
pinMode12 = configurePin(rpi, 12)
```

## Writing to Digital Pin
We can write digital value to pin by running the command below.

```matlab
%writeDigitalPin(rpi, pinNumber, value)
writeDigitalPin(rpi, 5, true) %value can be either true or false
```

## Reading from Digital Pin
We can read digital value from pin by running the command below.

```matlab
%pinValue = readDigitalPin(rpi, pinNumber)
pinValue = readDigitalPin(rpi, 12) %pinValue value is either true or false, which is the current logic state of the pin
```

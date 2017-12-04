# [ENGLISH] Controlling Servo
In this part we will try to control a servo motor attached on Raspberry Pi 3 through MATLAB. We can initialize servo connection and its parameters by running the code below.

```matlab
rpi = raspi()
rpiServo = servo(rpi, 23, 'MinPulseDuration',6.00e-4,'MaxPulseDuration',2.4e-3) %initializing servo connection on pin 23 (pin 17 on shield) with minimum pulse 0.6 ms and maximum pulse 2.4 ms
```

Note that usually pulse needed to control servo is ranged from 1 ms to 2 ms. In our case, the servo included in Raspberry Pi 3 Starter Kit use a slightly different range, which is 0.6 ms to 2.4 ms.

After the initialization is done, we can control the servo by using ```writePosition``` function. The example is as below.

```matlab
writePosition(rpiServo, 0) %move servo to 0 degree
writePosition(rpiServo, 45) %move servo to 45 degree
writePosition(rpiServo, 90) %move servo to 90 degree
writePosition(rpiServo, 135) %move servo to 135 degree
writePosition(rpiServo, 180) %move servo to 180 degree
```

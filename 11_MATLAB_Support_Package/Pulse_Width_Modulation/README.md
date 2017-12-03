# [ENGLISH] Pulse Width Modulation
With MATLAB, we can use each of every available Raspberry Pi 3's pins to output PWM signal. In order to do so, we need to configure the pin to work in ```PWM``` mode by running the command below.

```matlab
rpi = raspi()
configurePin(rpi, 13, 'PWM')
```

## Setting PWM Frequency
We can set the PWM frequency by running the command below.

```matlab
%writePWMFrequency(rpi, pinNumber, frequency)
writePWMFrequency(rpi, 13, 2000) %set the frequency to be 2000 hertz
```

## Setting PWM Duty Cycle
We can set the PWM duty cycle by running the command below.

```matlab
%writePWMDutyCycle(rpi, pinNumber, dutyCycle)
writePWMDutyCycle(rpi, 13, 0.3) %set the duty cycle to be 0.3, which is 30% of the square wave is high and the other 70% is low
```

## Writing PWM Voltage
We can write average voltage PWM output by running the command below.

```matlab
%writePWMVoltage(rpi, pinNumber, voltage)
writePWMVoltage(rpi, 13, 1.65) %set the average voltage of PWM pin to be 1.65, which is 50% duty cycle
```

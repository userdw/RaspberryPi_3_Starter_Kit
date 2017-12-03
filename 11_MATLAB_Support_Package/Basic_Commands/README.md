# [ENGLISH] Basic Commands
Some basic commands that are available in MATLAB are as below.

## Initializing Connection:
Before we can controlling our Raspberry Pi from MATLAB, we need to initialize the connection first. We can do it by running the command below.

```matlab
rpi = raspi()
```

## Disconnecting from Raspberry Pi:
Disconnecting Raspberry Pi is as simple as deleting a variable. We can delete a variable in MATLAB by running the command below.

```matlab
clear rpi %
```

## Execute Raspberry Pi's Shell Commands from MATLAB:
Sometimes we need to execute shell commands in Raspberry Pi from MATLAB. We can do so by running the command below.

```matlab
system(rpi, 'ls')
```

`'ls'` is a shell command that works the same as `dir` in Windows Command Prompt. We can subtitute it for another commands. If we need to run the shell command as superuser, we can add `'sudo'` as third parameter of `system` function.

```matlab
rpi = raspi() %initializing Raspberry Pi connection
showLEDs(rpi) %show available LEDs on Raspberry Pi
```

The output should be as below.

<img src="/images/leds.jpg" height="300">

After knowing that available LED is ```'led0'```, we can now try to blink it by running the commands below.

```matlab
for i = 1:5
  writeLED(rpi, 'led0', true)
  pause(1)
  writeLED(rpi, 'led0', false)
  pause(1)
end
```

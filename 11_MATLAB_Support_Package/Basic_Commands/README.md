# [ENGLISH] Basic Commands
Some basic commands that are available in MATLAB for interfacing with Raspberry Pi are as below.

## Initializing Connection:
Before we can controlling our Raspberry Pi from MATLAB, we need to initialize the connection first. We can do it by running the command below.

```matlab
rpi = raspi()
```

## Disconnecting:
Disconnecting Raspberry Pi is as simple as deleting a variable. We can delete a variable in MATLAB by running the command below.

```matlab
clear rpi
```

## Execute Shell Commands from MATLAB:
Sometimes we need to execute shell commands in Raspberry Pi from MATLAB. We can do so by running the command below.

```matlab
system(rpi, 'ls')
```

`ls` is a shell command that works the same as `dir` in Windows Command Prompt. We can subtitute it for another commands.

## Restart:
Restarting Raspberry Pi can be done by running the command below.

```matlab
system(rpi, 'sudo reboot')
```

## Shutdown:
Turning off Raspberry Pi without shutting it down is a bad practice since it can lead to corrupt data. Before turning Raspberry Pi off, we can shut it down by running the command below.

```matlab
system(rpi, 'sudo shutdown -h now')
```

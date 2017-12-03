# [ENGLISH] Project 11: MATLAB Support Package
As all of us must already know that MATLAB is one of the most popular tools available for conducting research, usually that involves making a simulation or analyzing data. The creator of MATLAB, MathWorks, is aware of the existence of Raspberry Pi and see the possibilities for combining MATLAB with it.

In this project we will try to connect and control our Raspberry Pi 3 from MATLAB. The connection between Raspberry Pi 3 and MATLAB will be done through MATLAB Support Package for Raspberry Pi Hardware. MATLAB has began its support since R2014b version, which supports Raspberry Pi Model B+. **As of Raspberry Pi 3, the support has been released since April 2016 in R2016a version**. For more information about MATLAB Support Package for Raspberry Pi Hardware release note, please visit [this link](https://www.mathworks.com/help/supportpkg/raspberrypiio/release-notes.html).

Installation of MATLAB Support Package for Raspberry Pi Hardware can be done by following this [link](https://www.mathworks.com/help/supportpkg/raspberrypiio/ug/install-support-for-raspberry-pi-hardware.html). You will need to be logged in on your MathWorks account to complete the installation.

After the installation process done, we can insert the SD card to be configured followed by clicking **Add-Ons > Manage Add-Ons**.

<img src="/images/setup1.png" width="300">

Click **Setup** on the MATLAB Support Package for Raspberry Pi Hardware.

<img src="/images/setup2.png" width="750">

Choose the appropriate model for Raspberry Pi we are currently using. In this case, it's Raspberry Pi 3 Model B.

<img src="/images/setup3.png" width="500">

Choose the network configuration.

<img src="/images/setup4.png" width="500">

Choose the SD card's drive letter.

<img src="/images/setup5.png" width="500">

Click **Write** to start burning the Raspbian into the SD card.

<img src="/images/setup6.png" width="500">

After the process finished we can now connect Raspberry Pi to our network.

When Raspberry Pi has been connected, you can type and run ```rpi = raspi()```. If there are no mistakes, the output should be the same as below.

<img src="/images/testingMATLABRPi.png" width="600">

## The topics which will be included in this project are:
* [Basic Commands](/11_MATLAB_Support_Package/Basic_Commands).
* [Accessing LED](/11_MATLAB_Support_Package/Accessing_LED).
* [Accessing GPIO](/11_MATLAB_Support_Package/Accessing_GPIO).
* [Pulse Width Modulation](/11_MATLAB_Support_Package/Pulse_Width_Modulation).
* [Controlling Servo](/11_MATLAB_Support_Package/Controlling_Servo).

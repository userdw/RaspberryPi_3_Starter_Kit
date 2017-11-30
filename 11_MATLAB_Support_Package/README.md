# [ENGLISH] Project 11: MATLAB Support Package
As all of us must already know that MATLAB is one of the most popular tools available for conducting research, usually that involves making a simulation or analyzing data. The creator of MATLAB, MathWorks, is aware of the existence of Raspberry Pi and see the possibilities for combining MATLAB with it.

In this project we will try to connect and control our Raspberry Pi 3 with MATLAB. The connection between Raspberry Pi 3 and MATLAB will be done through MATLAB Support Package for Raspberry Pi Hardware. MATLAB has began its support since R2014b version, which supports Raspberry Pi Model B+. **As of Raspberry Pi 3, the support has been released since April 2016 in R2016a version**. For more information about MATLAB Support Package for Raspberry Pi Hardware release note, please visit [this link](https://www.mathworks.com/help/supportpkg/raspberrypiio/release-notes.html).

Installation of MATLAB Support Package for Raspberry Pi Hardware can be done by following this [link](https://www.mathworks.com/help/supportpkg/raspberrypiio/ug/install-support-for-raspberry-pi-hardware.html). You will need to be logged in on your MathWorks account to complete the installation.

After the installation process done, we can insert the SD card to be configured followed by clicking **Add-Ons > Manage Add-Ons**.

<img src="/images/setup1.png" width="300">

Click **Setup** on the MATLAB Support Package for Raspberry Pi Hardware.

<img src="/images/setup2.png" width="600">

Choose the appropriate model for Raspberry Pi we are currently using. In this case, it's Raspberry Pi 3 Model B.

<img src="/images/setup3.png" width="500">

Choose the network configuration.

<img src="/images/setup4.png" width="500">

Choose the SD card's drive letter.

<img src="/images/setup5.png" width="500">

Klik **Write** to start burning the Raspbian into the SD card.

<img src="/images/setup6.png" width="500">

After the process finished we can now connect Raspberry Pi to our network.

When Raspberry Pi has been connected, you can type and run ```rpi = raspi()```. If there are no mistakes, the output should be the same as below.

* 

### In this project you will need:
* Raspbery Pi 3 (1),
* Raspberry Pi IO Expansion Shield (1),
* LED Module (1).

<img src="/images/blinking and fading LED.png" height="400">

### Assemble the modules following these steps:
1. Plug the Raspberry Pi IO Expansion Shield to the top of  Raspberry Pi 3,
2. Plug the LED Module to the header on the Raspberry Pi IO Expansion Shield labelled **9**,
3. Run the [Blinking_and_Fading_a_LED](/01_Blinking_and_Fading_a_LED/Blinking_and_Fading_a_LED.py) code in Raspberry Pi 3 with Python. 

If there are no mistakes, the LED Module should start blinking then increase and fade in its brightness.

# [BAHASA INDONESIA] Proyek 1: Blinking and Fading a LED
Hampir semua awal dari eksplorasi dan pengembangan yang dilakukan pada embedded device dimulai dari mengedipkan LED, di mana hal tersebut digunakan untuk memastikan bahwa board kita dapat bekerja dengan baik, serta bagi kita agar mengetahui bagaimana bentuk kode yang paling sederhana untuk mengakses output pin dari board tersebut. Hal yang sama akan kita lakukan untuk perjalanan eksplorasi Raspberry Pi 3 kita. Melalui proyek ini, kami berharap Anda akan mendapatkan gambaran bahwa mengendalikan output pin pada Raspberry Pi 3 adalah hal yang mudah dilakukan. Bahasa pemrograman yang akan digunakan adalah Python. Python merupakan bahasa pemrograman yang bersahabat bagi programmer awal yang baru saja memasuki dunia pemrograman. Adapun sintaks Python yang mudah dibaca akan membuat Anda dapat mulai mengendalikan output pin pada Raspberry Pi 3 dengan cepat.

### Modul-modul yang dibutuhkan pada proyek ini:
* Raspberry Pi 3 (1),
* Raspberry Pi IO Expansion Shield (1),
* LED Module (1).

<img src="/images/blinking and fading LED.png" height="400">

### Hubungkan modul-modul di atas mengikuti langkah-langkah di bawah ini:
1. Pasang Raspberry Pi IO Expansion Shield di atas Raspberry Pi 3,
2. Hubungkan LED Module ke header Raspberry Pi IO Expansion Shield yang berlabel **9**,
3. Jalankan kode program [Blinking_and_Fading_a_LED](/01_Blinking_and_Fading_a_LED/Blinking_and_Fading_a_LED.py) di Raspberry Pi 3 menggunakan Python. 

Apabila tidak terdapat kesalahan, maka LED Module akan berkedip kemudian tingkat kecerahannya akan berubah.

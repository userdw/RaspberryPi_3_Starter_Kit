# [ENGLISH] Raspberry Pi 3 Starter Kit
This repository has been created as the companion for Raspberry Pi 3 Starter Kit. Raspberry Pi 3 Starter Kit itself is a suitable start point for both hobbyist and academist alike to start exploring the possibilities offered by this inexpensive mini PC platform. For more information about the product please visit links below:
* [Raspberry Pi 3 Starter Kit](http://digiwarestore.com/en/) - Raspberry Pi Starter Kit's product page.
* [Raspberry Pi](https://www.raspberrypi.org/) - Raspberry Pi's official website.

## Initial Configuration
* The steps below was tested on **RASPBIAN STRETCH WITH DESKTOP** and computer/laptop with Windows OS
* Get the latest Raspbian [here](https://www.raspberrypi.org/downloads/raspbian/). Follow the steps mentioned [here](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md) to install Raspbian into the SD card.
* Accessing Raspberry Pi remotely through SSH is disabled by default. To enable it insert the SD card to the computer/laptop. Make a file named ```ssh``` and place it into the boot partition of the SD card without any extension. After adding the ```ssh``` file, insert the SD card into Raspberry Pi then boot it up. It will take some time until you enter the Raspberry Pi's Desktop for the first time.
* If you have access to router, you can now plug Raspberry Pi's Ethernet port to the router to get an IP address. Check Raspberry Pi's IP with IP scanner software, then connect to it using terminal software such as [PuTTY](http://www.putty.org/).
* If you don't have access to router, connect Raspberry Pi with keyboard, mouse, and display to get direct access to it. After the Raspberry Pi has been booted up, press ```Ctrl``` + ```Alt``` + ```t``` simultaneously to open terminal window.
* To change keyboard layout to ```US```, type and run ```sudo nano /etc/default/keyboard``` then change ```XKBLAYOUT="gb"``` to ```XKBLAYOUT="us"```. Reboot your Raspberry Pi with ```sudo reboot``` command. Skip this step if you're using keyboard with UK layout on Raspberry Pi.
* Raspberry Pi 3 comes with 2 network interfaces (WiFi and Ethernet), which both of them configured to get IP from router (DHCP). Since there will be some cases where we don't have access to the router, we can configure the Ethernet with static IP. That way we can still access Raspberry Pi 3 from our computer/laptop through Ethernet even if we don't have access to the router. To do this you can type and run ```sudo nano /home/pi/.bashrc``` then add ```sudo ifconfig eth0 192.168.10.250 netmask 255.255.255.0``` at the end of the file. This effect will take place when we reboot the Raspberry Pi. You can reboot your Raspberry Pi with ```sudo reboot``` command. If you're still using a router to remotely access Raspberry Pi, you might want to turn Raspberry Pi off then connect its Ethernet port to your computer/laptop. You can turn off your Raspberry Pi with ```sudo halt``` command.

<img src="/images/sudo nano bashrc2.PNG" height="400">

* Configure your computer's/laptop's Ethernet port IP address to ```192.168.10.10```.
* Plug Raspberry Pi's Ethernet port then turn it on.
* Access Raspberry Pi using PuTTY with ```192.168.10.250``` as IP address and ```22``` as Port.
* Sometime there are cases when we need to access Raspberry Pi's Desktop remotely. In that case we can make use of VNC (Virtual Network Computing) server inside Raspberry Pi. Follow the steps mentioned [here](https://www.raspberrypi.org/documentation/remote-access/vnc/) to enable the VNC server.

**Notes:**
* To save the changes you made within nano editor press ```Ctrl``` + ```x``` then ```y``` followed up by ```Enter```.
 
## The titles of the projects which will be included in this repository are:
* [01. Blinking and Fading a LED](/01_Blinking_and_Fading_a_LED)
* [02. Click Counter](/02_Click_Counter)
* [03. Proximity Indicator](/03_Proximity_Indicator)
* [04. Motion Detector](/04_Motion_Detector)
* [05. Ambient Light Monitoring](/05_Ambient_Light_Monitoring)
* [06. Potentiometer Controlled Servo](/06_Potentiometer_Controlled_Servo)
* [07. Weather Station](/07_Weather_Station)

Those projects listed above are aimed as introductory to Raspberry Pi 3 programming. All those projects are using WiringPi library for accessing the I/O pins. WiringPi installation can be done following the steps mentioned on [this link](http://wiringpi.com/download-and-install/). Since those projects will use Python, we need to install Python wraper for WiringPi (since it was written in C). Installation guide for WiringPi Python wrapper (a.k.a WiringPi-Python) can be found on [this link](https://goo.gl/Lnh8Xn). Image below can be used as reference for accessing I/O Expansion Shield pins with WiringPi library on Raspberry Pi 3.

<img src="/images/pin table.png" height="400">

# [BAHASA INDONESIA] Raspberry Pi 3 Starter Kit
Silahkan kunjungi link berikut untuk mengunduh sistem operasi untuk raspberry pi dengan versi terbaru : https://www.raspberrypi.org/downloads/raspbian/. Repository ini dibuat sebagai pelengkap dari Raspberry Pi 3 Starter Kit. Raspberry Pi 3 Starter Kit merupakan produk yang sesuai untuk digunakan sebagai titik awal eksplorasi ide-ide yang dapat direalisasikan dengan mini PC berharga terjangkau ini.
Informasi untuk produk tersebut dapat ditemukan pada link-link di bawah:
* [Raspberry Pi 3 Starter Kit](http://digiwarestore.com/en/) - Halaman produk Raspberry Pi Starter Kit
* [Raspberry Pi](https://www.raspberrypi.org/)- Raspberry Pi sebagai development board utama

## Konfigurasi Awal
* Tambahkan file ssh tanpa extension dan simpan dalam micro SD card yang digunakan Raspberry pi 3
* Konfigurasi file config.txt
    * Buka file config.txt yang berada pada micro SD menggunakan software editor notepad++ atau sejenis
    * Temukan konfigurasi "#hdmi_force_hotplug=1" ubah menjadi "hdmi_force_hotplug=1" dengan menghilangkan tanda "#"
    * Temukan konfigurasi "#hdmi_drive=2" ubah menjadi "hdmi_drive=2" dengan menghilangkan tanda "#"
* Simpan file tersebut kemudian pasang kembali micro SD card ke Raspberry pi 3, apabila tidak terjadi kesalahan maka Raspberry pi 3 akan booting dengan tampilan grafis
* Setelah Raspberry pi 3 menyala, edit konfigurasi IP address ethernet raspberry pi 3 menggunakan jendela editor dengan menekan "Ctrl" + "Alt" +"T" pada keyboard
* Kemudian tuliskan perintah "sudo nano ~/.bashrc" pada jendela editor 

<img src="/images/sudo nano bashrc.PNG" height="400">

* Setelah muncul jendela editor tambahkan perintah "sudo ifconfig eth0 192.18.10.250 netmask 255.255.255.0" berikut di akhir baris dari file konfigurasi tersebut 

<img src="/images/sudo nano bashrc2.PNG" height="400">

* Kemudian simpan file tersebut dengan menekan "Ctrl" + "x"
* Kemudian tekan "y" lalu enter.
* Setelah konfigurasi tersimpan berikutnya cek ip dengan perintah "ifconfig eth0"

<img src="/images/ifconfig eth0.PNG" height="400">

## Judul-judul proyek yang akan disertakan pada repository ini adalah:
* [01. Blinking and Fading a LED](/01_Blinking_and_Fading_a_LED)
* [02. Click Counter](/02_Click_Counter)
* [03. Proximity Indicator](/03_Proximity_Indicator)
* [04. Motion Detector](/04_Motion_Detector)
* [05. Ambient Light Monitoring](/05_Ambient_Light_Monitoring)
* [06. Potentiometer Controlled Servo](/06_Potentiometer_Controlled_Servo)
* [07. Weather Station](/07_Weather_Station)

Proyek-proyek yang terdapat pada poin-poin di atas ditujukan sebagai pengantar untuk pemrograman Raspberry Pi 3. Berikut adalah tabel pin yang membantu anda untuk mengakses pin pada shield menggunakan library WiringPi untuk Raspberry Pi 3 I/O Expansion Shield.

<img src="/images/pin table.png" height="400">

Untuk panduan installasi library WiringPi dapat mengkikuti langkah berikut : http://wiringpi.com/download-and-install/. Kemudian terdapat library kedua yang harus terinstall juga yaitu WiringPi for python, untuk panduan installasi dapat mengikuti langkah berikut : https://goo.gl/Lnh8Xn


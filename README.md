# [ENGLISH] Raspberry Pi 3 Starter Kit
Please Visit this link if want to download the latest version of Raspberry pi operating system : https://www.raspberrypi.org/downloads/raspbian/. This repository has been created as the companion for Raspberry Pi 3 Starter Kit. Raspberry Pi 3 Starter Kit itself is a suitable start point for both hobbyist and academist alike to start exploring the possibilities offered by  this inexpensive mini PC platform.
For more information about the product please visit links below:
* [Raspberry Pi 3 Starter Kit](http://digiwarestore.com/en/) - Raspberry Pi Starter Kit's product page
* [Raspberry Pi](https://www.raspberrypi.org/) - Raspberry Pi as the main development board

## The titles of the projects which will be included in this repository are:
* [01. Blinking and Fading a LED](/01_Blinking_and_Fading_a_LED)
* [02. Click Counter](/02_Click_Counter)
* [03. Proximity Indicator](/03_Proximity_Indicator)
* [04. Motion Detector](/04_Motion_Detector)
* [05. Ambient Light Monitoring](/05_Ambient_Light_Monitoring)
* [06. Potentiometer Controlled Servo](/06_Potentiometer_Controlled_Servo)
* [07. Weather Station](/07_Weather_Station)

Those projects listed above are aimed as introductory to Raspberry Pi 3 programming. Next one is pin table for help you to access a pin  on shield  using WiringPi library with Raspberry Pi 3  I/O Expansion Shield.

<img src="/images/pin table.png" height="400">

For WiringPi library installation please follow this link : http://wiringpi.com/download-and-install/. Then there is second library must be installed is Wiringpi for python, for installation guide please follow this link : https://goo.gl/Lnh8Xn

# [BAHASA INDONESIA] Raspberry Pi 3 Starter Kit
Silahkan kunjungi link berikut untuk mengunduh sistem operasi untuk raspberry pi dengan versi terbaru : https://www.raspberrypi.org/downloads/raspbian/. Repository ini dibuat sebagai pelengkap dari Raspberry Pi 3 Starter Kit. Raspberry Pi 3 Starter Kit merupakan produk yang sesuai untuk digunakan sebagai titik awal eksplorasi ide-ide yang dapat direalisasikan dengan mini PC berharga terjangkau ini.
Informasi untuk produk tersebut dapat ditemukan pada link-link di bawah:
* [Raspberry Pi 3 Starter Kit](http://digiwarestore.com/en/) - Halaman produk Raspberry Pi Starter Kit
* [Raspberry Pi](https://www.raspberrypi.org/)- Raspberry Pi sebagai development board utama

# Konfigurasi awal Raspberry Pi 3
* Tambahkan file ssh tanpa extension dan simpan dalam micro sd card yang digunakan Raspberry pi 3
* Konfigurasi file config.txt
  * Buka file config.txt yang berada pada micro SD menggunakan software editor notepad++ atau sejenis
  * Temukan konfigurasi "#hdmi_force_hotplug=1" ubah menjadi "hdmi_force_hotplug=1" dengan menghilangkan tanda "#"
  * Temukan konfigurasi "#hdmi_drive=2" ubah menjadi "hdmi_drive=2" dengan menghilangkan tanda "#"
* Simpan file tersebut kemudian pasang kembali micro sd card ke Raspberry pi 3, apabila tidak terjadi kesalahan maka Raspberry pi 3 akan   booting dengan tampilan grafis
* Setelah Raspberry pi 3 menyala, edit konfigurasi ip address  ethernet raspberry pi 3 menggunakan jendela editor dengan menekan "Ctrl"   + "Alt" +"T" pada keyboard
* Kemudian tuliskan perintah "sudo nano ~/.bashrc" pada jendela editor 

<img src="/images/sudo nano bashrc.PNG" height="400">

* Setelah muncul jendela editor tambahkan perintah "sudo ifconfig eth0 192.18.10.250 netmask 255.255.255.0" berikut di akhir baris dari   file konfigurasi tersebut 

<img src="/images/sudo nano bashrc2.PNG" height="400">

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


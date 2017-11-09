# [ENGLISH] Raspberry Pi 3 Starter Kit
This repository has been created as the companion for Raspberry Pi 3 Starter Kit. Raspberry Pi 3 Starter Kit itself is a suitable start point for both hobbyist and academist alike to start exploring the possibilities offered by this inexpensive mini PC platform. For more information about the product please visit links below:
* [Raspberry Pi 3 Starter Kit](http://digiwarestore.com/en/) - Raspberry Pi 3 Starter Kit's product page.
* [Raspberry Pi](https://www.raspberrypi.org/) - Raspberry Pi's official website.

## Initial Configuration
* The steps below was tested on ```RASPBIAN STRETCH WITH DESKTOP``` and computer/laptop running Windows OS.
* Get the latest Raspbian [here](https://www.raspberrypi.org/downloads/raspbian/) then follow the steps mentioned [here](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md) to install Raspbian into the SD card (recommended size is 8 GB or more).
* Accessing Raspberry Pi remotely through SSH is disabled by default. To enable it insert the SD card to the computer/laptop. Make a file named ```ssh``` and place it into the boot partition of the SD card without any extension. After adding the ```ssh``` file, insert the SD card into Raspberry Pi then boot it up. It will take some time for first time boot.
* If you have access to router, you can now plug Raspberry Pi's Ethernet port to the router to get an IP address. Check Raspberry Pi's IP with IP scanner software, then connect to it using terminal software such as [PuTTY](http://www.putty.org/).
* If you don't have access to router, connect Raspberry Pi with keyboard, mouse, and display to get direct access to it. After the Raspberry Pi has been booted up, press ```Ctrl``` + ```Alt``` + ```t``` simultaneously to open terminal window.
* To change keyboard layout to ```US```, type and run ```sudo nano /etc/default/keyboard``` then change ```XKBLAYOUT="gb"``` to ```XKBLAYOUT="us"```. To save the changes you made, press ```Ctrl``` + ```x``` then ```y``` followed up by ```Enter```. Reboot your Raspberry Pi with ```sudo reboot``` command. Skip this step if you're using keyboard with UK layout on Raspberry Pi.
* Raspberry Pi 3 comes with 2 network interfaces (WiFi and Ethernet), which both of them configured to get IP from router (DHCP). Since there will be some cases where we don't have access to the router, we can configure the Ethernet with static IP. That way we can still access Raspberry Pi 3 from our computer/laptop through Ethernet even if we don't have access to the router. To do this you can type and run ```sudo nano /home/pi/.bashrc``` then add ```sudo ifconfig eth0 192.168.10.250 netmask 255.255.255.0``` at the end of the file. This effect will take place when we reboot the Raspberry Pi. You can reboot your Raspberry Pi with ```sudo reboot``` command. If you're still using a router to remotely access Raspberry Pi, you might want to turn Raspberry Pi off then reconnect its Ethernet port to your laptop/computer. You can turn off your Raspberry Pi with ```sudo halt``` command.

<img src="/images/sudo nano bashrc2.PNG" height="400">

* Configure your computer's/laptop's Ethernet port IP address to be in the same subnet mask range as the Raspberry Pi, for example ```192.168.10.10```.
* Plug Raspberry Pi's Ethernet port to your computer's/laptop's then turn it on.
* Access Raspberry Pi using PuTTY with ```192.168.10.250``` as IP address and ```22``` as Port.
* Sometime there are cases when we need to access Raspberry Pi's Desktop remotely. In that case we can make use of VNC (Virtual Network Computing) server inside Raspberry Pi. Follow the steps mentioned [here](https://www.raspberrypi.org/documentation/remote-access/vnc/) to enable the VNC server and connecting to it. You can set your VNC viewer resolution following the steps mentioned [here](https://support.realvnc.com/knowledgebase/article/View/523/2/troubleshooting-vnc-server-on-the-raspberry-pi).
 
## The titles of the projects which will be included in this repository are:
* [01. Blinking and Fading a LED](/01_Blinking_and_Fading_a_LED)
* [02. Click Counter](/02_Click_Counter)
* [03. Proximity Indicator](/03_Proximity_Indicator)
* [04. Motion Detector](/04_Motion_Detector)
* [05. Ambient Light Monitoring](/05_Ambient_Light_Monitoring)
* [06. Potentiometer Controlled Servo](/06_Potentiometer_Controlled_Servo)
* [07. Weather Station](/07_Weather_Station)

Those projects listed above are aimed as introductory to Raspberry Pi 3 programming. We will use Python 3 as the programming language and [WiringPi-Python](https://github.com/WiringPi/WiringPi-Python) as the Python package to interface with Raspberry Pi's I/O pins. WiringPi-Python itself is a Python wrapper for [WiringPi](http://wiringpi.com/) library which is written in C. Installation for WiringPi-Python can be done by running the commands below on terminal:
```
sudo apt-get update
sudo apt-get install python-dev python-pip
sudo pip3 install wiringpi2
```
Image below can be used as reference for accessing I/O Expansion Shield pins with WiringPi library on Raspberry Pi 3.

<img src="/images/pin table.png" height="400">

# [BAHASA INDONESIA] Raspberry Pi 3 Starter Kit
Repository ini dibuat sebagai pelengkap dari Raspberry Pi 3 Starter Kit. Raspberry Pi 3 Starter Kit sesuai untuk digunakan sebagai titik awal bagi para penghobi ataupun akademisi untuk mulai mengeksplorasi hal-hal yang dapat diwujudkan dengan Raspberry Pi 3. Informasi untuk Raspberry Pi 3 Starter Kit dapat ditemukan pada link-link di bawah:
* [Raspberry Pi 3 Starter Kit](http://digiwarestore.com/en/) - Halaman produk Raspberry Pi 3 Starter Kit
* [Raspberry Pi](https://www.raspberrypi.org/) - Website resmi Raspberry Pi

## Konfigurasi Awal
* Langkah-langkah di bawah telah diuji menggunakan ```RASPBIAN STRETCH WITH DESKTOP``` dan komputer/laptop dengan sistem operasi Windows.
* Unduh sistem operasi Raspbian pada [link](https://www.raspberrypi.org/downloads/raspbian/) ini, kemudian ikuti langkah-langkah yang terdapat pada [link](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md) berikut untuk melakukan instalasi Raspbian pada SD card (kapasitas yang disarankan adalah 8 GB atau lebih).
* Secara default pengaksesan Raspberry Pi secara remote tidak diijinkan. Untuk mengaktifkan akses remote pada Raspberry Pi, masukkan SD card ke komputer/laptop. Buat sebuah file dengan nama ```ssh``` tanpa ekstensi apapun dan letakkan di partisi boot SD card. Setelah menambahkan file ```ssh```, masukkan SD card ke Raspberry Pi dan nyalakan.
* Apabila Anda memiliki akses router, hubungkan port Ethernet Raspberry Pi ke router agar Raspberry Pi mendapatkan alamat IP. Periksa alamat IP Raspberry Pi dengan software IP scanner, lalu akses Raspberry Pi menggunakan software terminal seperti [PuTTY](http://www.putty.org/).
* Apabila Anda tidak memiliki akses router, hubungkan Raspberry Pi dengan keyboard, mouse, and layar monitor untuk melakukan akses secara langsung. Setelah Anda memasuki lingkungan desktop Raspberry Pi,  tekan ```Ctrl``` + ```Alt``` + ```t``` untuk membuka terminal.
* Untuk mengubah layout keyboard ke ```US```, ketikkan dan jalankan perintah ```sudo nano /etc/default/keyboard``` kemudian ganti baris ```XKBLAYOUT="gb"``` menjadi ```XKBLAYOUT="us"```. Untuk menyimpan perubahan yang telah dilakukan, tekan ```Ctrl``` + ```x``` kemudian ```y``` diikuti dengan ```Enter```. Reboot Raspberry Pi dengan perintah ```sudo reboot```. Lewati langkah ini apabila keyboard yang digunakan memiliki layout UK.
* Raspberry Pi 3 memiliki dua antarmuka jaringan (WiFi dan Ethernet), dimana keduanya memiliki konfigurasi DHCP secara default. Karena akan ada kasus dimana kita tidak memiliki akses router, kita dapat mengkonfigurasi port Ethernet dengan IP statis. Dengan demikian kita masih dapat mengakses Raspberry Pi 3 dengan komputer/laptop kita melalui Ethernet meskipun kita tidak memiliki akses router. Konfigurasi tersebut dapat dilakukan dengan perintah ```sudo nano /home/pi/.bashrc``` yang kemudian diikuti dengan menambahkan ```sudo ifconfig eth0 192.168.10.250 netmask 255.255.255.0``` pada akhir file. Perintah tersebut akan dieksekusi pada saat Raspberry Pi dihidupkan, maka dari itu kita harus melakukan reboot pada Raspberry Pi. Reboot Raspberry Pi dapat dilakukan dengan perintah ```sudo reboot```. Apabila Anda masih mengakses Raspberry Pi melalui router, matikan Raspberry Pi terlebih dahulu untuk memindahkan koneksi Ethernet Raspberry Pi dari router ke komputer/laptop Anda. Anda dapat mematikan Raspberry Pi dengan perintah ```sudo halt```.

<img src="/images/sudo nano bashrc.PNG" height="400">

* Konfigurasikan antarmuka Ethernet komputer/laptop Anda agar memiliki alamat IP yang berada dalam rentang subnet mask Raspberry Pi, sebagai contoh ```192.168.10.10```.
* Hubungkan port Ethernet Raspberry Pi ke komputer/laptop Anda kemudian nyalakan.
* Akses Raspberry Pi melalui PuTTY dengan alamat IP ```192.168.10.250``` dan port ```22```.
* Akan ada saat dimana kita perlu untuk mengakses lingkungan desktop Raspberry Pi secara remote. Untuk hal tersebut kita dapat memanfaatkan server VNC (Virtual Network Computing) yang terdapat di dalam Raspberry Pi. Ikuti langkah-langkah yang disebutkan pada [link](https://www.raspberrypi.org/documentation/remote-access/vnc/) berikut untuk mengaktifkan server VNC dan mengaksesnya. Anda dapat mengatur resolusi dari VNC viewer dengan mengikuti langkah-langkah yang terdapat pada [link](https://support.realvnc.com/knowledgebase/article/View/523/2/troubleshooting-vnc-server-on-the-raspberry-pi) berikut.

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


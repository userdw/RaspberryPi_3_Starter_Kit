# [ENGLISH] Project 5: Ambient Light Monitoring
Through this project you will be introduced to the usage of Light Dependent Resistor (LDR) to estimate the ambient light surrounding the system. This kind of system will be found in outdoor lighting or even in our smartphone to control screen brightness. The system in this project will detect the level of ambient light. When the ambient light gets brighter, the LED brightness will increase. On the contrary, when the ambient light gets dimmer, the LED brightness will decrease.

<img src="/images/ambient light monitoring.png" height="400">

### In this project you will need:
* Raspberry Pi 3 (1),
* I/O Expansion Shield (1),
* LED Module (1),
* LDR Sensor (1).

### Assemble the modules following these steps:
1. Plug the I/O Expansion Shield to the top of Raspberry Pi 3,
2. Plug the LED Module to the header on the I/O Expansion Shield labelled **9**,
3. Plug the LDR Sensor to the header on the I/O Expansion Shield labelled **A0**,
4. Run the [Ambient_Light_Monitoring](/05_Ambient_Light_Monitoring/05_Ambient_Light_Monitoring.py) code into Raspberry Pi 3 using python.

Once you turn on the Raspberry Pi 3, it will enter calibration mode for about 3 seconds. Cover the LDR Sensor with your finger to determine the lowest brightness, and uncover the LDR Sensor to determine the highest brightness. Be careful of shadows. If there are no mistakes, LED Module will gets brighter when the ambient light gets dimmer. On the contrary, LED Module will gets dimmer when the ambient light gets brighter.

# [BAHASA INDONESIA] Proyek 5: Ambient Light Monitoring
Proyek ini digunakan untuk memberikan gambaran mengenai penggunaan sensor Light Dependent Resistor (LDR) untuk mengukur intensitas cahaya lingkungan sekitar. Aplikasi seperti ini dapat ditemukan pada sistem lampu taman hingga pengatur tingkat kecerahan layar pada smartphone kita. Sistem pada proyek ini akan mendeteksi intensitas cahaya sekitar menggunakan LDR Sensor. Apabila intensitas cahaya yang diterima semakin besar, maka tingkat kecerahan LED akan naik. Sebaliknya, apabila intensitas cahaya yang diterima semakin kecil, maka tingkat kecerahan LED akan menurun.

<img src="/images/ambient light monitoring.png" height="400">

### Modul-modul yang dibutuhkan pada proyek ini:
* Raspberry Pi 3 (1),
* I/O Expansion Shield (1),
* LED Module (1),
* LDR Sensor (1).

### Hubungkan modul-modul di atas mengikuti langkah-langkah di bawah ini:
1. Pasang I/O Expansion Shield di atas Raspberry Pi 3,
2. Hubungkan LED Module ke header I/O Expansion Shield yang berlabel **9**,
3. Hubungkan LDR Sensor ke header I/O Expansion Shield yang berlabel **A0**,
4. Jalankan kode program [Ambient_Light_Monitoring](/05_Ambient_Light_Monitoring/05_Ambient_Light_Monitoring.py) pada Raspberry Pi 3 menggunakan python.

Pada saat Raspberry Pi 3 dinyalakan, Raspberry Pi 3 akan memasuki proses kalibrasi selama kurang lebih 3 detik. Tutupi LDR Sensor dengan jari untuk mendapatkan nilai kecerahan terendah, dan hilangkan halangan pada LDR Sensor untuk mendapatkan nilai kecerahan tertinggi. Bayangan akan mempengaruhi proses kalibrasi. Apabila tidak terdapat kesalahan, nyala LED Module akan semakin terang saat cahaya sekitar semakin gelap. Sebaliknya, nyala LED Module akan semakin redup saat cahaya sekitar semakin terang.

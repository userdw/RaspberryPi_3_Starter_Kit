# [ENGLISH] Project 3: Proximity Indicator
Measuring distance can be done through a lot of methods. One of the most common method to be used is using the reflection of light. In this project you will learn how to use phototransistor to detect an object and get the rough estimation of object's distance. The system in this project will detect the presence of an object. If the object is getting closer, LED will blink faster and buzzer will beep faster. On the contrary, if the object is getting further, LED will blink slower and buzzer will beep slower.

<img src="/images/proximity indicator.png" height="400">

### In this project you will need:
* Raspberry Pi 3 (1),
* I/O Expansion Shield (1),
* LED Module (1),
* IR Sensor (1).

### Assemble the modules following these steps:
1. Plug the I/O Expansion Shield to the top of Raspberry Pi 3,
2. Plug the LED Module to the header on the I/O Expansion Shield labelled **9**,
3. Plug the Buzzer Module to the header on the I/O Expansion Shield labelled **2**,
4. Plug the IR Sensor to the header on the I/O Expansion Shield labelled **A0**,
5. Run the [Proximity_Indicator](/03_Proximity_Indicator/Proximity_Indicator) code into Raspberry Pi 3 using Python.

Once you turn on the Raspberry Pi 3, it will enter calibration mode for about 3 seconds. Cover the IR Sensor with the desired object which will be tracked to determine the highest brightness, and uncover the IR Sensor to determine the lowest brightness.If there are no mistakes, LED Module should blink faster as the object gets near, and Buzzer Module should beep faster as well. On the contrary, LED Module should blink slower as the objects gets further, and Buzzer Module should beep slower as well.

# [BAHASA INDONESIA] Proyek 3: Proximity Indicator
Pengukuran jarak dapat dilakukan dengan banyak cara, dimana salah satu metode yang digunakan adalah memanfaatkan sifat pantulan cahaya. Proyek ini bertujuan untuk mendemonstrasikan penggunaan sensor cahaya, yaitu phototransistor dengan Arduino 101. Sistem pada proyek ini akan mendeteksi keberadaan dari suatu obyek. Apabila obyek semakin mendekat maka LED akan berkedip semakin cepat dan buzzer akan berbunyi semakin cepat pula. Sebaliknya, apabila obyek semakin menjauh, maka kedipan LED akan semakin lambat dan buzzer akan berbunyi semakin lambat pula.

<img src="/images/proximity indicator.png" height="400">

### Modul-modul yang dibutuhkan pada proyek ini:
* Raspberry Pi 3 (1),
* I/O Expansion Shield (1),
* LED Module (1),
* IR Sensor (1).

### Hubungkan modul-modul di atas mengikuti langkah-langkah di bawah ini:
1. Pasang I/O Expansion Shield di atas Raspberry Pi 3,
2. Hubungkan LED Module ke header I/O Expansion Shield yang berlabel **9**,
3. Hubungkan Buzzer Module ke header I/O Expansion Shield yang berlabel **2**,
4. Hubungkan IR Sensor ke header I/O Expansion Shield yang berlabel **A0**,
5. Jalankan kode program [Proximity_Indicator](/03_Proximity_Indicator/Proximity_Indicator) ke Raspberry Pi 3 menggunakan Python.

Pada saat Raspberry Pi 3 dinyalakan, Raspberry Pi 3 akan memasuki proses kalibrasi selama kurang lebih 3 detik. Tutupi IR Sensor dengan obyek yang hendak dideteksi untuk mendapatkan nilai kecerahan tertinggi, dan hilangkan halangan dari IR Sensor untuk mendapatkan nilai kecerahan terendah. Apabila tidak terdapat kesalahan, maka LED Module akan berkedip semakin cepat saat obyek yang dideteksi semakin mendekat, dan Buzzer Module akan berbunyi semakin cepat pula. Sebaliknya, LED Module akan berkedip semakin lambat saat obyek yang dideteksi semakin menjauh, dan Buzzer Module akan berbunyi semakin lambat pula.

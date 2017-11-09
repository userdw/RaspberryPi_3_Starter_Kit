# [ENGLISH] Project 6: Potentiometer Controlled Servo
If we need to control an output which have more states than on/off, we will have some difficulties if we use switch as an input to control it. That's because the switch itself only has two states. For example, something that have more states than on/off is the speed of a motor, the brightness of a LED, the speed of running text, etc. In this project, you will be introduced to potentiometer and its usage as an input to control servo movement.

<img src="/images/potentiometer controlled servo.png" height="400">

### In this project you will need:
* Raspberry Pi 3 (1),
* I/O Expansion Shield (1),
* Rotation Sensor (1),
* Micro Servo (1).

### Assemble the modules following these steps:
1. Plug the I/O Expansion Shield to the top of Raspberry Pi 3,
2. Plug the Rotation Sensor to the header on the I/O Expansion Shield labelled **A0**,
3. Plug the Micro Servo to the header on the I/O Expansion Shield labelled **9**,
4. Run the [Potentiometer_Controlled_Servo](/06_Potentiometer_Controlled_Servo/Potentiometer_Controlled_Servo) code in Raspberry Pi 3 using Python.

If there are no mistakes, Micro Servo movement will be determined by the rotation of Rotation Sensor. If you don't get the full swing from the servo, it might be you didn't change the position of PWR_SEL jumper to 3V3.

# [BAHASA INDONESIA] Proyek 6: Potentiometer Controlled Servo
Apabila kita hendak mengendalikan suatu output yang memiliki beberapa keadaan selain on/off, maka kita akan mengalami kesulitan apabila menggunakan switch sebagai input, karena switch sendiri hanya memiliki dua kondisi saja. Beberapa contoh sederhana adalah pengaturan kecepatan suatu motor, pengaturan intensitas cahaya suatu lampu, pengaturan kecepatan gerak dari sebuah running text, dll. Pada proyek ini akan dikenalkan penggunaan potensiometer sebagai perangkat input, dimana dengan potensiometer tersebut kita akan mengendalikan sudut dari sebuah motor servo.

<img src="/images/potentiometer controlled servo.png" height="400">

### Modul-modul yang dibutuhkan pada proyek ini:
* Raspberry Pi 3 (1),
* I/O Expansion Shield (1),
* Rotation Sensor (1),
* Micro Servo (1).

### Hubungkan modul-modul di atas mengikuti langkah-langkah di bawah ini:
1. Pasang I/O Expansion Shield di atas Raspberry Pi 3,
2. Hubungkan Rotation Sensor ke header I/O Expansion Shield yang berlabel **A0**,
3. Hubungkan Micro Servo ke header I/O Expansion Shield yang berlabel **9**,
4. Jalankan kode program [Potentiometer_Controlled_Servo](/06_Potentiometer_Controlled_Servo/Potentiometer_Controlled_Servo) pada Raspberry Pi 3 menggunakan Python.

Apabila tidak terdapat kesalahan, gerakan Micro Servo akan ditentukan dari putaran yang diberikan ke Rotation Sensor.

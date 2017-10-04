# [ENGLISH] Web Parsing
Since you visited this page, you must know that Raspberry Pi 3 itself is a computer with small form factor that fits perfectly in your pocket. Since it is a computer, then you can expect all things that you can normally do with computer can be done in Raspberry Pi 3, including browsing the Internet. Let's try to see http://www.bmkg.go.id/. It's a site that contains information about weather prediction in Indonesia. When you view its source you will find lots of text (represented by picture below), not only the predictions but all kind of information regarding display formatting so that our web browser software can display the web page pleasantly to our eyes.

<img src="/images/bmkgSource.jpg" height="400">

First, not all of us have time to bother ourself to check weather prediction. But that doesn't mean the information is not useful, we usually just don't care. But when it comes to it, it could save your day by reminding you to get your umbrella ready. Second, since we are maker, the traditional things like browsing internet through web browser software doesn't have any appeal on our eyes. We just want something different. What if, let's say, we want to display the weather prediction information on character LCD? We will try answer that question step by step.

<img src="/images/webParsing.jpg" height="400">

### In this project you will need:
* Raspberry Pi 3 (1),
* Character LCD 16x2 (1) <sup>*) not included in Raspberry Pi 3 Starter Kit</sup>,
* 

If there are no mistakes, system will start to measure the ambient temperature and display it to te screen.

# [BAHASA INDONESIA] Proyek 7: Weather Station
Proyek ini ditujukan untuk memberikan contoh sederhana mengenai penggunaan mikrokontroler sebagai sebuah stasiun cuaca. Adapun pada proyek ini hal yang akan dipantau adalah suhu sekitar dari sebuah ruangan. Sistem pada proyek ini akan memanfaatkan MCP9700 Temperature Sensor untuk pendeteksian suhu, dan menampilkannya pada layar.

<img src="/images/weather station.png" height="443">

### Modul-modul yang dibutuhkan pada proyek ini:
* Raspberry Pi 3 (1),
* I/O Expansion Shield (1),
* MCP9700 Temperature Sensor (1),

### Hubungkan modul-modul di atas mengikuti langkah-langkah di bawah ini:
1. Pasang I/O Expansion Shield di atas Raspberry Pi 3,
2. Hubungkan MCP9700 Temperature Sensor ke header I/O Expansion Shield yang berlabel **A0**,
5. Jalankan kode program [Weather_Station](/07_Weather_Station/07_Weather_Station.py) pada Raspberry Pi 3 menggunakan python.

Apabila tidak terdapat kesalahan, sistem akan mulai melakukan pengukuran suhu dan menampilkannya pada layar.

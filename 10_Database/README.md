# [BAHASA INDONESIA] Proyek 10: Database
Database merupakan kumpulan data yang saling berhubungan antara kumpulan data satu dengan lainnya yang disimpan secara sistematis dalam media penyimpanan elektronik guna membentuk data baru. Database merupakan komponen penting dalam sistem informasi yang berfungsi sebagai gudang penyimpanan data yang akan diolah lebih lanjut. Selain itu, database juga mampu mengorganisasi data, menghindari duplikasi data, menghindari hubungan antar data yang tidak jelas, dan dapat meng-update data yang tergolong rumit. Seorang perancang database akan mengumpulkan data untuk memodelkan suatu kegiatan yang mempunyai informasi dengan jumlah data yang sangat banyak contohnya seperti data penjualan, data kepegawaian, data sekolah, data perpustakaan, dan lain-lain. Jika dijabarkan, sebuah sistem data penjualan akan berisi tentang seluruh informasi mengenai data penjualan seperti nama produk, harga produk, jumlah stok, data customer, diskon, retur, dan lain-lain. Begitu juga dalam sistem data kepegawaian akan berisi terkait dengan data karyawan, gaji, pajak, lama bekerja, jumlah
cuti, dan lain sebagainya.Gambar dibawah ini menunjukkan pusat penyimpanan data media social Facebook yang diletakkan dalam ruangan yang cukup besar.

<p align="center">
<img src="/images/Database center.jpeg" height="300">
</p>

Proses memasukkan dan mengambil data dari dan ke media penyimpanan data memerlukan perangkat lunak yang disebut yang disebut dengan Database Management System (DBMS). Perangkat lunak ini digunakan untuk memelihara, mengontrol, mengelola, mengakses, dan menganalisis data dalam jumlah besar serta dapat menjalankan perintah-perintah yang diminta oleh pengguna (database user) atau aplikasi lain. Sebelum adanya DBMS, data umumnya disimpan dalam bentuk file teks yang sudah disediakan oleh sistem operasi. Namun seiring dengan bertambahnya kecepatan dalam pengolahan data, metode penyimpanan dalam bentuk file teks hanya akan berjalan secara optimal apabila ukuran filenya relatif kecil. Beberapa contoh DBMS yang terkenal antara lain MySQL, PostgreSQL, EnterpriseDB, MongoDB, MariaDB, Microsoft SQL Server, Oracle, Sybase, SAP HANA, MemSQL, SQLite, dan IBM DB2. Gambar dibawah ini menunjukkan simbol dari DBMS bernama SQLite.

<p align="center">
<img src="/images/SQLite.png" height="100">
</p>

### Entity Relationship Diagram (ERD)
ERD adalah sebuah diagram yang berfungsi untukmenggambarkan hubungan antar entitas/tabel menggunakan primary key di dalam sebuah database. Sekilas ERD ini terlihat sangat mirip dengan diagram alir (flowchart) yang mempunyai simbol khusus dengan makna yang berbeda-beda. Pada dasarnya terdapat komponen utama yang khusus digunakan untuk menggambarkan hubungan antar data menggunakan ERD, komponen tersebut antara lain:
1. Entitas, adalah suatu objek atau konsep yang berisi tentang suatu informasi seperti informasi orang, benda, tempat, kejadian, maupun konsep. Dalam sebuah sistem database, entitas berbentuk sebuah tabel dua dimensi yang terdiri dari baris dan kolom. Simbol dari entitas
digambarkan dengan bentuk persegi panjang seperti yang ditunjukkan pada gambar dibawah ini.

<p align="center">
<img src="/images/Entitas.jpg" height="65">
</p>

2. Atribut, merupakan deskripsi yang lebih rinci dari sebuah entitas. Simbol dari attribute digambarkan dengan bentuk oval yang ditunjukkan pada gambar dibawah ini. Berdasarkan jenis datanya, attribute dibedakan menjadi beberapa jenis antara lain:
   * Primary key, digunakan untuk mendeskripsikan isi dari suatu entitas secara unik.
   * Atribute simple, attribute yang memiliki nilai tunggal atau tidak dapat dipilah-pilah lagi
   * Atribute multivalue, attribute yang memiliki nilai lebih dari satu dari attribute yang bersangkutan

<p align="center">
<img src="/images/Atribute.png" height="65">
</p>

3. Relasi, merupakan hubungan antara beberapa entitas dalam diagram. Simbol dari relasi digambarkan dengan bentuk diamond.

<p align="center">
<img src="/images/Relasi.png" height="85">
</p>

4. Kardinalitas, menggambarkan banyaknya jumlah maksimum hubungan entitas yang dapat berelasi dengan entitas lainnya. Terdapat 3 jenis relasi antar entitas antara lain:
   * One to one, satu attribute pada entitas A hanya boleh berhubungan dengan satu attribute pada entitas B, begitu pula sebaliknya. Sebagai contoh: satu orang bisa mendaftar sebagai anggota perpustakaan sebanyak satu kali.
   * One to many, setiap attribute pada entitas A dapat berhubungan dengan lebih dari satu attribute pada entitas B, namun tidak sebaliknya. Sebagai contoh: satu orang dapat meminjam beberapa buku, namun satu buku tidak dapat dipinjam oleh beberapa siswa.
   * Many to many, Sebagai contoh: satu buku dapat terdiri dari banyak pengarang demikian juga satu pengarang dapat menulis banyak buku.

### Contoh Database Sederhana
Pada sebuah perpustakaan, setiap harinya pasti terdapat banyak aktivitas seperti membaca, meminjam, mengembalikan buku, dan juga melakukan pendaftaran sebagai anggota baru perpustakaan. Dalam hal ini, untuk mengefektifkan kinerja pegawai perpustakaan maka diperlukanlah sebuah sistem informasi yang berisi tentang data buku, data petugas, data peminjam, transaksi peminjaman, transaksi pengembalian, dan lain sebagainya. Dibawah ini merupakan contoh ERD database perpustakaan sederhana yang menunjukkan hubungan antara perpustakaan, mahasiswa, dan buku.

<p align="center">
<img src="/images/ERDPerpustakaan.jpg" height="400">
</p>


# README

Hal yang perlu di ingat ketika ingin melakukan analisis Deep Learning adalah

- Alat yang digunakan bisa menggunakan jupyter notebook maupun google colab. Namun sebaiknya menggunakan google colab untuk menghindari adanya crash dependency

- Upload data bisa menggunakan local computer, upload data ke google drive maupun menggunakan url. Jika cara menggunakan url gagal atau susah bisa menggunakan cara upload data dulu ke google drive.Oleh karena itu, dalam github ini ditampilkan dua cara agar bisa mengcover jika salah satu cara gagal.

- Sebelum di upload ke google drive, data terlebih dahulu harus dibagi ke dua folder train dan test. Untuk mendapatkan path dari data yang sudah diupload, bisa menggunakan seperti cara mencari data di mac atau ubuntu. Yaitu 
1. %pwd untuk mengetahui lokasi saat ini, 
2. %ls untuk menampilkan list file dan 
3. %cd untuk berpindah direktori

- Cek dan pastikan data telah berhasil di input

- Buatlah 1 list yang berisi data training. Data yang awalnya berbentuk image perlu diubah ke dalam bentuk matriks. Warna image perlu diubah ke dalam bentuk warna grayscale agar tidak memberatkan komputasi.Image yang mempunyai warna akan membuat ukuran matriks akan menjadi besar. Padahal sebenarnya warna tidak akan mempengaruhi analisis secara signifikan. Sehingga jika diubah ke grayscale pun tidak menjadi masalah

- Image juga bisa diubah ke dimensinya ke yang lebih kecil, efeknya gambar tidak terlalu tajam, namun sebisa mungkin masih bisa menggambarkan sebagian besar makna gambar tersebut.

- Pada data training, perlu dilakukan pengacakan urutan agar satu kelas tidak mengumpul.
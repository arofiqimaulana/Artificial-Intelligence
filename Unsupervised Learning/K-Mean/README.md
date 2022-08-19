# K-Mean

## Pengertian
k-Mean termasuk dalam teknik clustering yang berguna untuk membagi data menjadi beberapa cluster. Algoritma ini termasuk dalam unsupervised learning yang berarti tidak butuh variabel dependent (Y). Huruf k disini menunjukkan banyaknya cluster yang dipilih.

Prinsip kerja algoritma ini adalah mengelompokkan objek ke centroid terdekat. Centroid disini didapatkan dari pengambilan secara acak sebanyak k objek dari total n objek. Sehingga tahapan dari algoritma ini adalah

## Flow
Tentukan k buah cluster
1. Pilih sejumlah k buah objek secara ajak yang akan dijadikan sebagai centroid cluster
2. Tentukan k buah centroid (titik tengah)
3. Kelompokkan objek ke centroid cluster terdekat berdasarkan jarak euclidian
4. Hitung kembali semua nilai titik centroid
5. Ulangi langkahb 3 s.d 5 sampai nilai titik centroid tidak berubah lagi

Setiap cluster memiliki tikik pusat yang dikenal sebagai centroid. Pada awal pembentukan cluster, nilai centroid ditentukan secara random. Namun selanjutnya nilai centroid tersebut ditentukan berdasarkan rumus ini


###### Centroid

$$ \text{centroid} = \sum_{i=1}^{n} \frac{x_i}{n} $$ 


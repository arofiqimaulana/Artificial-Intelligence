# K-Medoids

## Pengertian
k-Medoids dikenal juga sebagai *Partitioning Around Medoids* (PAM), adalah varian dari metode k-Means. Metode ini mengatasi permasalahan data ekstrem yang akan sensitif jika menggunakan metode rata-rata (k-Means).

Medoid merupakan objek yang letaknya terpusat di dalam suatu cluster sehingga robust terhadap outlier. Cluster dibangun dengan menghitung kedekatan yang dimiliki antara medoids dengan objek non medoids (Setyawati, 2017).

## Flow
1. Tentukan k (jumlah cluster) yang diinginkan
2. Pilih secara acak medoid awal sebanyak k dari n data
3. Hitung jarak masing-masing obyek ke medoid sementara, kemudian tandai jarak terdekat obyek ke medoid dan hitung totalnya (jarak bisa menggunakan euclidian,manhattan dkk).
4. Lakukan iterasi medoid
5. Hitung total simpangan (S) <br>
Jika a adalah jumlah jarak terdekat antara obyek ke medoid awal, dan b adalah jumlah jarak terdekat antara obyek ke medoid baru, maka total simpangan adalah S = b — a
Jika S < 0, maka tukar obyek dengan data untuk membentuk sekumpulan k baru sebagai medoid
6. Ulangi langkah 3 sampai 5 dan hentikan jika sudah tidak terjadi perubahan anggota medoid


## Reference
- https://machinelearningmastery.com/clustering-algorithms-with-python/
- https://pyclustering.github.io/docs/0.10.1/html/d0/dd3/classpyclustering_1_1cluster_1_1kmedoids_1_1kmedoids.html
- https://scikit-learn-extra.readthedocs.io/en/stable/generated/sklearn_extra.cluster.KMedoids.html
- https://scikit-learn-extra.readthedocs.io/en/stable/install.html
- https://repository.usd.ac.id/40031/2/175314055_full.pdf
- https://medium.com/@tribinty/k-medoids-partitioning-around-medoids-pam-non-hierarchical-clustering-with-r-9d0af590bbc0

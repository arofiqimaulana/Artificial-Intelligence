# Hierarchical Clustering

## Pengertian
Secara umum, hierarchical clustering dibagi menjadi dua jenis yaitu agglomerative dan divisive. Kedua metode ini dibedakan berdasarkan pendekatan dalam melakukan pengelompokkan data hingga membentuk dendrogram, menggunakan bottom-up atau top-down manner.

## Agglomerative vs Divisive
1. Agglomerative Clustering <br>
Dikenal juga sebagai juga sebagai agglomerative nesting (AGNES) dimana cara kerja dalam melakukan pengelompokan data menggunakan bottom-up manner. Prosesnya dimulai dengan menganggap setiap data sebagai satu cluster kecil (leaf) yang hanya memiliki satu anggota saja, lalu pada tahap selanjutnya dua cluster yang memiliki kemiripan akan dikelompokkan menjadi satu cluster yang lebih besar (nodes). Proses ini akan dilakukan terus menerus hingga semua data menjadi satu cluster besar (root).

2. Divisive hierarchical clustering <br>
Dikenal juga sebagai divisive analysis (DIANA) di mana cara kerja dalam melakukan pengelompokan data menggunakan top-down manner. Prosesnya dimulai dengan menganggap satu set data sebagai satu cluster besar (root), lalu dalam setiap iterasinya setiap data yang memiliki karakteristik yang berbeda akan dipecah menjadi dua cluster yang lebih kecil (nodes) dan proses akan terus berjalan hingga setiap data menjadi satu cluster kecil (leaf) yang hanya memiliki satu anggota saja.

## Algoritma
Terdapat beberapa metode dalam hierarchical clustering yaitu

1. Single Linkage (Nearest Neighbor) <br>
Jarak antar dua cluster yang ada, dipilih ** jarak paling **dekat atau aturan tetangga deka (nearest neighbour rule).

2. Complete Linkage (Farthest Neighbor) <br>
Jarak antar cluster ditentukan oleh jarak terjauh antara dua obyek dalam cluster yang berbeda.

3. Average linkage (Between Group) <br> 
Jarak antara dua cluster dianggap sebagai ** jarak rata-rata ** antara semua anggota dalam satu cluster dengan semua anggota cluster lain.

4. Metode Ward <br>
Menurut Johnson & Wichern (2002) metode Ward merupakan suatu metode pembentukan cluster yang didasari oleh hilangnya informasi akibat penggabungan obyek menjadi cluster. Hal ini diukur dengan menggunakan jumlah total dari deviasi kuadrat pada mean cluster untuk setiap pengamatan. Error sum of squares (SSE) digunakan sebagai fungsi obyektif. Metode ini berusaha meminimmkan keragaman dalam cluster.

## Reference
- https://algotech.netlify.app/blog/introduction-to-hierarchical-clustering/
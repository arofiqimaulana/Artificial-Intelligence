# Algoritma k-Nearest Neighbors (k-NN)

## Gambaran Umum
Algoritma k-Nearest Neighbors (k-NN) adalah algoritma pembelajaran mesin yang sederhana, non-parametrik, dan bersifat *lazy learning* yang digunakan untuk tugas klasifikasi dan regresi. Algoritma ini bekerja dengan mencari `k` titik data terdekat (tetangga) dari suatu input berdasarkan metrik jarak (misalnya, jarak Euclidean) dan membuat prediksi berdasarkan kelas mayoritas (untuk klasifikasi) atau rata-rata (untuk regresi) dari tetangga tersebut.

## Cara Kerja k-NN
1. **Persiapkan Data**: Pastikan dataset telah dinormalisasi atau distandarisasi, karena k-NN sensitif terhadap skala fitur.
2. **Pilih Nilai `k`**: Tentukan jumlah tetangga (`k`) yang akan dipertimbangkan. Ini adalah hiperparameter yang dapat disesuaikan.
3. **Hitung Jarak**: Untuk titik data baru, hitung jarak ke semua titik dalam dataset pelatihan menggunakan metrik jarak (biasanya jarak Euclidean).
4. **Identifikasi k Tetangga Terdekat**: Pilih `k` titik data dengan jarak terkecil.
5. **Buat Prediksi**:
   - Untuk **klasifikasi**, tetapkan kelas dengan suara mayoritas di antara `k` tetangga.
   - Untuk **regresi**, hitung rata-rata (atau rata-rata tertimbang) dari nilai `k` tetangga.
6. **Evaluasi**: Gunakan metrik seperti akurasi (untuk klasifikasi) atau mean squared error (untuk regresi) untuk menilai performa.

## Kelebihan
- Mudah dipahami dan diimplementasikan.
- Tidak ada fase pelatihan, karena menyimpan seluruh dataset (*lazy learning*).
- Cocok untuk dataset kecil atau data non-linier.

## Kekurangan
- Komputasi mahal untuk dataset besar, karena menghitung jarak untuk setiap prediksi.
- Sensitif terhadap fitur yang tidak relevan dan skala data.
- Performa sangat bergantung pada pilihan `k` dan metrik jarak.

## Contoh Implementasi
Berikut adalah implementasi sederhana menggunakan Python dengan pustaka scikit-learn:

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Data contoh
X = np.array([[1, 2], [2, 3], [3, 4], [6, 5], [7, 7]])  # Fitur
y = np.array([0, 0, 0, 1, 1])  # Label (klasifikasi biner)

# Pisahkan data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisasi fitur
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Inisialisasi dan latih model k-NN
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Akurasi: {accuracy:.2f}")
```


## Memilih Nilai `k`
- Nilai `k` kecil (misalnya, 1 atau 3) dapat menyebabkan *overfitting*, karena sensitif terhadap noise.
- Nilai `k` besar dapat menghaluskan prediksi, tetapi berisiko *underfitting* dengan mengabaikan pola lokal.
- Gunakan validasi silang (*cross-validation*) untuk menemukan nilai `k` optimal.

## Aplikasi
- Klasifikasi gambar
- Sistem rekomendasi
- Deteksi anomali
- Pengenalan pola

## Catatan
- **Metrik Jarak**: Pilihan umum meliputi jarak Euclidean, Manhattan, dan Minkowski.
- **Optimasi**: Untuk dataset besar, pertimbangkan algoritma tetangga terdekat aproksimasi (misalnya, KD-Tree, Ball Tree) yang didukung oleh scikit-learn.
- **Pra-pemrosesan**: Selalu normalisasi atau standarisasi fitur untuk memastikan perhitungan jarak yang adil.

## Referensi
- Dokumentasi scikit-learn: [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
- "Machine Learning with Python" oleh Sebastian Raschka
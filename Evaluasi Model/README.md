# Teknik Evaluasi Model

Dalam menguji model machine learning, terdapat beberapa metrik yang biasa digunakan untuk menilai kualitas dan kinerja model. Alat ukur yang dipilih tergantung pada jenis tugas yang dihadapi (klasifikasi, regresi, klastering, dsb.). Berikut ini beberapa alat ukur umum yang digunakan:

## 1. Untuk Tugas Klasifikasi

- Akurasi (Accuracy): Proporsi dari semua prediksi yang benar.
- Matriks Confusion: Menunjukkan prediksi benar dan salah antara kelas aktual dan kelas yang diprediksi.
- Precision: Proporsi prediksi positif yang benar-benar positif.
- Recall (atau Sensitivity): Proporsi data positif aktual yang berhasil diprediksi dengan benar.
- F1-Score: Rerata harmonik dari precision dan recall.
- ROC Curve & AUC: Mengukur performa model pada berbagai ambang batas klasifikasi.
- Log Loss: Ukuran yang mengukur ketidakpastian prediksi.

## 2. Untuk Tugas Regresi

- Mean Absolute Error (MAE): Rata-rata dari selisih absolut antara nilai asli dan nilai prediksi.
- Mean Squared Error (MSE): Rata-rata dari kuadrat selisih antara nilai asli dan nilai prediksi.
- Root Mean Squared Error (RMSE): Akar kuadrat dari MSE.
- R-squared: Mengukur seberapa baik variabilitas data dijelaskan oleh model.

## 3. Untuk Tugas Klastering

- Silhouette Score: Mengukur seberapa mirip objek dengan kluster sendiri dibandingkan dengan kluster lain.
- Davies-Bouldin Index: Rasio jarak rata-rata dalam klaster dengan jarak antar klaster.

## 4. Untuk Tugas Ranking

- Normalized Discounted Cumulative Gain (NDCG): Mengukur kualitas urutan yang diprediksi dibandingkan dengan urutan ideal.
- Precision at K: Proporsi item relevan pada K item teratas.

## 5. Untuk Tugas Forecasting

### 5.1 Metrik Evaluasi:

- Mean Absolute Error (MAE): Rata-rata dari selisih absolut antara nilai aktual dan nilai prediksi.
- Mean Squared Error (MSE): Rata-rata dari kuadrat selisih antara nilai aktual dan nilai prediksi.
- Root Mean Squared Error (RMSE): Akar kuadrat dari MSE, memberikan gambaran mengenai besar kesalahan prediksi.
- Mean Absolute Percentage Error (MAPE): Rata-rata dari selisih persentase antara nilai aktual dan prediksi Cocok untuk data yang memiliki skala yang bervariasi.
- Symmetric Mean Absolute Percentage Error (sMAPE): Varian dari MAPE yang lebih simetris dan dapat mengatasi beberapa kekurangan MAPE.

### 5.2 Teknik Validasi:

- Train/Test Split: Memecah data menjadi set pelatihan dan set pengujian. Model dilatih pada set pelatihan dan diuji pada set pengujian.
- Rolling Forecast Origin (atau Time Series Cross-Validation): Sebuah teknik validasi silang khusus untuk data time series di mana titik awal prediksi "digulirkan" ke depan dalam waktu untuk simulasi prediksi "real-time".
- Out-of-sample validation: Menggunakan data yang tidak digunakan selama proses pelatihan untuk validasi model.

### 5.3 Analisis Residu:

- Menilai sifat residu (perbedaan antara prediksi dan nilai aktual) dapat memberikan informasi berharga tentang apakah ada informasi yang belum ditangkap oleh model.
- Plot residu terhadap waktu, cek apakah ada pola atau ketergantungan.
- Cek distribusi residu, idealnya harus mendekati distribusi normal.
- Autokorelasi residu seharusnya minimal, yang menunjukkan tidak ada informasi yang tersisa dalam residu.

### 5.3 Uji Statistik:

- Ljung-Box test: Mengukur apakah kumpulan nilai (biasanya residu) adalah sampel acak independen dari distribusi normal. Jika residu memiliki autokorelasi, model mungkin belum menangkap semua informasi.
- Komparasi dengan Model Naive/Benchmark:Seringkali berguna untuk membandingkan model yang Anda latih dengan model sederhana seperti model naive (misalnya, selalu memprediksi nilai terakhir yang diketahui) untuk mendapatkan perspektif tentang seberapa baik kinerja model Anda.

### 5.4 Lain-lain:

- Cross-Validation: Teknik untuk mengukur kinerja model dengan membagi data menjadi beberapa subset dan melakukan pelatihan serta pengujian berulang kali.
- Learning Curve: Plot yang menunjukkan kinerja model terhadap jumlah data pelatihan untuk mengetahui apakah model memerlukan lebih banyak data atau apakah model menderita dari bias/variance tinggi.
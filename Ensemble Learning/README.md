
# 📘 Ensemble Learning

Ensemble learning bisa dibilang sebagai pembelajaran menggunakan sistem demokrasi. Hal ini karena hasil prediksi menggunakan voting dari beberapa metode. Secara arti, jika kita lihat pengertian ensemble adalah

> a group of items viewed as a whole rather than individually

# 🛠️ Boosting vs Bagging

**Boosting** dan **Bagging** adalah dua teknik ensemble dalam pembelajaran mesin yang digunakan untuk meningkatkan akurasi model dengan menggabungkan beberapa model pembelajaran sederhana (biasanya pohon keputusan). Meskipun keduanya bertujuan untuk meningkatkan performa, cara kerjanya sangat berbeda. Berikut adalah perbedaan utama antara keduanya:

## 🔍 1. Tujuan
- **Boosting**: Meningkatkan akurasi dengan mengurangi bias dan kesalahan model secara bertahap. Setiap model yang baru lebih fokus untuk memperbaiki kesalahan dari model sebelumnya.
- **Bagging**: Mengurangi varians dan meningkatkan kestabilan model dengan membangun banyak model secara paralel dan menggabungkan hasilnya. Ini biasanya digunakan untuk mengurangi overfitting.

## 🔍 2. Cara Kerja
- **Boosting**:
  - Model dibangun secara bertahap (seri).
  - Setiap model baru dibangun untuk memperbaiki kesalahan (residual) dari model sebelumnya.
  - Model yang lebih lemah diperbaiki oleh model berikutnya yang lebih kuat.
  - Contoh algoritma: AdaBoost, Gradient Boosting, XGBoost.

- **Bagging**:
  - Model dibangun secara paralel.
  - Menggunakan subset data acak (bootstrapping) untuk melatih beberapa model secara independen.
  - Hasil akhir diperoleh dengan menggabungkan hasil prediksi dari semua model (misalnya dengan voting atau rata-rata).
  - Contoh algoritma: Random Forest.

## 🔍 3. Proses Pembelajaran
- **Boosting**:
  - Menggunakan data yang sama di setiap iterasi.
  - Model dibangun untuk fokus pada data yang sulit diprediksi oleh model sebelumnya.
  - Model saling bergantung satu sama lain.

- **Bagging**:
  - Setiap model dilatih dengan data yang berbeda (melalui teknik bootstrapping).
  - Model-model tersebut berdiri sendiri, tanpa saling bergantung.
  - Tidak ada perhatian khusus terhadap kesalahan model sebelumnya.

## 🔍 4. Performa dan Pengaruh Terhadap Overfitting
- **Boosting**:
  - Cenderung lebih rentan terhadap overfitting, terutama jika terlalu banyak iterasi dilakukan atau model dasar terlalu kompleks.
  - Meningkatkan akurasi dengan mengurangi bias tetapi bisa meningkatkan varians pada data yang bising.

- **Bagging**:
  - Membantu mengurangi overfitting karena model dibangun secara independen dan kemudian digabungkan.
  - Lebih baik digunakan untuk model yang sangat bervariasi (misalnya pohon keputusan) karena bisa mengurangi varians.

## 🔍 5. Bobot Prediksi
- **Boosting**:
  - Bobot model yang lebih kuat lebih besar. Model-model yang lebih akurat memiliki pengaruh lebih besar terhadap hasil akhir.

- **Bagging**:
  - Setiap model biasanya diberi bobot yang sama, tidak ada model yang lebih dominan daripada yang lain.

## 🔍 6. Kecepatan Pelatihan
- **Boosting**:
  - Lebih lambat karena proses pelatihan bertahap (seri) dan membutuhkan model sebelumnya untuk memperbaiki kesalahan.

- **Bagging**:
  - Lebih cepat dibandingkan Boosting karena model dibangun secara paralel dan tidak tergantung satu sama lain.

## 🔍 7. Contoh Algoritma
- **Boosting**:
  - AdaBoost
  - Gradient Boosting
  - XGBoost
  - LightGBM

- **Bagging**:
  - Random Forest
  - Bagging Classifier

## 🔍 Ringkasan Perbandingan:

| **Aspek**          | **Boosting**                              | **Bagging**                                  |
|--------------------|-------------------------------------------|----------------------------------------------|
| **Tujuan**         | Mengurangi bias model                     | Mengurangi varians dan overfitting           |
| **Proses**         | Bertahap (seri)                           | Paralel (model independen)                   |
| **Pembelajaran**   | Model baru fokus pada kesalahan model sebelumnya | Model dibangun dengan subset data berbeda   |
| **Kestabilan**     | Rentan terhadap overfitting               | Mengurangi overfitting                       |
| **Kecepatan**      | Lebih lambat                              | Lebih cepat                                 |
| **Contoh Algoritma**| AdaBoost, Gradient Boosting, XGBoost      | Random Forest, Bagging Classifier            |

## 📚 Refference
- Suyanto. 2018. Machine Learning Tingkat Dasar dan Lanjut. Informatika. Bandung.
- https://towardsdatascience.com/ensemble-methods-bagging-boosting-and-stacking-c9214a10a205
- https://www.edureka.co/blog/boosting-machine-learning/
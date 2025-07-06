# 📘 Gradient Boosting

adalah metode ensemble yang menggabungkan banyak model pembelajaran sederhana (biasanya Decision Tree) untuk menghasilkan model yang lebih kuat. Gradient Boosting bekerja dengan cara membangun model secara bertahap, dimana setiap model baru memperbaiki kesalahan dari model sebelumnya.

## 🛠️ Cara Kerja

Proses Gradient Boosting dapat dijelaskan dalam beberapa langkah sebagai berikut:

1. **Model Pertama (Basis)**: Pertama, model pohon keputusan pertama dibangun menggunakan data pelatihan.
2. **Perbaikan Model**: Setelah model pertama dilatih, residual (kesalahan) dari model pertama dihitung. Residual ini adalah perbedaan antara nilai yang diprediksi oleh model pertama dan nilai yang sebenarnya.
3. **Model Kedua**: Model kedua dibangun untuk memprediksi residual dari model pertama. Ini berarti model kedua berfokus untuk memperbaiki kesalahan yang dilakukan oleh model pertama.
4. **Iterasi**: Proses ini diulang beberapa kali, dengan setiap model baru berfokus pada residual yang belum terprediksi dengan baik oleh model-model sebelumnya.
5. **Prediksi Akhir**: Prediksi akhir diperoleh dengan menggabungkan hasil dari semua model yang telah dibangun. Hasil prediksi dari setiap model biasanya diberi bobot sesuai dengan performanya.

### Fungsi Kerja:
- **Fokus pada kesalahan**: Setiap model baru belajar untuk memperbaiki kesalahan yang dibuat oleh model sebelumnya.
- **Penurunan Gradien**: Proses ini mengurangi kesalahan iteratif dengan menggunakan algoritma penurunan gradien untuk mengarahkan model menuju minimum kesalahan yang optimal.

## 📋 Kelebihan dan Kekurangan Gradient Boosting

### Kelebihan:
1. **Akurasi Tinggi**: Gradient Boosting memiliki performa yang sangat baik, terutama untuk data yang kompleks dan tidak linier.
2. **Kemampuan Generalisasi**: Ini bekerja dengan sangat baik untuk data yang lebih kecil dan dapat mencegah overfitting lebih baik dibandingkan metode lainnya.
3. **Fleksibilitas**: Bisa digunakan untuk berbagai jenis data dan masalah, baik itu klasifikasi, regresi, maupun ranking.

### Kekurangan:
1. **Waktu Komputasi yang Lama**: Karena model dibangun secara bertahap, proses pelatihan bisa memakan waktu lama, terutama jika jumlah iterasi (model) yang diperlukan sangat banyak.
2. **Tidak Mudah Dipahami**: Model Gradient Boosting cenderung lebih sulit untuk dipahami dan diinterpretasi, karena melibatkan banyak model pohon keputusan.
3. **Overfitting**: Jika tidak diatur dengan benar, seperti penggunaan parameter yang tepat, Gradient Boosting bisa mengalami overfitting pada data pelatihan.

## 📋 Implementasi Gradient Boosting

Gradient Boosting sering digunakan dengan pustaka Python seperti **Scikit-learn**, **XGBoost**, **LightGBM**, dan **CatBoost**. Berikut adalah contoh implementasi dasar menggunakan Scikit-learn:

```python
from sklearn.ensemble import GradientBoostingClassifier

# Data pelatihan (X_train, y_train)
# Model Gradient Boosting
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3)

# Melatih model
model.fit(X_train, y_train)

# Prediksi
predictions = model.predict(X_test)
```

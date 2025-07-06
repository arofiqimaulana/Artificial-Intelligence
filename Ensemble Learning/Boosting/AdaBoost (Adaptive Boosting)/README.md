# 📘 AdaBoost (Adaptive Boosting)

adalah metode pembelajaran mesin ensemble yang menggabungkan beberapa model sederhana (biasanya pohon keputusan) untuk menghasilkan model yang lebih kuat. Berbeda dengan metode boosting lainnya, AdaBoost menekankan pentingnya memperbaiki kesalahan model sebelumnya dengan cara **memberi bobot lebih** pada data yang sulit diprediksi.

## 🛠️ Cara Kerja:
AdaBoost bekerja dengan cara membangun model secara berurutan, di mana setiap model baru berfokus pada kesalahan yang dilakukan oleh model sebelumnya. Setiap model diberi bobot, dan kesalahan model akan mempengaruhi bobot data di iterasi berikutnya.

Proses AdaBoost dapat dijelaskan dalam beberapa langkah:

1. **Model Pertama**: Model pertama (misalnya, pohon keputusan) dilatih pada data pelatihan.
2. **Penentuan Bobot**: Setiap data yang diprediksi salah oleh model pertama akan diberikan bobot lebih tinggi pada iterasi berikutnya. Ini berarti model berikutnya akan lebih fokus pada data yang sulit diprediksi.
3. **Model Kedua dan Seterusnya**: Model kedua dibangun dengan data yang sudah dimodifikasi bobotnya. Setiap model baru mencoba memperbaiki kesalahan dari model sebelumnya.
4. **Prediksi Akhir**: Prediksi akhir dihasilkan dengan menggabungkan hasil dari semua model yang telah dibangun, dengan bobot prediksi dari setiap model.
5. **Bobot Model**: Model dengan kesalahan lebih rendah akan memiliki bobot yang lebih tinggi dalam prediksi akhir.

### Fungsi Kerja:
- **Menangani Kesalahan**: Model yang lebih baik diberikan perhatian lebih, sehingga meningkatkan kemampuan generalisasi.
- **Bobot Data**: Data yang sulit diprediksi diberi bobot lebih, untuk memberi perhatian lebih pada data tersebut.

## 📋 Kelebihan dan Kekurangan AdaBoost

### Kelebihan:
1. **Akurasi Tinggi**: AdaBoost dapat menghasilkan model yang sangat akurat, terutama untuk masalah klasifikasi biner.
2. **Tidak Rentan terhadap Overfitting**: Dengan pengaturan yang tepat, AdaBoost cenderung tidak mudah mengalami overfitting.
3. **Sederhana dan Mudah Dipahami**: Algoritma ini cukup sederhana untuk dipahami dan diterapkan, terutama dengan menggunakan model pohon keputusan yang sederhana.

### Kekurangan:
1. **Sensitif terhadap Noise**: Jika terdapat banyak data yang noise atau outliers, AdaBoost bisa terpengaruh karena memberikan bobot lebih pada data yang salah diprediksi.
2. **Model Lemah**: Jika model dasar (misalnya pohon keputusan kecil) terlalu lemah, AdaBoost tidak akan memberikan hasil yang optimal.
3. **Waktu Pelatihan Lama**: Karena setiap model dilatih secara bertahap, proses pelatihan bisa memakan waktu lebih lama dibandingkan dengan metode lain.

## 📋 Implementasi AdaBoost

AdaBoost dapat diimplementasikan dengan pustaka Python seperti **Scikit-learn**. Berikut adalah contoh implementasi menggunakan **AdaBoostClassifier** dari Scikit-learn:

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Data pelatihan (X_train, y_train)
# Model dasar (decision tree)
base_model = DecisionTreeClassifier(max_depth=1)

# Model AdaBoost
model = AdaBoostClassifier(base_model, n_estimators=50, learning_rate=1.0)

# Melatih model
model.fit(X_train, y_train)

# Prediksi
predictions = model.predict(X_test)
```
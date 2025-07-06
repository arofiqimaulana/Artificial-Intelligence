# Algoritma Boosting dalam Machine Learning

Boosting adalah teknik dalam **ensemble learning** yang menggabungkan banyak model lemah (weak learners) untuk membentuk model yang kuat. Berikut ini adalah beberapa algoritma boosting yang paling populer:

## ✅ Daftar Algoritma Boosting

| Nama Algoritma | Penjelasan Singkat |
|----------------|---------------------|
| **AdaBoost (Adaptive Boosting)** | Menggabungkan beberapa model lemah (biasanya decision tree stump) secara iteratif, fokus pada kesalahan sebelumnya. |
| **Gradient Boosting (GB)** | Menggunakan pendekatan gradient descent untuk meminimalkan loss. Tiap model baru belajar dari kesalahan model sebelumnya. |
| **XGBoost (Extreme Gradient Boosting)** | Versi upgrade dari Gradient Boosting, lebih cepat dan efisien. Populer karena performa tinggi di kompetisi data science. |
| **LightGBM (Light Gradient Boosting Machine)** | Dibuat oleh Microsoft. Lebih cepat dari XGBoost untuk dataset besar, menggunakan histogram-based algorithm. |
| **CatBoost (Categorical Boosting)** | Dikembangkan oleh Yandex. Dirancang untuk menangani data kategorikal secara otomatis dan efisien. |
| **Gradient Boosted Regression Trees (GBRT)** | Nama lain untuk gradient boosting, khusus untuk regresi. |
| **Stochastic Gradient Boosting** | Variasi dari GB yang menggunakan subset data (stochastic) untuk menghindari overfitting. |
| **Histogram-Based Gradient Boosting** | Versi lebih efisien dari GB, digunakan dalam LightGBM dan scikit-learn (`HistGradientBoosting`). |

## ⚠️ Catatan
Semua algoritma di atas menggunakan prinsip dasar yang sama: **memperbaiki kesalahan dari model sebelumnya**, namun berbeda dalam cara training, optimasi, dan penanganan data.

### Tips:
- Gunakan **XGBoost** untuk performa tinggi di kompetisi.
- Gunakan **LightGBM** jika dataset sangat besar dan butuh kecepatan.
- Gunakan **CatBoost** untuk data dengan banyak fitur kategorikal.


# 🌲 Algoritma Decision Tree C5.0

**C5.0** adalah algoritma pohon keputusan yang merupakan versi lanjutan dari **C4.5**, dikembangkan oleh **Ross Quinlan**. C5.0 dirancang untuk mengatasi keterbatasan C4.5 dan menawarkan efisiensi serta akurasi yang lebih tinggi, terutama pada dataset besar.

---

## 🧠 Apa Itu C5.0?

C5.0 adalah algoritma klasifikasi yang menggunakan pendekatan pohon keputusan dan berbasis pada prinsip **information gain** dan **gain ratio** seperti C4.5, namun lebih cepat, lebih hemat memori, dan mendukung fitur tambahan seperti **boosting**.

---

## 🚀 Keunggulan C5.0 dibandingkan C4.5

| Fitur                | C4.5         | C5.0                        |
|----------------------|--------------|-----------------------------|
| Kecepatan            | Lebih lambat | Jauh lebih cepat            |
| Penggunaan memori    | Lebih besar  | Lebih efisien               |
| Boosting             | Tidak ada    | Didukung                    |
| Handling missing data| Ada          | Ada                         |
| Interpretasi hasil   | Tersedia     | Tersedia                    |
| Fitur rule set       | Tidak        | Ya (ruleset dari tree)      |

---

## ⚙️ Cara Kerja C5.0 (Umum)

1. Hitung **entropy** dan **information gain** dari atribut.
2. Gunakan **gain ratio** untuk memilih atribut terbaik.
3. Bentuk **decision tree** dari atribut terbaik tersebut.
4. Terapkan teknik **boosting** untuk meningkatkan akurasi (opsional).
5. Lakukan **pruning** untuk mencegah overfitting.
6. Hasil akhir dapat berupa tree atau **ruleset**.

---

## 🔍 Fitur Tambahan C5.0

- Mendukung **boosting** (ensembling beberapa tree)
- Output dapat berupa **ruleset**
- Bisa memberikan **confidence level** pada prediksi
- Menangani missing values dan atribut numerik/kategorikal

---

## 🧪 Penerapan C5.0 di Python

Python belum menyediakan implementasi C5.0 secara langsung di scikit-learn. Namun kamu bisa:

### ✅ 1. Gunakan `C50` di R
```R
library(C50)
model <- C5.0(Species ~ ., data = iris)
summary(model)
```

### ✅ 2. Gunakan `sklearn` dengan `entropy` sebagai pendekatan
```python
from sklearn.tree import DecisionTreeClassifier

# Pendekatan mendekati C5.0
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X_train, y_train)
```

---

## 📘 Referensi

- Quinlan, J. R. (1993). *C4.5: Programs for Machine Learning*
- Quinlan, J. R. (2004). *Data Mining Tools See5 and C5.0*
- [Wikipedia - C5.0 Algorithm](https://en.wikipedia.org/wiki/C4.5_algorithm)
- [C50 Package for R](https://cran.r-project.org/web/packages/C50/index.html)
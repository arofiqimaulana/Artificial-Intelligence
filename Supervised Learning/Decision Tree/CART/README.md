# 🌳 Algoritma Decision Tree CART

**CART (Classification and Regression Trees)** adalah algoritma pohon keputusan yang dikembangkan oleh **Breiman et al. (1986)**. Berbeda dengan ID3 dan C4.5, CART dapat digunakan untuk **klasifikasi** maupun **regresi**, dan selalu menghasilkan **pohon biner**.

---

## 🧠 Apa Itu CART?

CART membagi dataset dengan cara memilih fitur dan nilai split terbaik berdasarkan **Gini Impurity** (untuk klasifikasi) atau **Mean Squared Error (MSE)** (untuk regresi). Hasil dari model CART adalah struktur pohon biner di mana setiap node internal memiliki dua cabang.

---

## ⚙️ Cara Kerja CART

### Untuk Klasifikasi:
1. Untuk setiap atribut dan nilai threshold, hitung **Gini Impurity** dari split.
2. Pilih split dengan penurunan impurity terbesar.
3. Bagi data berdasarkan split tersebut.
4. Ulangi hingga terpenuhi kondisi penghentian (misal: maksimal kedalaman pohon, jumlah minimum sampel, atau impurity minimum).

### Untuk Regresi:
1. Hitung nilai rata-rata target.
2. Gunakan **MSE (Mean Squared Error)** untuk menentukan split terbaik.
3. Lanjutkan pembentukan pohon hingga kondisi berhenti.

---

## 📚 Rumus Penting

### Gini Impurity:
$$
Gini(D) = 1 - \sum_{i=1}^{n} p_i^2
$$

### MSE (untuk regresi):
$$
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y})^2
$$

---

## ✅ Kelebihan CART

- Mendukung **klasifikasi dan regresi**.
- Menghasilkan **pohon biner**, mudah diinterpretasi.
- Dapat menangani data numerik dan kategorikal.
- Didukung secara luas dalam library Python (scikit-learn).

---

## ⚠️ Kekurangan CART

- Rentan terhadap **overfitting** (perlu pruning atau max depth).
- Pemilihan split bisa bias terhadap fitur dengan banyak level.

---

## 🧪 Contoh Penerapan CART di Python

```python
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.datasets import load_iris, load_boston

# Klasifikasi dengan CART
X_class, y_class = load_iris(return_X_y=True)
clf = DecisionTreeClassifier(criterion='gini')
clf.fit(X_class, y_class)

# Regresi dengan CART
X_reg, y_reg = load_boston(return_X_y=True)
reg = DecisionTreeRegressor(criterion='squared_error')
reg.fit(X_reg, y_reg)
```

---

## 📘 Referensi

- Breiman, L., Friedman, J., Stone, C. J., & Olshen, R. A. (1986). *Classification and Regression Trees*.
- [Wikipedia - CART Algorithm](https://en.wikipedia.org/wiki/Decision_tree_learning)
- [Scikit-learn Decision Trees](https://scikit-learn.org/stable/modules/tree.html)


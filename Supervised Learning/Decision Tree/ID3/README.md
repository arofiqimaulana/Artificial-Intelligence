# 🌳 Algoritma Decision Tree ID3

**ID3 (Iterative Dichotomiser 3)** adalah algoritma pohon keputusan yang diperkenalkan oleh **J. Ross Quinlan**. Algoritma ini merupakan salah satu yang paling dasar dan menjadi pondasi dari algoritma lanjutan seperti C4.5 dan C5.0.

---

## 🧠 Apa Itu ID3?

ID3 membangun pohon keputusan dari dataset berlabel menggunakan **Information Gain** untuk memilih atribut terbaik pada setiap langkah pemisahan (split). Cocok digunakan untuk data kategorikal.

---

## ⚙️ Cara Kerja ID3

1. Hitung **Entropy** dari dataset.
2. Hitung **Information Gain** dari setiap atribut.
3. Pilih atribut dengan Information Gain tertinggi sebagai node.
4. Bagi dataset berdasarkan nilai atribut tersebut.
5. Ulangi proses untuk setiap subset hingga seluruh data terklasifikasi atau tidak ada lagi atribut yang tersisa.

---

## 📚 Rumus Penting

### Entropy:
\[
Entropy(S) = - \sum p_i \log_2(p_i)
\]

### Information Gain:
\[
Gain(S, A) = Entropy(S) - \sum \left( \frac{|S_v|}{|S|} \times Entropy(S_v) \right)
\]

---

## ✅ Kelebihan ID3

- Sederhana dan mudah dipahami.
- Cepat untuk dataset kecil dan menengah.
- Baik untuk data kategorikal.

---

## ⚠️ Kekurangan ID3

- Tidak mendukung atribut numerik secara langsung.
- Rentan terhadap **overfitting**.
- Tidak melakukan **pruning**.
- Bias terhadap atribut dengan banyak nilai.

---

## 🧪 Contoh Penerapan ID3 di Python (menggunakan `sklearn` approximation)

Scikit-learn tidak menyediakan ID3 secara eksplisit, namun pendekatan mirip bisa dilakukan:

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# Menggunakan entropy (mirip ID3)
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X, y)
```

Untuk ID3 murni, kamu bisa menggunakan pustaka seperti `id3` atau `sklearn-id3` dari PyPI.

```bash
pip install sklearn-id3
```

---

## 📘 Referensi

- Quinlan, J. R. (1986). *Induction of Decision Trees*. Machine Learning Journal.
- [Wikipedia - ID3 Algorithm](https://en.wikipedia.org/wiki/ID3_algorithm)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/modules/tree.html)


# 🌳 Algoritma Decision Tree C4.5

Algoritma **C4.5** adalah pengembangan dari algoritma **ID3** yang digunakan untuk membangun pohon keputusan dalam klasifikasi. Diperkenalkan oleh **Ross Quinlan**, C4.5 menyempurnakan kelemahan ID3 dan menjadi dasar dari banyak algoritma modern, termasuk **J48** yang digunakan di Weka.

---

## 🧠 Apa Itu C4.5?

C4.5 membentuk decision tree berdasarkan **information gain ratio** dari setiap atribut, dan mampu menangani:
- Fitur **numerik** dan **kategorikal**
- Data yang **hilang**
- **Pruning** (pemangkasan) untuk mengurangi overfitting

---

## ⚙️ Cara Kerja C4.5

1. **Hitung Entropy** dari dataset.
2. **Hitung Gain** dari setiap atribut.
3. **Hitung Gain Ratio** (penyesuaian gain berdasarkan jumlah partisi).
4. Pilih atribut dengan **gain ratio tertinggi** sebagai node.
5. Ulangi langkah-langkah di atas hingga semua data terklasifikasi atau tidak bisa dibagi lagi.
6. **Lakukan pruning** untuk mengurangi kompleksitas tree.

---

## 📚 Rumus Penting

### Entropy:
$$
Entropy(S) = - \sum p_i \log_2(p_i)
$$

### Information Gain:
$$
Gain(S, A) = Entropy(S) - \sum \left( \frac{|S_v|}{|S|} \times Entropy(S_v) \right)
$$

### Gain Ratio:
$$
GainRatio(A) = \frac{Gain(S, A)}{SplitInfo(A)}
$$

---

## ✅ Kelebihan C4.5

- Bisa menangani atribut numerik.
- Mampu mengatasi data kosong (missing values).
- Menghindari bias terhadap atribut dengan banyak nilai melalui **Gain Ratio**.
- Menerapkan **post-pruning** untuk menghindari overfitting.

---

## ⚠️ Kekurangan C4.5

- Kompleksitas tinggi untuk dataset besar.
- Bisa lambat jika jumlah atribut dan data sangat banyak.

---

## 🧪 Contoh Penerapan di Python (Menggunakan `sklearn` approximation)

Walaupun `scikit-learn` tidak langsung menyediakan C4.5, kamu bisa menggunakan `DecisionTreeClassifier` dengan parameter `criterion='entropy'` sebagai pendekatan.

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Load dataset
X, y = load_iris(return_X_y=True)

# Buat model dengan entropy (mendekati C4.5)
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf = clf.fit(X, y)

# Visualisasi pohon
tree.plot_tree(clf, filled=True)
```

---

## 📘 Referensi

- Quinlan, J. R. (1993). *C4.5: Programs for Machine Learning*.
- [Wikipedia - C4.5 Algorithm](https://en.wikipedia.org/wiki/C4.5_algorithm)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/modules/tree.html)

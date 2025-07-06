# 📊 Decision Tree - Panduan Lengkap

Decision Tree adalah salah satu algoritma **machine learning** yang digunakan untuk **klasifikasi dan regresi**. Algoritma ini bekerja seperti struktur pohon, di mana setiap node merepresentasikan kondisi berdasarkan fitur, dan cabangnya merepresentasikan hasil dari kondisi tersebut.

---

## 🧠 Apa Itu Decision Tree?

Decision Tree adalah model prediktif yang memetakan observasi dari sebuah item ke kesimpulan mengenai target nilai item tersebut. Biasanya digunakan dalam supervised learning.

Contohnya mirip seperti proses pengambilan keputusan:  
"Kalau hujan → bawa payung; kalau tidak → tidak usah bawa."

---

## 🔄 Jenis Algoritma Decision Tree

| Algoritma        | Penjelasan Singkat |
|------------------|--------------------|
| **ID3 (Iterative Dichotomiser 3)** | Menggunakan **entropy** dan **information gain** untuk membangun tree. Cocok untuk data kategorikal. |
| **C4.5**         | Penyempurnaan ID3. Menggunakan **gain ratio** dan bisa menangani data numerik. |
| **CART (Classification and Regression Tree)** | Menggunakan **Gini Index** sebagai pengukuran, mendukung klasifikasi dan regresi. |
| **CHAID**        | Cocok untuk data nominal, menggunakan chi-square untuk split. |

---

## ⚖️ Perbandingan Algoritma Decision Tree

| Kriteria        | ID3            | C4.5           | CART            |
|-----------------|----------------|----------------|-----------------|
| Split Metric    | Information Gain | Gain Ratio     | Gini Index      |
| Output          | Multi-way Tree | Multi-way Tree | Binary Tree     |
| Data Type       | Kategorikal     | Campuran       | Campuran        |
| Pruning         | Tidak ada       | Ada            | Ada             |

---

## 📚 Istilah Penting dalam Decision Tree

| Istilah            | Penjelasan |
|--------------------|------------|
| **Entropy**        | Mengukur ketidakpastian dalam data. Semakin tinggi, semakin acak. |
| **Information Gain** | Mengukur seberapa banyak "informasi" yang diperoleh dari membagi data berdasarkan fitur tertentu. |
| **Gain Ratio**     | Perbaikan dari Information Gain yang mempertimbangkan jumlah cabang dari split. |
| **Gini Index**     | Alternatif dari entropy, mengukur ketidaksamaan suatu dataset. |
| **Overfitting**    | Ketika pohon terlalu kompleks dan tidak bisa digeneralisasikan ke data baru. |
| **Pruning**        | Proses mengurangi ukuran tree agar lebih sederhana dan menghindari overfitting. |

---

## 🧪 Kapan Menggunakan Decision Tree?

- Saat interpretabilitas model penting.
- Ketika dataset memiliki kombinasi fitur kategorikal dan numerik.
- Untuk baseline model yang cepat dibangun.

---

## 📘 Referensi Tambahan

- [Scikit-learn DecisionTreeClassifier Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [Wikipedia: Decision Tree](https://en.wikipedia.org/wiki/Decision_tree_learning)


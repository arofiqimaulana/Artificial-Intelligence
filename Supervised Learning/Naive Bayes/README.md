# 🤖 Naive Bayes - Penjelasan dan Implementasi

## 📌 Deskripsi

**Naive Bayes** adalah algoritma klasifikasi berbasis probabilistik yang menggunakan **Teorema Bayes** dengan asumsi "naive" (sederhana), yaitu bahwa setiap fitur pada data saling bebas (independen). Meskipun asumsi ini jarang berlaku di dunia nyata, algoritma ini terbukti sangat efektif dalam banyak aplikasi, terutama dalam pemrosesan teks seperti **klasifikasi email spam**, **analisis sentimen**, dan lainnya.

## 🧠 Konsep Dasar

- Berdasarkan **Teorema Bayes**:

P(C|X) = P(X|C) * P(C) / P(X)


Di mana:
- `P(C|X)`: Probabilitas kelas C diberikan fitur X.
- `P(X|C)`: Probabilitas fitur X diberikan kelas C.
- `P(C)`: Probabilitas awal kelas C.
- `P(X)`: Probabilitas awal fitur X.

- **Naive Assumption**: Fitur-fitur dianggap independen satu sama lain.

## ✅ Kelebihan

- Cepat dan efisien, bahkan pada dataset besar.
- Tidak memerlukan banyak data untuk pelatihan.
- Bekerja baik pada data kategorikal.
- Mudah diimplementasikan dan diinterpretasikan.

## ⚠️ Kekurangan

- Asumsi independensi antar fitur jarang benar dalam kenyataan.
- Kurang akurat dibanding algoritma kompleks pada data yang tidak memenuhi asumsi naive.

## 🧪 Jenis Naive Bayes

- **Gaussian Naive Bayes**: Untuk fitur numerik (distribusi normal).
- **Multinomial Naive Bayes**: Umumnya digunakan untuk pemodelan teks.
- **Bernoulli Naive Bayes**: Cocok untuk fitur biner (true/false).

## 🔧 Implementasi Sederhana (Python)

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load data
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi dan latih model
model = GaussianNB()
model.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = model.predict(X_test)
print("Akurasi:", accuracy_score(y_test, y_pred))

📚 Referensi
- Scikit-learn: Naive Bayes
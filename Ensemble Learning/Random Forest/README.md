# 📊 Random Forest
## 📌 Deskripsi
Random Forest adalah algoritma machine learning yang termasuk dalam metode ensemble learning. Algoritma ini bekerja dengan membuat banyak decision tree selama proses pelatihan dan menggabungkan hasil dari masing-masing pohon untuk meningkatkan akurasi dan mengurangi overfitting. Random Forest dapat digunakan untuk klasifikasi maupun regresi.

## 🧠 Konsep Dasar
- Ensemble Learning: Menggabungkan beberapa model untuk menghasilkan prediksi yang lebih baik.

- Bagging (Bootstrap Aggregating): Random Forest menggunakan teknik ini dengan membuat subset data secara acak dan membangun decision tree untuk masing-masing subset.

- Voting/Averaging: Untuk klasifikasi, hasil dari setiap decision tree di-voting. Untuk regresi, hasilnya dirata-rata.

## ✅ Kelebihan
- Mengurangi overfitting dibanding decision tree tunggal.
- Bekerja baik pada dataset yang besar dan kompleks.
- Dapat menangani data numerik dan kategorikal.
- Memiliki estimasi feature importance.

## ⚠️ Kekurangan
- Kurang interpretatif dibanding decision tree tunggal.
- Memerlukan lebih banyak waktu komputasi dan memori.

## 🔧 Code
```
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi dan latih model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = model.predict(X_test)
print("Akurasi:", accuracy_score(y_test, y_pred))
```

## 📚 Referensi
- Scikit-learn: Random Forest
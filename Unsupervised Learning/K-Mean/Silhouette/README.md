
# 📄 Silhouette dalam Clustering

## 📌 Apa itu Silhouette?
**Silhouette** adalah metrik untuk mengevaluasi kualitas hasil clustering.  
Nilai silhouette mengukur **seberapa mirip suatu objek dengan cluster-nya sendiri** dibandingkan dengan cluster terdekat lainnya.

Rentang nilai:  
- **+1** → objek sangat cocok dengan cluster sendiri dan jauh dari cluster lain  
- **0** → objek berada di batas antara dua cluster  
- **< 0** → objek kemungkinan salah penempatan (lebih dekat ke cluster lain)  

---

## 📐 Rumus Silhouette untuk 1 titik data
Untuk suatu titik \( i \):

\[
s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}}
\]

Keterangan:
- \( a(i) \) = rata-rata jarak titik \( i \) ke semua titik dalam cluster yang sama (**intra-cluster distance**)
- \( b(i) \) = jarak rata-rata titik \( i \) ke semua titik di **cluster terdekat lainnya** (**nearest-cluster distance**)
- \( s(i) \) = skor silhouette untuk titik \( i \)

---

## 🎯 Interpretasi Nilai Silhouette
| Nilai       | Interpretasi                                                                 |
|-------------|-------------------------------------------------------------------------------|
| 0.71 – 1.00 | Struktur cluster sangat baik                                                  |
| 0.51 – 0.70 | Struktur cluster baik                                                         |
| 0.26 – 0.50 | Struktur cluster cukup, bisa ditingkatkan                                     |
| ≤ 0.25      | Struktur cluster lemah, kemungkinan jumlah cluster tidak tepat atau data tumpang tindih |

---

## 🔍 Kegunaan Silhouette
1. **Menentukan jumlah cluster terbaik** → coba berbagai nilai k dan pilih yang memberi rata-rata silhouette tertinggi.
2. **Evaluasi kualitas clustering** → identifikasi apakah ada cluster yang tidak konsisten.
3. **Analisis distribusi data** → melihat apakah data tumpang tindih antar cluster.

---

## ⚙️ Contoh Implementasi di Python

```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Buat data contoh
X, _ = make_blobs(n_samples=500, centers=4, cluster_std=0.6, random_state=42)

# Uji beberapa nilai k
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X)
    score = silhouette_score(X, labels)
    print(f"k={k}, silhouette score={score:.3f}")
```

---

## 📊 Silhouette Diagram
**Silhouette diagram** menampilkan distribusi nilai silhouette untuk setiap cluster.  
Tujuannya:
- Melihat bentuk & konsistensi tiap cluster  
- Mengidentifikasi cluster dengan anggota yang banyak “negatif” (potensi salah cluster)  

---

## ⚠️ Tips & Best Practice
- **Normalisasi data** terlebih dahulu agar jarak antar fitur setara.  
- Jangan hanya bergantung pada silhouette—cek juga visualisasi dan konteks domain.  
- Perhatikan **ukuran cluster**; skor tinggi tapi cluster kecil bisa menyesatkan.

---

## 📚 Referensi
- Rousseeuw, P.J. (1987). *Silhouettes: a graphical aid to the interpretation and validation of cluster analysis*. Journal of Computational and Applied Mathematics, 20, 53–65.
- [Scikit-learn: Silhouette Coefficient](https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient)

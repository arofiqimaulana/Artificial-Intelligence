
# 📄 Teknik Pemilihan Jumlah Cluster (k) dengan Metode Elbow

## 📌 Apa itu Metode Elbow?
Metode **Elbow** adalah teknik untuk menentukan jumlah cluster optimal dalam algoritma *clustering* (seperti K-Means) dengan memplot **Within-Cluster Sum of Squares (WCSS)** terhadap jumlah cluster k.

**Inti idenya:**  
- Saat k bertambah, WCSS akan semakin kecil.  
- Namun, setelah titik tertentu, penurunan WCSS menjadi lambat — membentuk “siku” (*elbow*). Titik ini adalah jumlah cluster optimal.

---

## 📐 Rumus WCSS
**WCSS** mengukur jumlah kuadrat jarak setiap titik ke pusat cluster-nya:


$$ WCSS = \sum_{j=1}^{k} \sum_{x_i \in C_j} ||x_i - \mu_j||^2 $$

Keterangan:
- \( C_j \) = cluster ke-j
- \( \mu_j \) = centroid cluster ke-j
- \( x_i \) = titik data
- \( ||x_i - \mu_j||^2 \) = kuadrat jarak antara titik dan centroid

---

## 🎯 Langkah-langkah Metode Elbow
1. Tentukan rentang k yang ingin diuji (mis. 1–10).  
2. Jalankan algoritma *clustering* (mis. K-Means) untuk setiap k.  
3. Hitung **WCSS** untuk setiap k.  
4. Plot k (sumbu X) vs WCSS (sumbu Y).  
5. Cari titik “siku” di grafik, yaitu k optimal.

---

## ⚙️ Contoh Implementasi di Python

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Buat data contoh
X, _ = make_blobs(n_samples=500, centers=5, cluster_std=0.6, random_state=42)

# Simpan WCSS untuk berbagai k
wcss = []
K = range(1, 11)
for k in K:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X)
    wcss.append(km.inertia_)

# Plot Elbow
plt.plot(K, wcss, marker='o')
plt.title('Metode Elbow')
plt.xlabel('Jumlah Cluster (k)')
plt.ylabel('WCSS')
plt.show()
```

---

## 📊 Interpretasi Grafik Elbow
- **Sebelum elbow** → WCSS turun tajam, penambahan cluster signifikan mengurangi error.
- **Setelah elbow** → Penurunan WCSS kecil, penambahan cluster tidak memberi perbaikan signifikan.
- **Titik elbow** → Jumlah cluster yang efisien (trade-off antara akurasi dan kompleksitas).

---

## ⚠️ Tips & Best Practice
- Normalisasi data sebelum menggunakan K-Means untuk menghindari bias fitur dengan skala besar.
- Elbow tidak selalu jelas; jika sulit terlihat, pertimbangkan metrik lain seperti **Silhouette Score** atau **Gap Statistic**.
- Jangan hanya bergantung pada Elbow — gunakan pemahaman domain.

---

## 📚 Referensi
- Kodinariya, T.M. & Makwana, P.R. (2013). *Review on determining number of Cluster in K-Means Clustering*. International Journal of Advance Research in Computer Science and Management Studies.
- [Scikit-learn KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

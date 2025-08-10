
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

## 📊 Perbandingan

| Aspek | Elbow Method | Silhouette Method |
|-------|--------------|-------------------|
| **Tujuan** | Menentukan jumlah cluster dengan melihat penurunan *Within-Cluster Sum of Squares* (WCSS) | Menilai kualitas clustering dengan mengukur seberapa dekat titik ke cluster-nya dibandingkan cluster terdekat lain |
| **Metrik yang digunakan** | WCSS (*inertia*) = total kuadrat jarak dari setiap titik ke centroid cluster | Silhouette Score = rasio perbedaan jarak rata-rata dalam cluster sendiri (*a*) dan ke cluster terdekat (*b*) |
| **Nilai hasil** | Tidak ada batas nilai baku, hanya melihat bentuk kurva | Rentang nilai: -1 sampai +1 |
| **Cara interpretasi** | Cari titik “siku” pada grafik WCSS vs k, di mana penurunan mulai melambat | Nilai mendekati +1 = cluster jelas, 0 = di batas, <0 = salah penempatan |
| **Kelebihan** | - Sederhana dan cepat\n- Mudah divisualisasi | - Memberi ukuran kualitas cluster yang jelas\n- Bisa membandingkan beberapa k secara objektif |
| **Kekurangan** | - Siku kadang tidak jelas\n- Hanya berbasis WCSS, tidak melihat pemisahan antar cluster | - Lebih mahal secara komputasi untuk dataset besar\n- Tidak langsung memberi info “siku” |
| **Kapan cocok dipakai** | Saat ingin estimasi awal jumlah cluster secara visual | Saat ingin mengukur dan membandingkan kualitas clustering untuk beberapa k |

---

## 📌 Kesimpulan
- **Elbow** → fokus ke *jumlah cluster optimal* dari sudut *kompresi jarak dalam cluster*.
- **Silhouette** → fokus ke *kualitas pemisahan cluster* antar data.

📚 **Rekomendasi:** Gunakan keduanya secara bersamaan:  
1. Gunakan **Elbow** untuk estimasi awal jumlah cluster.  
2. Gunakan **Silhouette** untuk memvalidasi kualitas cluster tersebut.

---

## 📚 Referensi
- Kodinariya, T.M. & Makwana, P.R. (2013). *Review on determining number of Cluster in K-Means Clustering*. International Journal of Advance Research in Computer Science and Management Studies.
- [Scikit-learn KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- Rousseeuw, P.J. (1987). *Silhouettes: a graphical aid to the interpretation and validation of cluster analysis*. Journal of Computational and Applied Mathematics, 20, 53–65.
- Kodinariya, T.M. & Makwana, P.R. (2013). *Review on determining number of Cluster in K-Means Clustering*. International Journal of Advance Research in Computer Science and Management Studies.

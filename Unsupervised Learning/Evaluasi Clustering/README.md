## Evaluasi Clustering
Evaluasi clustering penting untuk mengetahui seberapa baik model clustering yang dihasilkan, terutama dalam hal seberapa terpisah atau terdistribusi cluster yang terbentuk.

## 1. Inertia (SSE) - Sum of Squared Errors

Inertia mengukur seberapa dekat titik data di dalam cluster dengan pusat cluster (centroid). Nilai inertia yang lebih rendah menunjukkan bahwa titik data lebih dekat ke pusat cluster.

Cara Menghitung:

Inertia dihitung sebagai jumlah kuadrat jarak dari setiap titik data ke pusat cluster terdekat.
```
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate data
X, _ = make_blobs(n_samples=100, centers=3)

# Fit KMeans model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Calculate Inertia
inertia = kmeans.inertia_

```

## 2. Silhouette Score

Silhouette Score mengukur seberapa mirip objek dalam satu cluster dibandingkan dengan objek di cluster lain. Nilai silhouette score berkisar antara -1 hingga 1, dimana 1 menunjukkan pemisahan cluster yang sangat baik.

Cara Menghitung:

Silhouette score dihitung dengan menggunakan jarak rata-rata antar titik dalam cluster (cohesion) dan jarak rata-rata antar cluster (separation).

```
from sklearn.metrics import silhouette_score

# Fit model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Calculate Silhouette Score
silhouette_avg = silhouette_score(X, kmeans.labels_)

```

## 3. Davies-Bouldin Index

Davies-Bouldin Index mengukur kualitas clustering berdasarkan rasio antara jarak antar pusat cluster dan ukuran cluster. Nilai yang lebih rendah menunjukkan cluster yang lebih terpisah dan lebih baik.

Cara Menghitung:

Davies-Bouldin dihitung sebagai rata-rata rasio antara jarak antara cluster dan ukuran cluster di dalamnya.

```
from sklearn.metrics import davies_bouldin_score

# Calculate Davies-Bouldin Index
db_index = davies_bouldin_score(X, kmeans.labels_)
```

## 4. Calinski-Harabasz Index

Calinski-Harabasz Index, atau Variance Ratio Criterion (VRC), mengukur pemisahan antara cluster dan seberapa padat masing-masing cluster. Nilai yang lebih tinggi menunjukkan hasil clustering yang lebih baik.

Cara Menghitung:

Indeks ini dihitung sebagai rasio antara variasi antar cluster dan variasi dalam cluster.

```
from sklearn.metrics import calinski_harabasz_score

# Calculate Calinski-Harabasz Index
ch_index = calinski_harabasz_score(X, kmeans.labels_)
```

## 5. Elbow Method

Elbow Method digunakan untuk memilih jumlah cluster optimal dengan mengamati penurunan Inertia (SSE) saat jumlah cluster meningkat. Titik dimana penurunan inertia mulai melambat (sudut siku) disebut sebagai "elbow" dan merupakan jumlah cluster yang optimal.

Cara Menghitung:

Plot nilai inertia terhadap jumlah cluster dan identifikasi titik elbow.

```
import matplotlib.pyplot as plt

inertia_values = []
for n_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)
    inertia_values.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia_values)
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

```
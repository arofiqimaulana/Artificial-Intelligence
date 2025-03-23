# Perbandingan antara Bag of Words (BoW) dan Word Embedding

| **Aspek**                     | **Bag of Words (BoW)**                                    | **Word Embedding**                                      |
|--------------------------------|------------------------------------------------------------|----------------------------------------------------------|
| **Definisi**                   | Model yang mewakili teks sebagai kumpulan kata tanpa urutan, berdasarkan frekuensi kata. | Representasi kata dalam bentuk vektor berdimensi rendah yang mencerminkan makna semantik kata tersebut. |
| **Representasi**               | Setiap kata diwakili dengan frekuensi atau apakah kata tersebut ada dalam dokumen (misalnya, dengan 0 atau 1). | Setiap kata diwakili dengan vektor angka dalam ruang berdimensi rendah yang menangkap konteks semantik kata tersebut. |
| **Konteks dan Urutan**         | Mengabaikan urutan kata, hanya mempertimbangkan kemunculan kata dalam dokumen. | Mempertimbangkan konteks kata dalam kalimat, sehingga kata dengan makna yang serupa akan berada dekat dalam ruang vektor. |
| **Sparsity**                   | Vektor BoW seringkali sangat **sparse** (banyak nilai 0) karena jumlah kata yang besar. | Vektor embedding lebih **dense** (lebih sedikit nilai 0) karena dimensi vektornya lebih kecil dan efisien. |
| **Dimensi**                    | Dimensi vektor BoW sangat besar, tergantung pada ukuran kosa kata (vocabulary). | Dimensi vektor embedding jauh lebih kecil (misalnya, 100-300 dimensi) meskipun menangkap informasi semantik. |
| **Metode Pembelajaran**        | Frekuensi kata dihitung secara langsung, tidak memperhitungkan hubungan antar kata. | Pembelajaran dilakukan dengan cara mengoptimalkan representasi vektor untuk menangkap konteks dan hubungan antar kata. |
| **Kelebihan**                  | Sederhana, mudah dipahami, dan diimplementasikan. | Menangkap hubungan semantik antar kata, lebih efisien dalam menangani kata-kata dengan makna serupa. |
| **Kekurangan**                 | Tidak menangkap konteks kata dan hubungan antar kata (kata yang serupa tapi berbeda konteks diperlakukan terpisah). | Memerlukan waktu pelatihan dan komputasi yang lebih besar untuk menghasilkan vektor embedding yang baik. |

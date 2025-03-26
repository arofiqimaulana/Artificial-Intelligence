# README
## Word Embeding
-  Adalah proses konversi sebuah teks menjadi sebuah vektor/array yang terdiri dari kumpulan angka. 
- Teknik ini diperlukan karena Algoritma ML/AI tidak mampu mengolah input dalam bentuk string/teks
- Angka tersebut melukiskan urutan di kamus kata yang kita miliki
- One hot-encoding akan mempunyai ukuran vektor yang sangat besar dan tidak memberikan informasi kedekatan antar kata. 
- Kelemahan one-hot encoding tsb diatasi oleh word embedding yang dapat mengubah kata menjadi sebuah vektor yang berisi angka-angka dengan ukuran yang cukup kecil untuk mengandung informasi yang lebih banyak.


## Vector Space Model (VSM)
    ○ VSM dilakukan dengan merepresentasikan setiap dokumen dalam bentuk vektor -> tingkat kemiripan antar dokumen dilakukan dengan menghitung penyimpandan sudut antar vektor
    ○ VSM bekerja dengan melihat kecocokan term (term similaritu) antara query dan corpus
    ○ VSM tidak mampu menangani masalah sinonim 
    ○ Akurasi perhitungan similarity menjadi rendah karena dokumen direpresentasikan ke dalam dimensi ruang besar (space) dan jarang (sparse)
## Latent Semantic Analysis (LSA)
    ○ Pengembangan dari metode VSM (mengatasi masalah sinonim)
    ○ Salah satu topic modeling yang merepresentasikan dokumen ke dalam ruang topik (topic space)
    ○ LSA mengambil kata-kata penting dari informasi yang diberikan oleh dokumen dan menangkap kesamaan semantik antara kata-kata sehingga mampu menangani masalah sinonim
    ○ LSA mereduksi dimensi ruang vektor sehingga punya kaurasi yang lebih daripada VSM
    ○ Namnun LSA menyebabkan masalah polysemi
## Probabilistic Latent Semantic Analysis (PLSA)
    ○ Algoritma yang diterapkan untuk memperkirakan makna sekumpulan teks menjadi suatu cluster atau kelompok tertentu sehingga mempermudah para analsis untuk menarik kesimpulan dari pengelompokan yang terbentuk
    ○ Menggabungkan teori klasik tentang VSM, Singular Value Decomposition, model variabel latent untuk mendapatkan kelompok (latent) dari sekumpulan teks (bag of word)
    ○ LSA dan PLSA mengabaikan urutan kata

## Latent Dirichlet Allocation (LDA)
- Termasuk dalam topic modeling
- Termasuk dalam soft/fuzzy clustering karena satu objek bisa mempunyai lebih dari satu topik
- Konsep topic modeling terdiri dari "kata" , "dokumen" dan "corpora"
    1. kata" : token
    2. "dokumen" : rangkaian/susunan token
    3. "corpora" : kumpulan dokumen
    4. "topic" : distribusi dari beberapa kosakata yang bersifat tetap
- Teknik yang bisa digunakan dalam topic modeling
    ○ VSM (Vector Space Model)
    ○ LSA (Latent Semantic Analysis)
    ○ PLSA (Probabilistic Latent Semantic Analysis)
    ○ LDA (Latent Dirichlet Allocation)
    ○ Pengembangan dari PLSA yang lebih stabil dalam mengolah data dalam jumlah besar
    ○ LDA mengasumsikan bahwa satu dokumen terdapat lebih dari satu topik, yang masing masing merupakan distribusi melalui kosakata
    ○ Digunakan untuk analisis pada dokumen yang sangat besar
    ○ Digunakn untuk meringkas, pengelompokan, menghubungkan maupun memproses data
    ○ Merupakan model probabilistik generatif dari suatu korpus
    ○ Ide dasar model LDA adalah suatu dokumen yang direpresentasikan sebagai model campuran dari berbagai topik yang dapat disebut juga laten, setiap topik dikarekterisasikan oleh kata.
    ○ Terdapat variabel laten yang dapat menjelaskan variabel teramati
        § Variabel teramati : dokumen
        § Variabel latent : topik
    ○ Cara kerja LDA adalah memasukkan kumpulan dokuemn dan beberapa parameter yang ditentukan -> dilakukan LDA -> yang menghasilkan model yang terdiri dari bobot yang dapat dinormalisasi terhadap probabilitas.
    ○ Probabilistik muncul dalam 2 jenis
        § Probabilitas bahwa dokumen tertentu menghasilkan topik tertentu pada suatu posisi
        § Probabilitas bahwa topik tertentu menghasilkan kata tertentu dari kumpulan perbendaharaan kata
    ○ Berapa jumlah topic yang seharusnya dipakai diperoleh dari trial dan error maupun menggunakan topic coherence
- Topic Modeling
    ○ Bertujuan untuk menemukan suatu topik yang tersembunyi dari rangkaian kata pada dokumen yang tidak terstruktur
    ○ Teknik ini menganalisis dari teks asli, bagaimana topik-topik saling terhubung dengan satu yang lain, bagaimana tema-tema bisa berubah dari waktu ke waktu
- Topic Coherence
        


### Perbandingan antara Bag of Words (BoW) dan Word Embedding

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

## Teorema Bayes
Teorema bayes menjelaskan mengenai peluang suatu kejadian berdasarkan pengetahuan awal (prior) dari kondisi yang mungkin berhubungan dengan kejadian tersebut. 

Contohnya, jika penyakit diabetes berhubungan dengan umur, maka peluang seseorang terjangkit diabetes akan lebih akurat jika dimasukkan faktor umur di dalamnya. Secara matematis, teorema bayes dituliskan sebagai berikut.

$$
P(A|B) = \frac{P(B|A)}{P(B)}
$$


- P(A|B) = Peluang terjadinya A jika B terjadi
- P(B|A) = Peluang B terjadi saat A muncul
- P(A) = Peluang terjadinya A tanpa memandang kejadian apapun.
- P(B) = Peluang terjadinya B tanpa memandang kejadian apapun.

## Penerapan
Penerapan teorema bayes di bidang statistika salah satunya diterapkan pada pendugaan parameter. Kita bisa menggunakan metode Bayesian MCMC untuk melakukan pendugaan parameter selain metode popular lainnya seperti OLS dan MLE. Metode OLS dan MLE memandang parameter sebagai konstanta sehingga dia tidak memiliki distribusi, sedangkan Bayesian menganggap parameter sebagai peubah acak sehingga dia memiliki distribusi.

Selain itu, teorema bayes juga digunakan untuk melakukan klasifikasi objek. Metode ini sering dikenal sebagai Naive bayes Classifier. Dan kali ini akan dibahas penerapan teorema bayes untuk tujuan klasifikasi. Prinsip kerja metode ini adalah mengklasifikasikan objek berdasarkan peluang yang tertinggi diantara kelas lainnya.

## Reference
- https://arofiqimaulana.com/naive-bayes-classifier/
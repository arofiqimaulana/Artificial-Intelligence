# Ensemble Learning

## Definition
Ensemble learning bisa dibilang sebagai pembelajaran menggunakan sistem demokrasi. Hal ini karena hasil prediksi menggunakan voting dari beberapa metode. Secara arti, jika kita lihat pengertian ensemble adalah
a group of items viewed as a whole rather than individually.

Ensemble learning dengan konsep majority voting hanya bekerja (memberikan akurasi maksimum) jika dan hanya jika 
1. Setiap saling model saling independen, yang dilatih dengan himpunan data yang saling independen.
2. Masing-masing model memiliki akurasi leihh dari 50%

Teknik penggabungan sejumlah model ini dapat menggunakan
1. Bagging (random sampling with replacement)
2. Boosting (weighted based on accuray)
3. Random Forest (several decision tree)
4. Stacking

## Refference
- Suyanto. 2018. Machine Learning Tingkat Dasar dan Lanjut. Informatika. Bandung.
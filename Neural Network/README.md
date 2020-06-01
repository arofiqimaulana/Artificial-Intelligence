# Artificial Neural Network (ANN)
Neural network merupakan salah satu bagian dari algortima machine learning. Algoritma ini terinspirasi dari cara kerja otak manusia. 

### Konsep Dasar
Konsep dasar algoritma ini adalah
1. Input (seperti dendrit)
berfungsi sebagai input vector. Misalkan kita punya 500 gambar apel dan 500 gambar jeruk. Setiap gambar  akan diubah ke dalam bentuk angka (matriks). Angka inilah yang nantinya akan menjadi input.  

2. Penjumlahan Input (seperti Soma) 
berfungsi sebagai summation function. Sinyal positif dan negatif yang datang kepada soma berasal dari dendrit. Semua input seolah-olah seperti informasi yang diserap oleh otak, Dalam istilah matematis, angka-angka tersebut seperti dijumlah. 

Setiap input akan diberikan bobot yang berbeda-beda. Bobot adalah sebuah parameter yang akan dipelajari oleh sebuah perceptron.

Jika diibaratkan, **bobot** ~ **koefisien regresi** dan **bias ~ error** dalam analisis regresi.

3. Fungsi Aktivasi (seperti sinapsis) 
merupakan fungsi yang akan membuat percepteron bisa menyesuaikan pola non-linier. Fungsi ini bisa dianalogikan sebagai pemisah/hyperplane di SVM (seperti aturan setelah pattern yang ditemukan). 

Di dalam istilah statistik mirip dengan **Fungsi kepekatan peluang** (probability density function).

4. Output (seperti Axon)
hasil dari perhitungan sebuah perceptron yang merupakan bilangan numerik.

### Apa itu perceptron ? apa bedanya dengan Neural Network
perceptron adalah basic unit dari neural network. Perceptron hanya menggunakan 1 neuron saja, sedangkan Neural network menggunakan lebih dari satu node. Perceptron juga dikenal sebagai Singel Layer Perceptron, jadi **Perceptron = SLP**

Jika dibandingkan, Perceptron kurang lebih setara dengan analisis regresi berganda, regresi logistik, maupun SVM. 

### Mengapa bagian di Soma dilakukan operasi penambahan ?
Misal terdapat 5 informasi, maka setelah informasi pertama, maka kita tambahkan informasi kedua, dst. Hal ini juga karena dalam pemodelan regresi, kita biasa memodelkan dalam bentuk 
`
Y = a*X1+b*X2+c*X3 + error
`

### Multi Layer Perceptron (MLP)
adalah sebuah jaringan saraf yang terdiri dari satu atau lebih hidden layer (selain layer input dan layer output). MLP yang memiliki banyak hidden layer disebut juga deep neural network (DNN).

Lawan dari MLP adalah SLP (Single Layer Perceptron) atau perceptron.

### Mengapa perlu hidden layer ?
Kadangkala keputusan tidak bisa diambul secara 1 kali kondisi saja (butuh pattern yang bersarang). Mirip dengan IF bersarang. 

### Mengapa perlu Fungsi Aktivasi ?
Fungsi aktivasi seolah-olah adalah pattern yang sudah ditemukan untuk membedakan apakah ini A atau B (layaknya hyperplane di SVM). 

Fungsi Aktivasi ini mirip dengan Fungsi kepekatan peluang. Perlu diingat bahwa fungsi peluang untuk regresi logistik berbentuk sigmoid (woww... lihat kedekatannya).

### Mengapa ada banyak fungsi aktivasi ?
Terdapat beberapa fungsi aktivasi seperti sigmoid, ReLu, Leaky ReLu, MaxOut, ELU. Jika pattern sangat sederhana maka hyperlane akan seperti garis lurus (ingat SVM). Karena pattern tiap data berbeda, maka pemisah garis lurus tidak bisa lagi digunakan, sehingga butuh pemisah yang flexibel sesuai dengan pattern yang ditemukan. 

Salah satu cara pemilihan fungsi adalah bahwa ReLu tidak mengakomodir nilai negatif, sehingga hati-hati menggunakannya jika kita punya data bernilai negatif.

# Convolutional Neural Network (CNN)
Secara prinsip, algoritma ini meniru visual cortex pada mamalia. Algoritma ini seolah-olah **mengambil bagian** yang penting-penting saja, misal wajah manusia akan dibagi menjadi beberapa titik fokus seperti hidung, telinga, mata, dan bibir. Sedangkan bagian selain tersebut tidak diambil.

Pengenalan pola pada suatu gambar kadangkala bisa dilihat dengan mengamati beberapa bagian saja. Hal ini mengakibatkan ukuran matriks akan berkurang sehingga tidak semua input akan dihubungkan ke layer. Hal ini tentunya akan mengurangi komputasi sehingga perhitungan menjadi lebih cepat. Oleh karena itulah, CNN sering dipakai/cocok digunakan untuk kasus **Computer Vision**.

Salah satu perbedaan ANN dan CNN adalah pada CNN tidak semua input dipasangkan dengan layer. 

## Max Pooling
merupakan proses untuk **mengurangi resolusi gambar** dengan tetap mempertahankan informasi pada gambar (ibarat PCA).


# Recurrent Neural Network (RNN)
merupakan arsitektur deep learning yang populer serta sangat menjanjikan untuk menyelesaikan berbagai persolan yang terkait **NLP (Natural Language Processing)**. Intinya RNN digunakan agar mesin dapat memahami bahasa manusia meskipun sebenarnya dapat diimplementasikan untuk menenali gambar atau objek.


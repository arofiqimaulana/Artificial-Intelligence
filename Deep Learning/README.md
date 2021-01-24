# 1. Artificial Neural Network (ANN)
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
Terdapat beberapa fungsi aktivasi seperti sigmoid, ReLu, Leaky ReLu, MaxOut, dan ELU. Jika pattern sangat sederhana maka hyperlane akan seperti garis lurus (ingat SVM). Jika pattern sangat kompleks, maka pemisah garis lurus tidak mampu menjadi pembeda, sehingga butuh pemisah yang lebih flexibel sesuai dengan pattern yang ditemukan. 

Salah satu cara pemilihan fungsi adalah bahwa ReLu tidak mengakomodir nilai negatif, sehingga hati-hati menggunakannya jika kita punya data bernilai negatif.

# 2. Convolutional Neural Network (CNN)
Merupakan salah satu bentuk dari ANN dimana algoritma ini meniru visual cortex pada mamalia. Algoritma ini seolah-olah **mengambil bagian** yang penting-penting saja, misal wajah manusia akan dibagi menjadi beberapa titik fokus seperti hidung, telinga, mata, dan bibir. Sedangkan bagian selain tersebut tidak diambil.

Pengenalan pola pada suatu gambar kadangkala bisa dilihat dengan mengamati beberapa bagian saja. Hal ini mengakibatkan ukuran matriks akan berkurang sehingga tidak semua input akan dihubungkan ke layer. Hal ini tentunya akan mengurangi komputasi sehingga perhitungan menjadi lebih cepat. Oleh karena itulah, CNN sering dipakai/cocok digunakan untuk kasus **Computer Vision**.

Salah satu perbedaan ANN dan CNN adalah pada CNN tidak semua input dipasangkan dengan layer. 

## Convolutional Layer
merupakan layer dari hasil modifikasi filter. 

## Filter
merupakan suatu alat (berupa matriks) yang digunakan untuk melakukan modifikasi matriks awal. Matriks Filter ini akan dikalikan dengan sub-matriks pada matriks X sehingga akan menghasilkan suatu matriks baru yang berukuran lebih kecil. 

Misal dari suatu matriks X berukuran 5x5, jika digunakan filter berukuran 3x3 maka matriks X tersebut akan menjadi berukuran 4x4. 

## Max Pooling
merupakan proses untuk **mengurangi resolusi gambar** dengan tetap mempertahankan informasi pada gambar (ibarat PCA) dengan perhitungan maximum.

## Average Pooling
merupakan proses untuk **mengurangi resolusi gambar** dengan tetap mempertahankan informasi pada gambar (ibarat PCA) dengan perhitugan rata-rata.

## Ilustrasi CNN
Bayangkan memiliki bidang tanah (matriks 100x100) kita punya senter yang bisa menerangi 3x3 petak. Senter ini bertindak seperti **filter**. Mula-mula senter akan menyinari petak pojok atas, kemudian dikalikan dengan


# 3. Recurrent Neural Network (RNN)
merupakan arsitektur deep learning yang populer serta sangat menjanjikan untuk menyelesaikan berbagai persolan yang terkait **NLP (Natural Language Processing)**. Intinya RNN digunakan agar mesin dapat memahami bahasa manusia meskipun sebenarnya dapat diimplementasikan untuk menenali gambar atau objek.

# 4. Long Term Short Term Memory (LSTM)/GRU Networks
LSTM dan GRU (Gated Recurrernt Unit) merupakan building unit untuk layer-layer pada recurrent neural network (RNN). LTSM juga banyak diimplementasikan pada bidang NLP. Bisa dibilang bahwa LSTM dan GRU merupakan pengembangan dari RNN

# 5. Deep Belief Networks (DBN)
merupakan model deep learning yang memanfaatkan tumpukan/stack Restrcited Boltzmann Machines (RBM) atau kadangkala Autoencoders. Autoencoders adalah model neural network yang memiliki input dan output sama. Autoencoder mempelajari data input dan berusaha untuk melakukan rekonstruksi terhdapat data input tersebut.

DBN terdiri dari atas multiple layers dari latent variabeles (hidden units), dimana masing-masing RBM layers saling terhubung, namun node intra RB, layer tidak saling terhubung dengan node intra RBM lainnya.

DBN banyak diimplementasikan pada kasus-kasus yang memerlukan classification dan pengenalan image/gambar.

# 6. Deep Stacking Networks (DSN)
Salah satu masalah pada deep learning adalah proses learning sangat sulit dilakukan dan memerlukan komputasi yang cukup kompleks. Secara umum, model DSN terdiri dari sub-nets berukuran kecil dengan hanya sebuah hidden layer. 

# 7. Model Lain
Beberapa model lain yang cukup populer digunakan yaitu
1. RCNN (Region Based CNN)
2. GoogleNet
3. AlexNet
4. ResNet
5. ResNeXt
6. SegNet
7. GAN (Generative Adversarial Network)
8. SwueezeNet
9. YOLO (Yoo Only Look Once)

Penerapan Deep Learning pada dunia nyata sangat banyak, sebagian besar didominasi oleh pengenalan objek dan gambar (pengenalan mengenai image,face,object,medical image).

# CNN Flowchart
![](Convolutional%20Neural%20Network%20(CNN)/images/flowchart.png)




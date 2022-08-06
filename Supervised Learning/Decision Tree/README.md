# Decision Tree

## Pengertian	
Decision tree merupakan suatu struktur yang digunakan untuk membantu proses pengambilan keputusan. Disebut sebagai “tree” karena struktur ini menyerupai sebuah pohon lengkap dengan akar, batang, dan percabangannya.

Pada prinsipnya data akan dikelompokkan dalam representasi graph tree. Sehingga, pertama-tama dilakukan adalah menentukan variabel kriteria/atribut/feature untuk menjadi root node dan tree. Pemilihan feature/atribut tersebut menggunakan Entropy dan Information Gain

## Algoritma
Terdapat dua macam algoritma yang dapat digunakan untuk menyelesaikan permasalahan association rules.
1. ID3 <br>
Algoritma ini menggunakan Information gain dalam penentuan atribut pemilah terbaik (the best split attribute).
2. C4.5 <br>
Merupakan pengembangan dari algoritma ID3. Jika ID3 menggunakan Information gain, maka Algoritma C4.5 menggunakan Gain Ratio agar tidak bias dalam penentuan atribut pemilah terbaik (the best split attribute).
3. Algoritma Multivariate Splitting <br>
Algoritma ID3 maupun C4.5, melakukan pengecekan untuk satu per satu variabel pada setiap simpul (yang bukan simpul daun). Hal ini disebut dengan univariate splitting. Metode univariate splitting yang menghasilkan garis pemisah seperti tangga yang relatif kaku, kurang fleksibel, dan sangat rentan salah untuk sampel-sampel data baru yang terdistribusi relatif acak, tidak teratur, membentuk area seperti anak-anak tangga.

## Terms

### 1. Entropy 
adalah suatu parameter yang mengukur tingkat keberagaman (heterogentias) dari suatu kumpulan data. Semakin heterogen, nilai entropy akan semakin besar. Jika Entropy = 0, maka Subset tersebut secara terklasifikasi secara sempurna.Atau dapat dikatakan bahwa subset tersebut hanya dimiliki oleh sampel positive saja atau sampel negatif saja. Atau dapat dikatakan juga bahwa subset yang memiliki nilai Entropy = 0, dia tidak perlu di split.

Keadaan Entropy = 0 ini disebut dengan keadan pure set. Subset yang pure inilah yang akan menjadi patokan variabel apa
yang akan menjadi root node. 

Entropy ini bisa dihitung per variabel maupun per kategori....E(S)

Entropy akan dihitung tiap kelas di setiap variabel. Nantinya, Entropy ini akan dilakukan weighted average sehingga setiap variabel akan mempunyai 1 nilai entropy.... I(S)

### 2. Information Gain
Information gain mengukur seberapa banyak informasi suatu feature tentang kelasnya. adalah suatu ukuran seberapa efektif suatu atribut dalam mengklasifikasikan data. Secara matematis, Information Gain adalah selisih E(S) - I(S) atau bisa dikatakan Entropy Variabel dikurangi Average Weighted Entropy tiap kelas.

Information Gain yang paling tinggi akan dijadikan sebagai Root Node.


### Refference
1. https://scikit-learn.org/stable/modules/tree.html
2. https://www.datacamp.com/community/tutorials/decision-tree-classification-python
3. https://algorit.ma/blog/decision-tree-adalah-2022/
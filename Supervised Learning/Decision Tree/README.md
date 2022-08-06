# Decision Tree

## Pengertian	
Decision tree merupakan suatu struktur yang digunakan untuk membantu proses pengambilan keputusan. Disebut sebagai “tree” karena struktur ini menyerupai sebuah pohon lengkap dengan akar, batang, dan percabangannya.

Pada prinsipnya data akan dikelompokkan dalam representasi graph tree. Sehingga, pertama-tama dilakukan adalah menentukan variabel kriteria/atribut/feature untuk menjadi root node dan tree. Pemilihan feature/atribut tersebut menggunakan Entropy dan Information Gain

## Algoritma
Beberapa algoritma yang dapat digunakan adalah

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

### 3. Gain Ratio
merupakan perbandingan antara Gain dan split information. Gain ratio berfungsi untuk mengakomodasi perhitungan information gain yang kemungkinan menghasilkan bias. Bias ini bisa timbul jika banyaknya kategori = banyak observasi 

### 4. Split Info
Split info digunakan sebagai pembagi dari Gain(A) yang akan menghasilkan Gain Ratio.

### 5. Gain Ratio
Gain Ratio merupakan salah satu ukuran lain yang digunakan untuk mengatasi masalah pada atribut yang memiliki nilai sangat bervariasi.Gain Ratio tertinggi dipilih sebagai atribut test untuk simpul.

## Formula

#### 1. Entropy
$$ E(S) = -\sum_{i=1}^{c} p_i \log _{2} p_i $$
- c : banyak kelas
- pi : peluang untuk kelas ke i 

#### 2. Entropy pada masing-masing variabel
$$ E_A(S) = \sum_{v} \frac{|S_v|}{|S|}Entropy(S_v) $$ 

dimana
- A : variabel
- v : nilai yang mungkin untuk A
- |S_v|: jumlah sampel untuk nilai v
- |S| : Jumlah sampel untuk semua data
- Entropy(S_v): Entropy untuk sampel yang memiliki nilai v

#### 3. Information Gain
$$ Gain(A) = Entropy(S) - Entropy_A(S)$$

#### 4. Split Info
$$ \textrm{SplitInfo}_A(D)=\sum_{j=1}^{v} \frac{|D_j|}{|D|}.log _{2}(\frac{|D_j|}{|D|}) $$

#### 5. Gain Ratio
$$ \textrm{GainRatio}(A) = \frac{Gain(A)}{\textrm{SplitInfo}_A(D)} $$

## Refference
1. https://scikit-learn.org/stable/modules/tree.html
2. https://www.datacamp.com/community/tutorials/decision-tree-classification-python
3. https://algorit.ma/blog/decision-tree-adalah-2022/
4. https://muhammadilhammubarok.wordpress.com/2018/08/14/algoritma-c4-5/
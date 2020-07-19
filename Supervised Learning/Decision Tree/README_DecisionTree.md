### Konsep Decision Tree Learning
Pada prinsipnya data akan dikelompokkan dalam representasi graph tree. Sehingga, pertama-tama dilakukan adalah
menentukan variabel/kriteria/atribut/feature untuk menjadi root node dan tree. Pemilihan feature/atribut tersebut
menggunakan Entropy dan Information Gain

### Entropy 
adalah suatu parameter yang mengukur tingkat keberagaman (heterogentias) dari suatu kumpulan data. Semakin heterogen,
nilai entropy akan semakin besar. Jika Entropy = 0, maka Subset tersebut secara terklasifikasi secara sempurna.Atau dapat 
dikatakan bahwa subset tersebut hanya dimiliki oleh sampel positive saja atau sampel negatif saja. Atau dapat dikatakan
juga bahwa subset yang memiliki nilai Entropy = 0, dia tidak perlu di split.

Keadaan Entropy = 0 ini disebut dengan keadan pure set. Subset yang pure inilah yang akan menjadi patokan variabel apa
yang akan menjadi root node. 

Entropy ini bisa dihitung per variabel maupun per kategori....E(S)

Entropy akan dihitung tiap kelas di setiap variabel. Nantinya, Entropy ini akan dilakukan weighted average sehingga 
setiap variabel akan mempunyai 1 nilai entropy.... I(S)

### Information Gain
Information gain mengukur seberapa banyak informasi suatu feature tentang kelasnya.
adalah suatu ukuran seberapa efektif suatu atribut dalam mengklasifikasikan data. Secara matematis, Information Gain
adalah selisih E(S) - I(S) atau bisa dikatakan Entropy Variabel dikurangi Average Weighted Entropy tiap kelas.

Information Gain yang paling tinggi akan dijadikan sebagai Root Node.
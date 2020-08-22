###Konsep Dasar
Random Forest berkaitan erat dengan Decision Tree. Jika dibuat suatu analogi, suatu hutan (random forest) terbentuk dari pohon-pohon (decision tree). Sehingga Random Forest merupakan hasil dari banyak sekali decision tree. Dengan banyak sekali decision tree yang ada, maka hasil prediksi/clustering menggunakan teknik voting. Yang paling banyak suaranya, dia yang menang. Dengan teknik voting ini, tentunya hasil prediksi akan jauh lebih mendekati hasil yang sebenarnya.

Kata random merujuk pada pemilihan data yang secara random dan pemilihan variabel yang juga random. Pemilihan data secara random maksudnya adalah tiap decision tree yang terbentuk, subset data yang diambil berbeda-beda. Misalkan

decision tree ke-1 : row 1-row 150
decision tree ke-2 : row 50-row 190
decision tree ke-3 : row 40-row 175 . . .dst
Sedangkan pemilihan variabel secara random mengacu pada tiap decision tree berasal dari subset yang berbeda. Misal

decision tree ke-1 : [X1,X2,X3,X7,Y]
decision tree ke-2 : [X2,X3,X5,X6,Y]
decision tree ke-3 : [X1,X3,X4,X5,Y] . . . dst
Oleh karena itu, Random Forest dikenal sebagai **Ensemble Method** karena mengkombinasikan beberapa hasil prediksi dari beberapa model dengan tujuan meningkatkan hasil prediksi menjadi jauh lebih baik.
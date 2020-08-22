### ARTIFICIAL INTELLIGENCE (AI)
AI adalah simulasi dari kecerdasan manusia yang diproses atau disimulasikan oleh mesin atau sistem komputer. AI merupakan bagian dari ilmu computation science atau sAIns komputasi. AI juga dapat dikatakan merupakan pengembangan sistem komputer yang mampu mengerjakan tugas yang melibatkan proses berpikir, seperti reasoning, planning, learning, dan self-correction.

### Cabang AI
Berdasarkan cara kerja, teknologi AI biasa dibagi menjadi dua kategori, yaitu
1. **rule-based AI** <br/>
Rule-based AI bekerja berdasarkan aturan. Komputer mengandalkan “aturan–aturan” yang sudah ditetapkan atau diprogram oleh manusia untuk memetakan apa “hasil atau jawaban” yang dikeluarkan oleh komputer (atau bisa disebut output) apabila  ada informasi yang dimasukkan ke dalam sistem (bisa disebut input).

2. **Machine learning** <br/>
komputer tidak mengandalkan aturan–aturan yang diprogram oleh manusia, namun komputer mengolah data yang dimasukkan oleh manusia untuk mencari pola- pola tertentu yang muncul dalam data 
tersebut. Pola–pola inilah yang “dipelajari” oleh komputer dan menjadi acuan
saat sistem AI digunakan. 

Berdasarkan kegunaannya, AI dibagi menjadi 
1. Computer vision <br/>
adalah cabang teknologi AI yang memiliki fokus untuk mengolah gambar dari foto, video, atau langsung dari kamera. 

2. Natural Language Processing (NLP) <br/>
kemampuan meniru manusia dalam berbicara dan berbahasa (text sebagi input).

3. Speech Recognition <br/>
kemampuan meniru manusia dalam berbicara dan berbahasa (suara sebagai input). Contoh: Siri, Alexa, Google Assistant. 

4. Robotics <br/>
memiliki fokus untuk membangun mesin fisik untuk menjalankan berbagai fungsi yang sebelumnya membutuhkan keterampilan tangan manusia.

## Summary Code


1. Supervised Learning
Persiapan dataset untuk data train dan data test yaitu
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)
```
Beberapa Algoritma yang bisa digunakan
```
from sklearn.model_selection import StratifiedKFold, cross_val_score,GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
```
Build Model
```
model = LinearRegression()
model = LogisticRegression()
model = RandomForestClassifier()
```
Train Model
``` 
fit = model.fit(X_train,y_train)
predictions = model.predict(X_test)
```
Evaluasi Model
```
from sklearn.metrics import mean_squared_error
print ('RMSE: ', mean_squared_error(y_test, predictions))
akurasi=cross_val_score(model, Xtrain, y_train,cv=cv)
```


### Source
Skill Academy Cource (https://skillacademy.com/)

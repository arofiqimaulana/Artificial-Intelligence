#!/usr/bin/env python
# coding: utf-8

# ### PENGERTIAN
# Principal Component Analysis (PCA) merupakan teknik mereduksi suatu set variabel yang berdimensi tinggi 
# menjadi lebih rendah namun masih mengandung sebagian besar informasi dari data awal. Misalkan dari 100 
# variabel yang ada, kita hanya memakai 10 variabel saja untuk dianalisis (dimensi yang awalnya 100 menjadi 10 saja).
# 
# Terdapat dua fungsi utama dari PCA yaitu reduksi dan transformasi. Fungsi reduksi digunakan untuk 
# mengurangi jumlah variabel (yang awalnya sangat banyak) menjadi lebih sedikit sehingga memudahkan 
# analisis pada tahap selanjutnya. Sedangkan fungsi transformasi digunakan untuk mengubah variabel 
# yang awalnya saling berkorelasi menjadi tidak saling berkorelasi.

# ### ISTILAH PENTING
# Berikut merupakan istilah – istilah penting di PCA
# 
# 1. Communality
# 2. Eigenvalue
# 3. Sphericity test
# 4. Factor
# 5. Factor Loading
# 6. Factor Matrix
# 7. Factor Score
# 8. PC Score
# 9. Factor Analysis vs PCA
# 10. Rotasi Matrix

# ### Berikut merupakan tahapan-tahapan dalam melakukan PCA 
# - Step 1: Standarisasi data
# - Step 2: Menghitung matrik covariance/korelasi
# - Step 3: Menghitung nilai eigen
# - Step 4: Menghitung PC .
# - Step 5: Reduksi Dimensi

# ## IMPORT DATA

# data yang digunakan dalam contoh ini adalah data iris.

# In[114]:


## Import Package
import pandas as pd
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression 


# In[2]:


## Load data iris
iris = datasets.load_iris()


# In[10]:


X = iris['data'] 


# In[11]:


y = iris['target']


# In[32]:


## Mengubah format data iris dari array ke dataframe


# In[29]:


iris.feature_names


# In[25]:


df_X = pd.DataFrame(X)


# In[60]:


df_X.columns =  iris.feature_names ## Assign nama kolom


# In[27]:


df_X.head()


# In[33]:


df_y = pd.DataFrame(y)


# In[38]:


df_y.columns = ['target']


# In[39]:


df_y.head()


# ## Standardize

# In[41]:


X_Scale = StandardScaler().fit_transform(df_X)


# In[46]:


dfX_Scale = pd.DataFrame(X_Scale,columns=iris.feature_names )


# In[47]:


dfX_Scale


# ## PCA

# In[52]:


### Misal kita pilih n = k
pca = PCA(n_components = 4) 


# In[56]:


### Variabel PC
principalComponents = pca.fit_transform(dfX_Scale)


# In[57]:


principalComponents_Df = pd.DataFrame(principalComponents,columns=['PC1','PC2','PC3','PC4'])


# In[58]:


principalComponents_Df.head()


# In[ ]:





# ## Eigen Value & Eigen Vector

# In[64]:


### Nilai Eigen
pca.explained_variance_


# In[67]:


### Berapa persen suatu PC mampu menjelaskan keragaman data
pca.explained_variance_ratio_


# In[ ]:





# ## Pemilihan Banyaknya Dimensi

# 1. Penentuan banyaknya dimensi yang akan diambil bisa berdasarkan nilai eigen atau nilai variance komulatif
# 2. Menurut Dillon & Goldstein (1984), PC yang Nilai eigen yang lebih dari 1 yang akan diambil 
# 3. Menurut (Marison,1976) PC yang nilai komulatif variance yang lebih dari 75%

# Berdasarkan kriteria di atas, banyaknya dimensi yang bisa dibentk bisa 1 (jika pakai eigenvalue) atau 2 (jika pakai komulaitif variance explained)

# Kita akan ambil 2 dimensi saja

# ## Penerapan PCA sebagai Explorasi

# PCA dapat digunakan sebagai explorasi data. Karena princip PCA adalah membentuk variabel baru dari dimensi yang tinggi menjadi dimensi rendah, maka kita bisa melihat pattern berdasarkan variabel baru (variabel PC). Kita buat plot saja antara variabel tersebut. Visualisasi paling mudah adalah visualisasi 2 Dimensi.

# In[76]:


### kita pilih banyak dimensi = 2
pca = PCA(n_components = 2) 


# In[77]:


PC = pca.fit_transform(X_Scale)


# In[83]:


df_PC = pd.DataFrame(PC,columns=['PC1','PC2'])


# In[84]:


df_PC.head()


# In[85]:


df_y.head()


# In[90]:


def Encoding(x):
    label = []
    if x == 0:
        label = 'setosa'
    elif x == 1:
        label = 'versicolor'
    elif x == 2:
        label = 'virginica'
    return label


# In[107]:


df_y['label'] = df_y['target'].apply(Encoding)


# In[108]:


DF = pd.concat([df_PC,df_y],axis=1,ignore_index=True)


# In[109]:


DF.columns = ['PC1','PC2','target','label']


# In[110]:


DF.head()


# In[113]:


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
sns.scatterplot(DF.PC1,DF.PC2,hue=DF.label)
plt.show()


# Berdasarkan visualisasi PC1 dan PC2, terlihat bahwa objek mempunyai karakteristik yang mirip akan mengelompok. Variabel PC1 dan PC2 ini bisa digunakan untuk mengidentifikasi objek baru masuk kategori yang mana.

# In[ ]:





# ## Penerapan PCA sebagai transformasi

# PCA dapat digunakan sebagai alat untuk mengatasi masalah multikolinieritas. Berbeda dengan  Sebaiknya, variabel yang digunakan semuanya agar informasi yang ada tidak hilang banyak. Model ini sering disebut dengan RIDGE REGRESSION

# Penggunaannya cukup mudah yaitu, variabel X diganti dengan variabel PC. Lalu lajutkan ke analisis selanjutnya. Misal
# - model lama => Y = X1 + X2 + X3 + X4
# - model baru => Y = PC1 + PC2 + PC3 + PC4

# In[115]:


classifier = LogisticRegression(random_state = 0)


# In[119]:


classifier.fit(df_PC,df_y['target'])


# In[121]:


## Model Regresi Logistik
classifier.coef_


# In[ ]:





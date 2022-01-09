library(class)
library(caTools)

# import data
df_iris = iris
set.seed(123)

# Split dataset into training and testing data
df_iris$status = sample.split(df_iris,SplitRatio = 0.80)

df_train = subset(df_iris,status==TRUE) # label TRUE = data train
df_test = subset(df_iris,status==FALSE) # label FALSE = data test

kolom_X = c('Sepal.Length','Sepal.Width','Petal.Length','Petal.Width')
kolom_y = c('Species')

X_train = df_train[kolom_X]
y_train = df_train[kolom_y]
X_test = df_test[kolom_X]
y_test = df_test[kolom_y]


# k-Nearest Neighbor
knn_result <- knn(train = X_train,test = X_test,cl=y_train$Species,k = 3,prob = TRUE)

# Evaluasi Model
head(cbind(y_test,knn_result)) # real vs prediksi

conf_matrix <- table(y_test$Species,knn_result) # Confusion Matrix
accuracy <- sum(diag(conf_matrix))/sum(conf_matrix) # Akurasi Model

accuracy
library(factoextra)
library(ggplot2)

df <- mtcars
df <- scale(df)

km <- kmeans(df, centers = 4, nstart = 25)
fviz_cluster(km, data = df)

cc = cbind(km$cluster)

knitr::include_graphics("ProsedurPengklasteran.PNG")

! [Alt text] (ProsedurPengklasteran.PNG) 

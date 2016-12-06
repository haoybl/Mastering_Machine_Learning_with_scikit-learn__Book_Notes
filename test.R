wine <- read.csv("/Users/AdamLiu/Git/Machine_Learning/Learning/Mastering_Machine_Learning_with_scikit-learn/winequality-red.csv", sep = ";")

density(hist(wine$quality))
summary(wine)

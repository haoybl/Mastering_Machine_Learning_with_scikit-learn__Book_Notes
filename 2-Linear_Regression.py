
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split

df = pd.read_csv('wine/winequality-red.csv', sep=';')
X = df[list(df.columns)[:-1]]
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_predictions = regressor.predict(X_test)
print ('R-squared:', regressor.score(X_test, y_test))



# ===================================



# import matplotlib.pylab as plt
# import pandas as pd

# df = pd.read_csv("winequality-red.csv", sep = ";")
# print(df.describe())

# plt.scatter(df['alcohol'], df['quality'])
# plt.xlabel('Alcohol')
# plt.ylabel('Quality')
# plt.title('Alcohol Against Quality')
# plt.show()



# ===================================



# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures


# X_train = [[6], [8], [10], [14],   [18]]
# y_train = [[7], [9], [13], [17.5], [18]]

# X_test = [[6],  [8],   [11], [16]]
# y_test = [[8], [12], [15], [18]]

# regressor = LinearRegression()
# regressor.fit(X_train, y_train)

# xx = np.linspace(0, 26, 100)
# yy = regressor.predict(xx.reshape(xx.shape[0], 1))

# plt.plot(xx, yy)

# quadratic_featurizer = PolynomialFeatures(degree=2)
# X_train_quadratic = quadratic_featurizer.fit_transform(X_train)
# X_test_quadratic = quadratic_featurizer.transform(X_test)

# regressor_quadratic = LinearRegression()
# regressor_quadratic.fit(X_train_quadratic, y_train)
# xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))

# plt.plot(xx, regressor_quadratic.predict(xx_quadratic), c='r', linestyle='--')
# plt.title('Pizza price regressed on diameter')
# plt.xlabel('Diameter in inches')
# plt.ylabel('Price in dollars')
# plt.axis([0, 25, 0, 25])
# plt.grid(True)
# plt.scatter(X_train, y_train)
# plt.show()

# print (X_train)
# print (X_train_quadratic)
# print (X_test)
# print (X_test_quadratic)
# print ('Simple linear regression r-squared', regressor.score(X_test, y_test))
# print ('Quadratic regression r-squared', regressor_quadratic.score(X_test_quadratic, y_test))
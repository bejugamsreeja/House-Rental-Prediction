#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sklearn.datasets import make_regression
X,Y = make_regression(n_features=2, noise=10, n_samples=1000)

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.xlabel('Feature - X')
plt.ylabel('Target - Y')
plt.scatter(X,Y,s=5)

Y.shape

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X[:-5],Y[:-5])

lr.coef_

lr.intercept_

lr.predict(X[-5:])

X[:5]

Y[-5:]

import pandas as pd

house_data = pd.read_csv('https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/house_rental_data.csv.txt', index_col='Unnamed: 0')

house_data.rename(columns={'Living.Room':'Livingroom'}, inplace=True)

house_data.head()

columns = house_data.columns.tolist()
columns.remove('Price')
feature_data = house_data[columns]
target_data = house_data.Price
from sklearn.model_selection import train_test_split
trainX,testX, trainY,testY = train_test_split(feature_data, target_data)
trainX.shape
testX.shape
lr = LinearRegression(normalize=True)
lr.fit(trainX,trainY)
lr.coef_
testX[:5]
testY[:5]
lr.predict(testX[:5])
from sklearn.metrics import mean_squared_error, mean_absolute_error
pred = lr.predict(testX)
mean_absolute_error(y_pred=pred, y_true=testY)
from sklearn.linear_model import Ridge,Lasso

ridge = Ridge(alpha=1000)
lasso = Lasso(alpha=1000)

ridge.fit(trainX,trainY)
lasso.fit(trainX,trainY)

pred = ridge.predict(testX)
pred = lasso.predict(testX)

mean_absolute_error(y_pred=pred, y_true=testY)

from sklearn.datasets import load_iris
iris = load_iris()
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(iris.data, iris.target)
logreg.predict_proba(iris.data[:1])
iris.target[:1]
logreg.score(iris.data, iris.target)
from sklearn.preprocessing import PolynomialFeatures
pol = PolynomialFeatures(degree=2)
pol.fit_transform([[1,2],[3,4]])


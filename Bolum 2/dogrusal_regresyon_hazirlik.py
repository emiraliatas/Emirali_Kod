#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('satislar.csv')
#pd.read_csv("veriler.csv")
#test
print(veriler)

aylar = veriler.iloc[:,[0]]
satislar = veriler.iloc[:,[1]]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(aylar,satislar,test_size=0.33,random_state=0)

"""
#Scaling islemi (Standard sapma)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.transform(y_test)
"""

#Model insası (linear regression)
from sklearn.linear_model import LinearRegression
lr=LinearRegression()

lr.fit(x_train,y_train)

tahmin_y_test = lr.predict(x_test)
#tahmin_ytest_original = sc.inverse_transform(tahmin_y_test)

x_train = x_train.sort_index()
y_train = y_train.sort_index()
x_test = x_test.sort_index()
y_test = y_test.sort_index()

plt.scatter(x_test,y_test, color="blue", label="Gerçek Satışlar")
plt.plot(x_test,lr.predict(x_test), color="orange", label="Model Tahmini")

plt.title("Aylara göre satış")
plt.legend()
plt.xlabel("Ay")
plt.ylabel("Satis")



















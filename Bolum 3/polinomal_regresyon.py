# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



#veri yükleme
veriler = pd.read_csv('maaslar.csv')





#dataframe slicing
egitim = veriler.iloc[:,[1]]
maas = veriler.iloc[:,[2]]



#dataframe to --> numpy array
EGİTİM = egitim.values
MAAS = maas.values




#linear regression, dogrusal model olusturma
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(egitim,maas)




#polynomial regression, non-linear model
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)

egitim_poly = poly_reg.fit_transform(EGİTİM)

lin_reg2 = LinearRegression()
lin_reg2.fit(egitim_poly, MAAS)





#Plotting
plt.scatter(egitim,maas)
plt.plot(egitim,lin_reg.predict(egitim))
plt.show()


plt.scatter(egitim, maas, color="red")
plt.plot(EGİTİM, lin_reg2.predict(egitim_poly), color="blue")
plt.show()









#tahminler
print(lin_reg.predict([[11]]))
print(lin_reg.predict([[6.6]]))

print(lin_reg2.predict(poly_reg.fit_transform([[11]])))
print(lin_reg2.predict(poly_reg.fit_transform([[6.6]])))









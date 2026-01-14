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




"""
#Plotting
plt.scatter(egitim,maas)
plt.plot(egitim,lin_reg.predict(egitim))
plt.show()
"""
"""
plt.scatter(egitim, maas, color="red")
plt.plot(EGİTİM, lin_reg2.predict(egitim_poly), color="blue")
plt.show()
"""
#verilerin ölceklenmesi (SVR ICIN COK ONEMLİ!!)
sc1 = StandardScaler()
egitim_scaled = sc1.fit_transform(EGİTİM)
sc2 = StandardScaler()
maas_scaled = sc2.fit_transform(MAAS)



#svr model creating
from sklearn.svm import SVR
svr_reg = SVR(kernel = "rbf")
svr_reg.fit(egitim_scaled, maas_scaled)

"""
plt.scatter(egitim_scaled, maas_scaled)
plt.plot(egitim_scaled, svr_reg.predict(egitim_scaled))
plt.show()
"""



#decision tree model
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(random_state = 0)
dt_reg.fit(EGİTİM, MAAS)

plt.scatter(EGİTİM, MAAS, color="red")
plt.plot(EGİTİM, dt_reg.predict(EGİTİM), color="blue")
plt.show()

print(dt_reg.predict([[11]]))
print(dt_reg.predict([[6.6]]))



#random forest model
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=10,random_state=0)
rf_reg.fit(EGİTİM, MAAS.ravel())

plt.scatter(EGİTİM, MAAS, color="red")
plt.plot(EGİTİM, rf_reg.predict(EGİTİM), color="blue")

plt.show()
print(rf_reg.predict([[6.6]]))







#r2 score calculating
from sklearn.metrics import r2_score

print("-------------------------------------------")
print("Random Forest R2 Score")
print(r2_score(MAAS, rf_reg.predict(EGİTİM)))

print("Decision Tree R2 Score")
print(r2_score(MAAS, dt_reg.predict(EGİTİM)))

print("SVR R2 Score")
print(r2_score(maas_scaled, svr_reg.predict(egitim_scaled)))

print("Polynomial Reg. R2 Score")
print(r2_score(MAAS, lin_reg2.predict(egitim_poly)))

print("Linear Reg. R2 Score")
print(r2_score(maas, lin_reg.predict(egitim)))















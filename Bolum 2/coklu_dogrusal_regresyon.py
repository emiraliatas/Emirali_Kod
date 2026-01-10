# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")
#test
print(veriler)

#encoder: Kategorik -> Numeric
ulke = veriler.iloc[:,0:1].values
print(ulke)



le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])

print(ulke)


ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

#encoder: Kategorik -> Numeric
c = veriler.iloc[:,-1:].values
print(c)


le = preprocessing.LabelEncoder()

c[:,-1] = le.fit_transform(veriler.iloc[:,-1])

print(c)


ohe = preprocessing.OneHotEncoder()
c = ohe.fit_transform(c).toarray()
print(c)



#numpy dizileri dataframe donusumu
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc)

Yas = veriler.iloc[:,1:4].values
sonuc2 = pd.DataFrame(data=Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = c[:,:1], index = range(22), columns = ['cinsiyet'])
print(sonuc3)



#dataframe birlestirme islemi
s=pd.concat([sonuc,sonuc2], axis=1)
print(s)

sonuc_final=pd.concat([s,sonuc3], axis=1)
print(sonuc_final)

#verilerin egitim ve test icin bolunmesi


x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

sc=StandardScaler()


y_pred = regressor.predict(x_test)


boy = sonuc_final.iloc[:,3:4]

sol = sonuc_final.iloc[:,:3]
sag = sonuc_final.iloc[:,4:]

bagımsız_degiskenler = pd.concat([sol,sag], axis=1)

x_train, x_test,y_train,y_test = train_test_split(bagımsız_degiskenler,boy,test_size=0.33, random_state=0)
regressor.fit(x_train,y_train)

boy_pred = regressor.predict(x_test)



import statsmodels.api as sm

X = np.append(arr = np.ones((22,1)).astype(int), values=bagımsız_degiskenler,axis=1)

X_liste = bagımsız_degiskenler.iloc[:,[0,1,2,3,5]].values
X_liste = np.array(X_liste,dtype=float)

model = sm.OLS(boy,X_liste).fit()
print(model.summary())

x_train,x_test,y_train,y_test = train_test_split(X_liste,boy,test_size=0.33,random_state=0)
regressor.fit(x_train,y_train)

boy_pred_final = regressor.predict(x_test)














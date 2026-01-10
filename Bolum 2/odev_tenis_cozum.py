# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

veriler = pd.read_csv("odev_tenis.csv")

outlook = veriler.iloc[:,[0]]
temp = veriler.iloc[:,1].values
hum = veriler.iloc[:,2].values
windy = veriler.iloc[:,3:4]
play = veriler.iloc[:,4:]



#encoding categorical data
#encoding for outlook
outlook_array=np.array(outlook)
musaitlik_sirasi = ["rainy","overcast","sunny"]
oenc = preprocessing.OrdinalEncoder(categories=[musaitlik_sirasi])
result_outlook = oenc.fit_transform(outlook_array)


#encoding for windy
le = preprocessing.LabelEncoder()
result_windy = le.fit_transform(windy)

#encoding for play
result_play = le.fit_transform(play)


#concatinating in a dataframe
bagımsız_degiskenler = pd.DataFrame({
    "Outlook": result_outlook.ravel(), 
    "Temperature": temp, 
    "Humidity": hum,
    "Windy": result_windy.ravel()
    })

bagımlı_degisken = pd.DataFrame({"Play": result_play.ravel()})



#setting test and train data
x_train, x_test, y_train, y_test, = train_test_split(bagımsız_degiskenler, bagımlı_degisken, test_size = 0.33, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

play_pred = regressor.predict(x_test)


import statsmodels.api as sm
X = np.append(arr = np.ones((14,1)).astype(int), values=bagımsız_degiskenler,axis=1)

X_liste = bagımsız_degiskenler.iloc[:,[1]].values
X_liste = np.array(X_liste,dtype=float)

model = sm.OLS(bagımlı_degisken,X_liste).fit()
print(model.summary())


x_train,x_test,y_train,y_test = train_test_split(X_liste,bagımlı_degisken,test_size=0.33,random_state=0)
regressor.fit(x_train,y_train)

play_pred_final = regressor.predict(x_test)














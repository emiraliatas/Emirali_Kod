import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures




veriler = pd.read_csv("maaslar_odev2.csv")


#dataframe slicing
x = veriler.iloc[:,2:5]
y = veriler.iloc[:,-1:]

y_array = y.values


#gerekli - gereksiz degiskenler
X = np.append(arr = np.ones((30,1)).astype(int), values=x,axis=1)

X_liste = x.iloc[:,[0,2]].values
X_liste = np.array(X_liste, dtype=float)

model = sm.OLS(y_array,X_liste).fit()
print(model.summary())


x_array = x.values







#train_test_split 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=0)





#linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x_train,y_train)

print("Linear Regression R2 Score")
print(r2_score(y_test,lin_reg.predict(x_test)))



#polynomial regression
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(x_array)
#train_test_split for polynomial
x_polytrain,x_polytest,y_polytrain,y_polytest = train_test_split(x_poly,y,test_size=0.33,random_state=0)


lin_reg2 = LinearRegression()
lin_reg2.fit(x_polytrain,y_polytrain)

print("Polynomial Regression R2 Score")
print(r2_score(y_polytest,lin_reg2.predict(x_polytest)))


#decision tree model
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor()
dt_reg.fit(x_train,y_train)

print("Decision Tree R2 Score")
print(r2_score(y_test,dt_reg.predict(x_test)))


#scaling for svr model
sc1 = StandardScaler()
x_scaled = sc1.fit_transform(x)
sc2 = StandardScaler()
y_scaled = sc2.fit_transform(y)


#train_test_split for scaled df
x_scaledtrain,x_scaledtest,y_scaledtrain,y_scaledtest = train_test_split(x_scaled,y_scaled,test_size=0.33,random_state=0)

#svr model
from sklearn.svm import SVR
svr_reg = SVR(kernel="rbf")
svr_reg.fit(x_scaledtrain,y_scaledtrain)

print("SVR R2 Score")
print(r2_score(y_scaledtest, svr_reg.predict(x_scaledtest)))



#random forest model
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor()
rf_reg.fit(x_train,y_train)

print("Random Forest R2 Score")
print(r2_score(y_test,rf_reg.predict(x_test)))


ceo_test = pd.DataFrame({"UnvanSeviyesi": 10, "Kidem": 10, "Puan": 100}, index=[30])
mudur_test = pd.DataFrame({"UnvanSeviyesi": 7, "Kidem": 10, "Puan": 100}, index = [31])



#worst to better predict
print("Polynomial Predict for CEO and Boss")
print(lin_reg2.predict(poly_reg.transform(ceo_test)))
print(lin_reg2.predict(poly_reg.transform(mudur_test)))
print("Linear Regression Predict for CEO and Boss")
print(lin_reg.predict(ceo_test))
print(lin_reg.predict(mudur_test))
print("Decision Tree Predict")
print(dt_reg.predict(ceo_test))
print(dt_reg.predict(mudur_test))
print("SVR Precict")
ceo_test_scld = sc1.transform(ceo_test)
mudur_test_scld = sc1.transform(mudur_test)
print(sc2.inverse_transform([svr_reg.predict(ceo_test_scld)]))
print(sc2.inverse_transform([svr_reg.predict(mudur_test_scld)]))

print("Random Forest Predict")
print(rf_reg.predict(ceo_test))
print(rf_reg.predict(mudur_test))







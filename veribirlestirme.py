import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing

veriler = pd.read_csv('eksikveriler.csv',)
print(veriler)
print("\n")

#ulke degerlerini tek sutun olarak alma
ulke = veriler.iloc[:,0:1].values
print(ulke)
print("\n")

#eksik veriler
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
yas = veriler.iloc[:,1:4].values
print(yas)
print("\n")

imputer = imputer.fit(yas[:,1:4])#ogrenme
yas[:,1:4] = imputer.transform(yas[:,1:4]) #verileri doldurma
print(yas)

#---------------------------------------------------
#ulkeleri 0 1 2  degerleriyle numaralandirmak
le = preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

#0 1 2 degerleri icin birer sutun olusturuldu
#her sutun icin ulke degerlerine gore 0 ve 1 kutupları kullanildi 
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

#ulke sutunu kendi icinde olusturuldu
sonuc = pd.DataFrame(data = ulke,index = range(22),columns = ['fr','tr','us'])
print(sonuc)

#boy kilo yas kendi icinde ayirildi ulke degeri lazim olmadigi icin boyle yaptik
sonuc2 = pd.DataFrame(data = yas, index = range(22) ,columns = ['boy','kilo','yas'])
print(sonuc2)


cinsiyet = veriler.iloc[:,-1]
sonuc3 = pd.DataFrame(data = cinsiyet,index = range(22),columns = ['cinsiyet'])
print(sonuc3)

#ilk basta ulke ile boy kilo yas sutunlarini birlestirdik
s = pd.concat([sonuc,sonuc2],axis = 1)
print(s)

#sonra bu birlesimi cinsiyet kismi ile birlestirdik
s2 = pd.concat([s,sonuc3],axis = 1)
print(s2) 


from sklearn.model_selection import train_test_split

#x bagımsız degisken, y bagımlı degisken. train-test ikililerindeki kisiler aynı, bir x-y ikilisiyle train diger x-y ikilisiyle test yapiyoruz
x_train, x_test, y_train, y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)


























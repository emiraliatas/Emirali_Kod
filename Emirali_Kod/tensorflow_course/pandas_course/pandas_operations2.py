import numpy as np
import pandas as pd

# dict1 = {"Isim": ["Ahmet","Deniz","Yusuf","Eysan"],
#          "Spor": ["Kosu","Yüzme","Kosu","Basketbol"],
#          "Kalori": [100,200,300,400]}
# dataframe1 = pd.DataFrame(dict1, index=[1,2,3,4])


# dict2 = {"Isim": ["Fatma", "Ayse", "Nur","Omer"],
#          "Spor": ["Yüzme","Basketbol","Kosu","Yüzme"],
#          "Kalori": [200,300,400,500]}
# dataframe2 = pd.DataFrame(dict2,index=[5,6,7,8])

# dict3 = {"Isim": ["Osman","Naz","Sadik","Beril"],
#          "Spor": ["Kosu","Basketbol","Yüzme","Basketbol"],
#          "Kalori": [150,200,300,400]}
# dataframe3 = pd.DataFrame(dict3,index=[9,10,11,12])

# concat_dataframe = pd.concat([dataframe1,dataframe2,dataframe3])
# print(concat_dataframe)

# merge_dict1 = {"Isim": ["Ahmet", "Mehmet", "Emir"],
#                "Spor": ["Kosu","Basket","Futbol"]}
# merge_dataframe1 = pd.DataFrame(merge_dict1)
# print(merge_dataframe1)
# merge_dict2 = {"Isim": ["Ahmet", "Mehmet", "Emir"],
#                "Kalori": [100,300,200]}
# merge_dataframe2 = pd.DataFrame(merge_dict2)
# print(merge_dataframe2)

# merged_dataframe = pd.merge(merge_dataframe1,merge_dataframe2,on="Isim")
# print(merged_dataframe)


# maas_dict = {"Name": ["Emir","Ekim","Doga","Salih"],
#              "Department": ["Yazilim","Satis","Pazarlama","Yazilim"],
#              "Maas": [200,300,400,500]}

# maas_dataframe = pd.DataFrame(maas_dict)
# print(maas_dataframe)
# print(maas_dataframe["Department"].value_counts())

# def brut_to_net(maas):
#     return maas * 0.66

# new_maas = maas_dataframe["Maas"].apply(brut_to_net)
# print(new_maas)


new_data = {"Karakter Sinifi": ["South Park","South Park","Simpsons","Simpsons","Simpsons"],
            "Karakter Ismi": ["Cartman","Kenny","Homer","Bart","Bart"],
            "Karakter Puani": [10,20,30,40,10]}

characterDF = pd.DataFrame(new_data)
print(characterDF)
pivot_characterDF = characterDF.pivot_table(values = "Karakter Puani", index = ["Karakter Sinifi","Karakter Ismi"],aggfunc=np.sum)
print(pivot_characterDF)
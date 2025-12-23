import numpy as np
import pandas as pd


maas_sozluk = {"Departman": ["Yazilim", "Yazilim", "Finans", "Finans", "Hukuk", "Hukuk"],
               "Isim": ["Ahmet","Emir","Cemre","Fatma","Berat","Mehmet"],
               "Maas": [100,150,200,220,180,215]}

maas_dataframe = pd.DataFrame(maas_sozluk)
print(maas_dataframe)

group_object = maas_dataframe.groupby("Departman")
print(group_object.min())
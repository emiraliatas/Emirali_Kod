import pandas as pd
import numpy as np

dict_data = {"Istanbul": [30,29,np.nan], "Ankara": [20,np.nan,22], "Izmir": [40,39,38]}
weather_dataframe = pd.DataFrame(dict_data, index=["Pazartesi","Sali","Carsamba"])

print(weather_dataframe)


new_data = {"Istanbul": [30,29,np.nan], "Ankara": [20,np.nan,22], "Izmir": [40,39,38], "Antalya":[45,np.nan,np.nan]}
new_dataframe = pd.DataFrame(new_data, index=["Pazartesi","Sali","Carsamba"])
print(new_dataframe)
clean_dataframe = new_dataframe.dropna(axis=1,thresh=2)
print(clean_dataframe)
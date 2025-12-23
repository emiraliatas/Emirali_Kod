import numpy as np
import pandas as pd

# series
# my_dict = {"Emir": 18, "Zeynep": 40, "Mehmet": 30}
# my_series = pd.Series(my_dict)
# print(my_series)

my_ages = [18,40,30]
my_names = ["Emir", "Zeynep", "Mehmet"]
new_series = pd.Series(index=my_names, data=my_ages)
print(new_series)

race_result1 = pd.Series([40,30,20], ["Emir","Ali","Mehmet"])
print(race_result1)
race_result2 = pd.Series([50,45,35], ["Emir", "Mahmut", "Ali"])
print(race_result2)
print(race_result1 + race_result2) 

race2 = pd.Series(data=["Emir", "Ali", "Mehmet"], index=["Birinci", "İkinci", "Ücüncü"])
print(race2)
import pandas as pd
import numpy as np

# data = np.random.randn(4,3)
# print(data)

# data_frame = pd.DataFrame(data)
# print(data_frame[0])

# new_data_frame = pd.DataFrame(data,index=["Emir", "Ali", "Mehmet", "Kaan"],columns=["Maas", "Yas", "Mesai"])
# print(new_data_frame)
# print(new_data_frame.iloc[0])

# new_data_frame["Tecrube"] = [1,2,3,4]
# print(new_data_frame)

# dropped_dataframe = new_data_frame.drop("Tecrube", axis=1, inplace=True)
# print(dropped_dataframe)
# print(new_data_frame)

# print(new_data_frame.reset_index())
# new_index_list = ["Emi", "Ali", "Meh", "Kaa"]
# new_data_frame["Yeni Index"] = new_index_list
# print(new_data_frame.set_index("Yeni Index"))   

first_indexes = ["HxH", "HxH", "HxH", "FMAB", "FMAB", "FMAB"]
second_indexes = ["Gon", "Killua", "Kurapika", "Edward", "Alphonse", "Father"]

united_indexes = list(zip(first_indexes, second_indexes))
print(united_indexes)
united_indexes = pd.MultiIndex.from_tuples(united_indexes)
my_anime_list = [[9,"A"],[10,"B"],[15,"C"],[20,"D"],[18,"E"],[400,"F"]]
anime_data_frame = pd.DataFrame(my_anime_list,index=united_indexes,columns=["Yas","Meslek"])
print(anime_data_frame.loc["FMAB"].loc["Edward"])
anime_data_frame.index.names = ["Series Name", "Name"]
print(anime_data_frame)
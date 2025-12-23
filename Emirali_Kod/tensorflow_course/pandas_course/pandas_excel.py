import pandas as pd
import numpy as np

maas_excel = pd.read_excel("maas.xlsx")
print(maas_excel)
yeni_dataframe = maas_excel.dropna()

yeni_dataframe.to_excel("yenimaas.xlsx")
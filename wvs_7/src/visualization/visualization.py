import pandas as pd


vn=pd.read_csv("../../data/processed/VNM.csv")
for i, col in enumerate(vn.columns[:40]):
    print(col)

vn["N_TOWN"].value_counts().plot(kind='barh')
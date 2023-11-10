import pandas as pd
df = pd.read_csv("data/raw/WVS_Cross-National_Wave_7_csv_v5_0.csv")
# filter to country
country_list=df.B_COUNTRY_ALPHA.unique().tolist()
for country in country_list:
    print(country)
    country_df=df.query("B_COUNTRY_ALPHA==@country")
    country_df.to_csv(f"data/processed/{country}.csv")
    

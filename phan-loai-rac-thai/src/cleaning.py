import pandas as pd
df=pd.read_csv("../data/raw/PLRT.csv")

# rename column & create ques_dict
df.rename(columns={"Timestamp":'0. timestamp'}, inplace=True)
# df.columns=df.columns.str.replace("vi.", 'vi').str.split(".").str[1].str.strip()
    # I can use this to create clean ques_dict w/o enumeration of Nhat Phuong if I want. 
categ_vars=df.columns[:8]
yeu_to_khach_quan=df.columns[8:21]
tam_ly_ca_nhan=df.columns[21:]

ques_dict={}
for index, var in enumerate(categ_vars):
    ques_dict.update({f"cat{index}":var})
for index, var in enumerate(yeu_to_khach_quan):
    ques_dict.update({f"kq{index}":var})
for index, var in enumerate(tam_ly_ca_nhan):
    ques_dict.update({f"psy{index}":var})

keys=[key for key, value in ques_dict.items()]

df.columns=keys
for col in df.columns:
    print(col, ques_dict[col])
    for i in df[col].unique():
        print("    ", i)

# create dummies variables for multiple choice columns. 
df.cat3.str.split(";", expand=True)
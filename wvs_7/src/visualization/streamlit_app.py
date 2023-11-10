import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# dir(st)

st.title("Converting data visualization code to its Streamlit form")
st.markdown("""
-----
# Categorical data
""")

# Read the local CSV file
vi = pd.read_csv("../../data/processed/VNM.csv")
vi.columns=vi.columns.str.lower()

lkp_cols=vi.iloc[:, 2:40].columns.to_list()
for col in lkp_cols:
    st.write(col)
    value_counts = vi[col].value_counts()
    st.bar_chart(value_counts)

# Plot the horizontal bar chart
town_counts = vi["n_town"].value_counts()
st.bar_chart(town_counts)
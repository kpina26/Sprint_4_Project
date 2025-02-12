import pandas as pd
import streamlit as st

st.header('Car Advertisement')

df = pd.read_csv('./vehicles_us.csv')

# for graphs, use st.plotly_chart()
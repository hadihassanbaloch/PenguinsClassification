import streamlit as st
import  pandas as pd

st.title('🤖 Machine Learning App')

st.info('This app is to create a machine learning model')

with st.expander("View the Data"):
  st.write("**Penguin Dataset**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df
  

import streamlit as st
import  pandas as pd

st.title('🤖 Machine Learning App')

st.info('This app is to create a machine learning model')

with st.expander("View the Data"):
  st.write("**Penguin Dataset**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df
  st.write("**Features**")
  X = df.drop("species",axis=1)
  X
  st.write("**Target**")
  y = df.species
  y
with st.expander("Data Visualization"):
  st.write("** ScatterPlot to compare difference in body length with body mass based on species**")
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g',  color='species')
  
#Data preparation
#"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
with st.sidebar:
  st.header("Input Features")

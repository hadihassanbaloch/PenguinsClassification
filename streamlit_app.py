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

with st.sidebar:
  st.header("**Input Features**")
  island = st.selectbox("Islands", ("Torgersen", "Biscoe", "Dream"))
  st.write("You have selected:", island)
  bill_length_mm = st.slider("Bill length (mm):", 32.1,59.6, 43.1)
  st.write("You have selected:", bill_length_mm )
  bill_depth_mm = st.slider(" Bill depth (mm): ",13.1, 21.5,17.2)
  st.write("You have selected:",  bill_depth_mm)
  flipper_length_mm = st.slider("Flipper length (mm): ",172.0, 231.0, 201.0)
  st.write("You have selected:",  flipper_length_mm)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  st.write("You have selected:",  body_mass_g)
  gender = st.selectbox("Gender", ("Male", "Female"))
  st.write("You have selected:", gender)

data = {
  "island": island,
  "bill_length_mm": bill_length_mm,
  "bill_depth_mm" : bill_depth_mm,
  "flipper_length_mm" : flipper_length_mm,
  "body_mass_g":body_mass_g,
  "sex": gender
}
input_data = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_data, X], axis=0)

with st.expander('Input features'):
  st.write('**Input penguin**')
  input_data
  st.write('**Combined penguins data**')
  input_penguins

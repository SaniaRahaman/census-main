# Show complete dataset and summary in 'census_home.py'
# Import necessary modules.
import streamlit as st
import numpy as np
import pandas as pd
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df) :
  st.header('Census Visualisation Web App')
  st.text('This web app allows the user to explore and visualise the census data')
    
  # Display dataset within beta_expander.
  st.header('View Data')
  with st.beta_expander('View Data Set') :
    st.table(census_df.head())      
  # Show dataset summary on click of a checkbox.
  st.subheader('Columns Description') 
  if st.checkbox('Show Summary') :
    st.table(census_df.describe()) 

  beta_col1, beta_col2, beta_col3 = st.beta_columns(3)

  with beta_col1 :
    if st.checkbox('Show all column names') :
      st.table(list(census_df.columns))

  with beta_col2 :
    if st.checkbox('View columns data-type') :
      st.table(census_df.dtypes)    
  
  with beta_col3 :
    if st.checkbox('View column data') :
      column_data = st.selectbox('Select column', tuple(census_df.columns))
      st.table(census_df[column_data])    
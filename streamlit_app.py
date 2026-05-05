import streamlit as st
import pandas as pd
import numpy as np

#Dashboad Config
st.set_page_config(
    page_title="Security Dashboard", layout = "wide")

#Data Ingest
@st.cache_data
def Load_data():
    
    file_path = "data/WiresharkDataset.csv"
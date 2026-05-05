import streamlit as st
import pandas as pd
import numpy as np

#Dashboad Config
st.set_page_config(
    page_title="Security Dashboard", layout = "wide")

#Data Ingest
@st.cache_data
def Load_data():
    dtypes = {'Protocol': 'category'}
    file_path = "data/WiresharkDataset.csv"
    df = pd.read_csv(file_path, dtype=dtypes, index_col = "No.")

    #Clean Data
    df.columns = (df.columns.str.strip().str.lower().str.replace(' ', '_'))
    df['time'] = pd.to_timedelta(df['time'], unit='s')
    df['info'] = df['info'].fillna('').astype(str)
    
    return df


def main():
    df = Load_data()
    st.title("Security Dashboard")

main()
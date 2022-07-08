import streamlit as st
import pandas as pd
import numpy as np
import os
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from argparse import ArgumentParser

#@st.cache
#CachedStFunctionWarning: Your script uses st.markdown() or st.write() to write to your Streamlit app from within some cached code at main(). This code will only be called when we detect a cache "miss", which can lead to unexpected results."""

path = "./data/uLog01"
st. set_page_config(layout="wide") 


st.title(f"Contents of: {path}")


def main():
    for file in os.listdir(path):
        
        if file.endswith(".csv"):
            file_size = os.path.getsize(path +"/" +file)

            try:
                df = pd.read_csv(path +"/" +file).drop(['basestation', 'flight_number'],axis=1)
            except:
                df = pd.read_csv(path +"/" +file)
            
            #writes the file name
            #followed by the describe pandas data method
            #to a streamlit chart
            
            st.markdown("""---""")
            st.markdown("""""")

            st.title(f">{file}")
            df.timestamp = df.timestamp/1000/1000
            time_duration = df.timestamp.max() - df.timestamp.min()
  

            st.markdown(f"Size: {file_size/1000} kb | Time: {time_duration} s | Shape: {df.shape} | ")

            #st.dataframe(df.head())
            
            
            col1, col2 = st.columns(2)
            with col1:
                #st.write("empty block")
                st.line_chart(df.drop(['timestamp'], axis=1))

            with col2:
                #st.write("empty block")
                #st.table(df.describe())
                st.table(df.describe(datetime_is_numeric=False))
                #AgGrid(df.describe())
                #st.write(file)
                #st.line_chart(df)
                #fails because it's trying to convert a uuid to a int64?
                #streamlit.errors.StreamlitAPIException: ("Could not convert '224c2092-44e1-4b73-879c-d0ad0c4b4c87' with type str: tried to convert to int64", 'Conversion failed for column value with type object')


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--folder", type=str, default="./data/uLog01")
    main()

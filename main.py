import streamlit as st
import pandas as pd
import numpy as np
import os
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

#@st.cache
#CachedStFunctionWarning: Your script uses st.markdown() or st.write() to write to your Streamlit app from within some cached code at main(). This code will only be called when we detect a cache "miss", which can lead to unexpected results."""

path = "./data/uLog01"

st.title(f"Contents of: {path}")


def main():
    for file in os.listdir(path):
        
        if file.endswith(".csv"):
            file_size = os.path.getsize(path +"/" +file)

            try:
                df = pd.read_csv(path +"/" +file).drop(['timestamp', 'basestation', 'flight_number'],axis=1)
            except:
                df = pd.read_csv(path +"/" +file)
            
            #writes the file name
            #followed by the describe pandas data method
            #to a streamlit chart

            st.markdown("""---""")
            st.markdown("""""")

            st.title(f">{file}")
            st.markdown(f"Size: {file_size/1000} kb | Shape: {df.shape}")
            
            #st.dataframe(df.head())
            
            
            col1, col2 = st.columns(2)
            with col1:
                #st.write("empty block")
                st.line_chart(df)

            with col2:
                #st.write("empty block")
                st.dataframe(df.describe())
                #AgGrid(df.describe())
                #st.write(file)
                #st.line_chart(df)
                #fails because it's trying to convert a uuid to a int64?
                #streamlit.errors.StreamlitAPIException: ("Could not convert '224c2092-44e1-4b73-879c-d0ad0c4b4c87' with type str: tried to convert to int64", 'Conversion failed for column value with type object')


if __name__ == "__main__":
    main()

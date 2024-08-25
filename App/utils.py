import pandas as pd
import streamlit as st

def plot_radiation_data(dataframe, columns):
    if not isinstance(dataframe, pd.DataFrame):
        st.error("Expected input is a pandas DataFrame.")
        return
    
    if not all(isinstance(col, tuple) and len(col) == 4 for col in columns):
        st.error("Each item in 'columns' should be a tuple with (column_name, title, y_label, color).")
        return
    
    st.subheader('Radiation Data Plots')

    for col_name, title, y_label, color in columns:
        if col_name not in dataframe.columns:
            st.warning(f"Column '{col_name}' not found in DataFrame.")
            continue
        
        st.line_chart(dataframe[[col_name]], use_container_width=True, width=700)

        st.write(f"**{title}**")

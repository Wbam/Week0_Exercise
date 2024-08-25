import streamlit as st
import pandas as pd
import os

from utils import plot_radiation_data

def main():
    st.title('Radiation Data Visualization')

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        radiation_data = pd.read_csv(uploaded_file, parse_dates=True, index_col='Timestamp')
        
        st.write("Data Preview:")
        st.write(radiation_data.head())

        columns_to_plot = [
            ('GHI', 'Global Horizontal Irradiance', 'GHI (W/m²)', 'blue'),
            ('DNI', 'Direct Normal Irradiance', 'DNI (W/m²)', 'orange'),
            ('DHI', 'Diffuse Horizontal Irradiance', 'DHI (W/m²)', 'green'),
            ('Tamb', 'Ambient Temperature', 'Temperature (°C)', 'red')
        ]
        
        plot_radiation_data(radiation_data, columns_to_plot)

if __name__ == "__main__":
    main()

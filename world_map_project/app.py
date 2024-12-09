import streamlit as st
import pandas as pd
import plotly.express as px

# Title and Description
st.title("Interactive World Map Visualization")
st.write("Visualize data on a world map interactively!")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file with 'Country' and 'Value' columns", type="csv")

if uploaded_file:
    # Load the data
    data = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.write(data.head())

    # Check for required columns
    if 'Country' in data.columns and 'Value' in data.columns:
        # Create a world map
        st.write("### World Map")
        fig = px.choropleth(
            data,
            locations="Country",  # Name of the column containing country names
            locationmode="country names",  # Matches country names
            color="Value",  # Data column to color the map
            title="World Map",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig)

    else:
        st.error("The dataset must contain 'Country' and 'Value' columns.")
else:
    st.write("Upload a CSV file to get started!")


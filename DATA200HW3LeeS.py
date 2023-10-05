import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px





fishdf = pd.read_csv("Fish.csv")

fishdf_sorted = fishdf.sort_values(by="Weight")


# Filter data for Bream species
Bream_sorted = fishdf_sorted[fishdf_sorted["Species"] == "Bream"]

# Reshape the DataFrame into a tidy format
tidy_data = pd.melt(Bream_sorted, id_vars=["Weight"], value_vars=["Length1", "Length2", "Length3"], var_name="Length", value_name="Value")

# Create the line chart using Plotly Express, specifying x and y columns
fig = px.line(tidy_data, x="Weight", y="Value", color="Length", title="Line graph of Weight by Length 1, 2, 3 of Bream species")

# Update the y-axis label
fig.update_yaxes(title_text="Length")

# Display the plot using Streamlit
st.plotly_chart(fig)

# streamlit run DATA200HW3LeeS.py
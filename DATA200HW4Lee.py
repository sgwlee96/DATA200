import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.read_csv("Real_estate.csv")

# number of convenience stores vs house price of unit area
# distance to the nearest MRT station vs house price of unit area

st.title("The factors that affects to the price of the house")

df_conv_area = df.loc[:, ['house_age', 'distance_to_the_nearest_MRT_station', 'number_of_convenience_stores','house_price_of_unit_area']]
fig = px.scatter(df_conv_area, x="distance_to_the_nearest_MRT_station", y="house_price_of_unit_area", title="Correleation between Distance to MRT Station and House Price", 
                    labels={"distance_to_the_nearest_MRT_station" : "Distance to the Nearest MRT Station",
                            "house_price_of_unit_area" : "House Price Per Unit Area"})

st.plotly_chart(fig)

st.write("This graph shows the correleation between the distance to the nearest MRT station and the house price per unit area. \
From the graph above, we could observe that there is a negative relationship between the distance to MRT station and the price of the house. \
As the distance to the MRT station decreases, the price of the house increases.")


fig = px.scatter(df_conv_area, x="house_age", y="house_price_of_unit_area", title="Correleation between the house age and House Price", 
                    labels={"house_age" : "House Age", "house_price_of_unit_area" : "House Price Per Unit Area"})

st.plotly_chart(fig)

st.write("This graph shows the corrleation between the house age and house price. From the graph above, we cannot identify clear correlation between \
    the house age and the house price. Thus, we can conclude that the house age does not significantly affect to the price of the house.")

#streamlit run DATA200HW4Lee.py                 

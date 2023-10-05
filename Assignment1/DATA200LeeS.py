import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO

# Import datasets 
# Read Fish.csv Dataset
fishdf = pd.read_csv("Fish.csv")
mtFlowerdf = pd.read_csv("mountain_flowers.csv")
realEdf = pd.read_csv("Real_estate.csv")
toydf = pd.read_csv("toy_dataset.csv")

# create Dashboard

st.set_page_config(
    page_title:="DATA200 Assignment 1 Dashboard",
    page_icon:="📊",  # You can use an emoji as the icon
    layout:="wide"
)


fishdf_sorted = fishdf.sort_values(by="Weight")

col1, col2 = st.columns(2)

with col1:

    st.title("Fish Data")

    option = st.selectbox(
    "Which species do you want to filter?",
    ('Roach', 'Perch', 'Smelt', 'Parkki', 'Pike', 'Bream', 'Whitefish'),
    )


    # Filter data for Bream species
    Bream_sorted = fishdf_sorted[fishdf_sorted["Species"] == option]

    # Reshape the DataFrame into a tidy format
    tidy_data = pd.melt(Bream_sorted, id_vars=["Weight"], value_vars=["Length1", "Length2", "Length3"], var_name="Length", value_name="Value")

    # Create the line chart using Plotly Express, specifying x and y columns
    fig = px.line(tidy_data, x="Weight", y="Value", color="Length", title=f"Line graph of Weight by Length 1, 2, 3 of {option} species")

    # Update the y-axis label
    fig.update_yaxes(title_text="Length")

    # Display the plot using Streamlit
    st.plotly_chart(fig)

    background_color = "#262730"

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Perch', 'Bream', 'Roach', 'Pike', 'Smelt', 'Parkki', 'Whitefish'
    sizes = [56, 35, 20, 17, 14, 11, 6]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    fig1.set_facecolor(background_color + "00")

    # Set label and tick color to white
    ax1.tick_params(axis='both', colors='white')
    for text in ax1.texts:
        text.set_color('white')

    ax1.set_title("Distribution of Fish Species", color='#ffffff')
    st.pyplot(fig1)

    image_stream = BytesIO()
    plt.savefig(image_stream, format="png")
    image_stream.seek(0)

    st.download_button(
        label="Download image",
        data=image_stream,
        file_name="Pie_Chart.png",
        mime="image/png"
    )
#######################################################################################################################################################

with col2:
    st.title("Real Estate data")

    values = st.slider(
    'Select a range of values',
    0.0, 6488.021, (1000.0, 4000.0))

    df_conv_area = realEdf.loc[:, ['house_age', 'distance_to_the_nearest_MRT_station', 'number_of_convenience_stores','house_price_of_unit_area']]
    mrtConvArea = df_conv_area[(df_conv_area['distance_to_the_nearest_MRT_station'] > values[0]) & (df_conv_area['distance_to_the_nearest_MRT_station'] < values[1])]
    fig = px.scatter(mrtConvArea, x="distance_to_the_nearest_MRT_station", y="house_price_of_unit_area", title="Correleation between Distance to MRT Station and House Price", 
                        labels={"distance_to_the_nearest_MRT_station" : "Distance to the Nearest MRT Station",
                                "house_price_of_unit_area" : "House Price Per Unit Area"})
    st.plotly_chart(fig)

    st.write("This graph shows the correleation between the distance to the nearest MRT station and the house price per unit area. \
    From the graph above, we could observe that there is a negative relationship between the distance to MRT station and the price of the house. \
    As the distance to the MRT station decreases, the price of the house increases.")


    values1 = st.slider(
    'Select a range of values',
    0.0, 43.8, (10.0, 30.0))

    houseAgedf = df_conv_area[(df_conv_area['house_age'] > values1[0]) & (df_conv_area['house_age'] < values1[1])]
    fig = px.scatter(houseAgedf, x="house_age", y="house_price_of_unit_area", title="Correleation between the house age and House Price", 
                        labels={"house_age" : "House Age", "house_price_of_unit_area" : "House Price Per Unit Area"})

    st.plotly_chart(fig)

    st.write("This graph shows the corrleation between the house age and house price. From the graph above, we cannot identify clear correlation between \
        the house age and the house price. Thus, we can conclude that the house age does not significantly affect to the price of the house.")

#######################################################################################################################################################

# Table
st.title("Toy dataset")
city_cnt_male = toydf[toydf['Gender']=='Male']['City'].value_counts()
city_cnt_female = toydf[toydf['Gender']=='Female']['City'].value_counts()

with st.expander("Click to see the graph"):
    data = {
    'Male': city_cnt_male,
    'Female': city_cnt_female
    }
    bar_chart_data = pd.DataFrame(data)

    # Display the bar chart using Streamlit
    st.bar_chart(bar_chart_data, color=["#FF0000", "#0000FF"])

    # Additional settings
    # st.xticks(rotation=30)
    # st.legend(['Male', 'Female'])
    # st.title("City count of Male and Female")
    # st.ylabel("Count")
    # st.xlabel("Cities")


# streamlit run DATA200LeeS.pyls

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import ast
import os

# Import datasets 
# Read Fish.csv Dataset
file_path = os.path.join(os.path.dirname(__file__), "imdb_movies_shows.csv")
df = pd.read_csv(file_path)
# create Dashboard

for i in range(len(df['genres'])):
    df['genres'][i] = ast.literal_eval(df['genres'][i])

for i in range(len(df['production_countries'])):
    df['production_countries'][i] = ast.literal_eval(df['production_countries'][i])

st.title('Movie and TV Show Dashboard')

# Sidebar for filtering data
st.sidebar.header('Filter Data')
min_year, max_year = st.sidebar.slider('Select release year range', min_value=df['release_year'].min(), max_value=df['release_year'].max(), value=(df['release_year'].min(), df['release_year'].max()))
selected_types = st.sidebar.multiselect('Select type', df['type'].unique(), default=df['type'].unique())

# Filter DataFrame based on user selection
filtered_df = df[(df['release_year'] >= min_year) & (df['release_year'] <= max_year) & (df['type'].isin(selected_types))]

# Visualization 1
def plot_count(df: pd.core.frame.DataFrame, col_list: list, title_name: str='Train') -> None:
    for col in col_list:
        # Creating outer and inner pie charts using Plotly Express
        fig = px.sunburst(
            df, 
            path=[col], 
            title=f'{title_name} Dataset Distribution of {col}',
            width=700,
            height=400,
            color_discrete_sequence=['#FF6347', '#20B2AA'],  # Set colors
        )

        # Displaying the plot in Streamlit
        st.plotly_chart(fig)

# Streamlit app
st.title('Movie and TV Show Dashboard')
plot_count(df, ['type'], ' ')
st.text("""The bar plot shows the count of shows and movies based on the selected filters. \n 
It provides an overview of the distribution of show and movie types.""")

# Visualization 2: Violin plot of 'runtime' by 'type'
st.subheader('Violin Plot of Runtime by Type')
runtime_violin = px.violin(filtered_df, x='type', y='runtime', box=True, title='Violin Plot of Runtime by Type', color='type', color_discrete_map={'SHOW': 'lightblue', 'MOVIE': 'lightgreen'})
st.plotly_chart(runtime_violin)
st.write("""
The violin plot displays the distribution of runtime for each type (show or movie). 
It reveals that movies generally have a wider range of runtimes compared to shows, and there's a higher concentration of shorter runtimes for shows. 
This insight could be helpful for viewers looking for content of a specific duration.
""")

# Visualization 3: Box plot of IMDb scores by 'type'
st.subheader('Box Plot of IMDb Scores by Type')
imdb_box_plot = px.box(filtered_df, x='type', y='imdb_score', points='all', title='Box Plot of IMDb Scores by Type', color='type', color_discrete_map={'SHOW': 'lightblue', 'MOVIE': 'lightgreen'})
st.plotly_chart(imdb_box_plot)
st.write("""
The box plot showcases the distribution of IMDb scores for shows and movies. 
It indicates that movies tend to have a slightly higher median IMDb score compared to shows, and there is a wider spread of scores for movies. 
This suggests that movies may have more varied audience reactions, while shows exhibit a more consistent rating pattern.
""")

# Visualization 4: Heatmap of correlation between numeric columns
st.subheader('Correlation Heatmap')
corr_heatmap = px.imshow(filtered_df.corr(), title='Correlation Heatmap')
st.plotly_chart(corr_heatmap)
st.write("""
The heatmap visualizes the correlation between numeric columns such as release year, runtime, IMDb score, and IMDb votes. 
It reveals that IMDb score and IMDb votes are positively correlated, indicating that highly rated content tends to attract more votes. 
Additionally, there's a negative correlation between release year and IMDb score, suggesting that older content may have slightly higher IMDb scores.
""")

# Visualization 5: word cloud

def plot_wordcloud(text):
    comment_words = ' '
    stopwords = set(STOPWORDS)
    
    for val in text:
        val = str(val)
        tokens = val.split()
        
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
            
        for words in tokens:
            comment_words = comment_words + words + ' '
            
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(comment_words)
    
    st.image(wordcloud.to_image(), use_column_width=True)
    # st.pyplot()

# Select a column for word cloud
selected_column = st.selectbox('Select a column for word cloud:', ['title', 'type', 'genres', 'production_countries'])

# Generate word cloud
plot_wordcloud(df[selected_column])
# Display the filtered DataFrame
st.subheader('IMDB Movie and Shows Table')

# Sort DataFrame by IMDb scores and votes
sorted_df = filtered_df.sort_values(by=['imdb_votes', 'imdb_score'], ascending=[False, False])

# Display the sorted DataFrame
st.write(sorted_df)

# streamlit run DATA200LeeS.py

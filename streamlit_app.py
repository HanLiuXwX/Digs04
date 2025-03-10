import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data
file_path = "./Cleaned_Animation_Movies.csv"
df = pd.read_csv(file_path)

# Sidebar filters
st.sidebar.header("Filter Options")
selected_years = st.sidebar.slider("Select Year Range", int(df["year"].min()), int(df["year"].max()), (1990, 2024))

# Filter data
df_filtered = df[df["year"].between(selected_years[0], selected_years[1])]

# Movie Count Line Chart
st.subheader("Number of Animated Movies Over Time")
yearly_stats = df_filtered.groupby("year").size().reset_index(name="movie_count")
fig_movie_count = px.line(yearly_stats, x="year", y="movie_count", title="Number of Animation Movies Released (1990-2024)", markers=True)
st.plotly_chart(fig_movie_count)

# Rating vs Revenue Scatter Plot
st.subheader("Do Higher Ratings Lead to Higher Revenue?")
fig_scatter = px.scatter(df_filtered, x="vote_average", y="revenue", size="vote_count", color="year",
                         title="Ratings vs. Revenue", hover_name="title", size_max=30, opacity=0.7, log_y=True)
st.plotly_chart(fig_scatter)

# Word Cloud
st.sidebar.header("Word Cloud Options")
wordcloud_option = st.sidebar.radio("Select Word Cloud Type", ["Top 10 Revenue Movies", "Top 10 Budget Movies"])
if wordcloud_option == "Top 10 Revenue Movies":
    top_movies = df.nlargest(10, "revenue")["title"].tolist()
    title = "Top 10 Highest Grossing Animated Movies"
else:
    top_movies = df.nlargest(10, "budget")["title"].tolist()
    title = "Top 10 Most Expensive Animated Movies"

wordcloud_text = " ".join(top_movies)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(wordcloud_text)
st.subheader(title)
st.image(wordcloud.to_array())

